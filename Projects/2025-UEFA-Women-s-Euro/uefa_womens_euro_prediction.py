import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random

# --- Load and clean data
df = pd.read_csv("UEFA Womens Euro 2025 Analysis - Overview_Stats.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")
numeric_columns = [
    'Goals_per_Match', 'Expected_Goals', 'Avg_Possession',
    'Shots_on_Target_per_Match', 'Big_Chances', 'Big_Chances_Missed',
    'Goals_Conceded_per_Match', 'Expected_Goals_Conceded',
    'Interceptions_per_Match', 'Clearances_per_Match'
]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
df = df.dropna(subset=numeric_columns)

# --- Offensive & Defensive models
X_off = df[['Goals_per_Match', 'Expected_Goals', 'Avg_Possession',
            'Shots_on_Target_per_Match', 'Big_Chances', 'Big_Chances_Missed']]
y_off = df['Goals_per_Match']
X_off = sm.add_constant(X_off)
off_model = sm.GLM(y_off, X_off, family=sm.families.Poisson()).fit()

X_def = df[['Goals_Conceded_per_Match', 'Expected_Goals_Conceded',
            'Interceptions_per_Match', 'Clearances_per_Match']]
y_def = df['Goals_Conceded_per_Match']
X_def = sm.add_constant(X_def)
def_model = sm.GLM(y_def, X_def, family=sm.families.Poisson()).fit()

# --- Stats for Spain & England
spain_stats_off = pd.DataFrame([{
    'const': 1,
    'Goals_per_Match': 3.4,
    'Expected_Goals': 3.06,
    'Avg_Possession': 0.728,
    'Shots_on_Target_per_Match': 8.2,
    'Big_Chances': 20,
    'Big_Chances_Missed': 11,
}])
england_stats_off = pd.DataFrame([{
    'const': 1,
    'Goals_per_Match': 3.0,
    'Expected_Goals': 2.92,
    'Avg_Possession': 0.608,
    'Shots_on_Target_per_Match': 6.0,
    'Big_Chances': 27,
    'Big_Chances_Missed': 16,
}])
spain_stats_def = pd.DataFrame([{
    'const': 1,
    'Goals_Conceded_per_Match': 0.6,
    'Expected_Goals_Conceded': 0.72,
    'Interceptions_per_Match': 9,
    'Clearances_per_Match': 8
}])
england_stats_def = pd.DataFrame([{
    'const': 1,
    'Goals_Conceded_per_Match': 1.2,
    'Expected_Goals_Conceded': 1.42,
    'Interceptions_per_Match': 11,
    'Clearances_per_Match': 10
}])

# --- Predict 90-min average goals
spain_avg_goals = (off_model.predict(spain_stats_off)[0] + def_model.predict(england_stats_def)[0]) / 2
england_avg_goals = (off_model.predict(england_stats_off)[0] + def_model.predict(spain_stats_def)[0]) / 2

print(f"\nPredicted 90-Minute Goals:")
print(f"  🇪🇸 Spain:   {spain_avg_goals:.2f}")
print(f"  🏴 England: {england_avg_goals:.2f}")

# --- Simulate 25,000 matches with extra time + penalties
n_simulations = 25000
results = []
scorelines = []
et_results = []
penalty_winners = []

for _ in range(n_simulations):
    spain_goals_90 = np.random.poisson(spain_avg_goals)
    england_goals_90 = np.random.poisson(england_avg_goals)

    if spain_goals_90 > england_goals_90:
        results.append("Spain")
    elif england_goals_90 > spain_goals_90:
        results.append("England")
    else:
        # Extra Time
        spain_et = np.random.poisson(spain_avg_goals / 3)
        england_et = np.random.poisson(england_avg_goals / 3)

        spain_total = spain_goals_90 + spain_et
        england_total = england_goals_90 + england_et

        if spain_total > england_total:
            results.append("Spain (ET)")
            et_results.append("Spain")
        elif england_total > spain_total:
            results.append("England (ET)")
            et_results.append("England")
        else:
            # Penalty shootout
            winner = random.choice(["Spain", "England"])
            results.append(f"{winner} (P)")
            penalty_winners.append(winner)

    scorelines.append((spain_goals_90, england_goals_90))

# --- Count final results
result_counts = Counter(results)
score_counts = Counter(scorelines).most_common(10)
et_counts = Counter(et_results)
penalty_counts = Counter(penalty_winners)

# --- Print Results
print(f"\nSimulated {n_simulations} Matches (with ET & Penalties):")
for outcome, count in result_counts.items():
    print(f"  {outcome}: {count} ({count / n_simulations:.2%})")

print("\n🔝 Most Common Regulation-Time Scorelines:")
for score, count in score_counts:
    print(f"  Spain {score[0]} - England {score[1]} : {count} times")

print("\n⚽ Extra Time Wins:")
for team, count in et_counts.items():
    print(f"  {team}: {count} ({count / n_simulations:.2%})")

print("\n🎯 Penalty Shootout Wins:")
for team, count in penalty_counts.items():
    print(f"  {team}: {count} ({count / n_simulations:.2%})")

# --- Plot 90-min Goal Distribution
spain_goals_all = [s for s, _ in scorelines]
england_goals_all = [e for _, e in scorelines]
plt.figure(figsize=(10, 5))
plt.hist(spain_goals_all, bins=range(0, max(spain_goals_all)+2), alpha=0.6, label='Spain')
plt.hist(england_goals_all, bins=range(0, max(england_goals_all)+2), alpha=0.6, label='England')
plt.title("90-Minute Goal Distribution (Spain vs. England)")
plt.xlabel("Goals")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

# --- Plot Outcome Breakdown (Reg, ET, P)
categories = ["Spain", "England", "Spain (ET)", "England (ET)", "Spain (P)", "England (P)"]
frequencies = [result_counts.get(cat, 0) for cat in categories]

plt.figure(figsize=(10, 5))
plt.bar(categories, frequencies, color='lightcoral')
plt.title("Match Outcome Breakdown (25,000 Simulations)")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Export full outcome summary
outcomes_df = pd.DataFrame(result_counts.items(), columns=['Outcome', 'Count'])
outcomes_df['Percentage'] = (outcomes_df['Count'] / n_simulations * 100).round(2)
outcomes_df.to_csv("match_outcomes.csv", index=False)

# --- Export top 10 regulation-time scorelines
top_scores_df = pd.DataFrame(score_counts, columns=['Scoreline', 'Count'])
top_scores_df[['Spain_Goals', 'England_Goals']] = pd.DataFrame(top_scores_df['Scoreline'].tolist(), index=top_scores_df.index)
top_scores_df.drop(columns='Scoreline', inplace=True)
top_scores_df.to_csv("top_scorelines.csv", index=False)

# --- Export all 90-min scorelines (optional for heatmap/analysis)
scorelines_df = pd.DataFrame(scorelines, columns=['Spain_90', 'England_90'])
scorelines_df.to_csv("all_scorelines.csv", index=False)

# --- Export Extra Time and Penalty Wins
et_df = pd.DataFrame(et_counts.items(), columns=['ET_Winner', 'Count'])
et_df['Percentage'] = (et_df['Count'] / n_simulations * 100).round(2)
et_df.to_csv("extra_time_wins.csv", index=False)

penalty_df = pd.DataFrame(penalty_counts.items(), columns=['Penalty_Winner', 'Count'])
penalty_df['Percentage'] = (penalty_df['Count'] / n_simulations * 100).round(2)
penalty_df.to_csv("penalty_wins.csv", index=False)

