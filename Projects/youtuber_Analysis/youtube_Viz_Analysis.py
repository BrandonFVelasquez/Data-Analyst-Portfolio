import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# Load data
df = pd.read_csv('most_subscribed_youtube_channels.csv')

# Formatter for millions
def millions(x, pos):
    return f'{x/1_000_000:.1f}M'

million_formatter = mticker.FuncFormatter(millions)

# Histogram of Subscribers
plt.figure(figsize=(10, 6))
sns.histplot(df['subscribers'], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title('Subscriber Count', fontsize=16)
plt.xlabel('Number of Subscribers (millions)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.gca().xaxis.set_major_formatter(million_formatter)
plt.tight_layout()
plt.show()

# Pie Chart of subscribers by category (original style, just improved colors & readability)
category_counts = df['category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 10}
)
plt.title('Channels by Category', fontsize=16)
plt.tight_layout()
plt.show()

# Box Plot of Years Started
plt.figure(figsize=(10, 6))
sns.boxplot(x='started', data=df, color='lightgreen')
plt.title('Distribution of Years Started', fontsize=16)
plt.xlabel('Year Started', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter Plot of Subscribers vs. Videos
plt.figure(figsize=(10, 6))
sns.scatterplot(x='video count', y='subscribers', data=df, hue='category', palette='tab10', alpha=0.7)
plt.title('Subscribers vs. Videos', fontsize=16)
plt.xlabel('Number of Videos', fontsize=12)
plt.ylabel('Number of Subscribers (millions)', fontsize=12)
plt.gca().yaxis.set_major_formatter(million_formatter)
plt.xscale('log')  # spreads clustered values
plt.legend(title='Category', fontsize=9)
plt.tight_layout()
plt.show()

# Export the plots as image files
plt.figure(figsize=(10, 6))
sns.histplot(df['subscribers'], bins=30, kde=True)
plt.title('Subscriber Count')
plt.xlabel('Number of Subscribers')
plt.ylabel('Frequency')
plt.savefig('plots/subscriber_histogram.png')
plt.close()

plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Subscribers by Category')
plt.savefig('plots/subscribers_by_category.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='started', data=df)
plt.title('Distribution of Years Started')
plt.xlabel('Year Started')
plt.savefig('plots/years_started_boxplot.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='video count', y='subscribers', data=df)
plt.title('Subscribers vs. Videos')
plt.xlabel('Number of Videos')
plt.ylabel('Number of Subscribers')
plt.savefig('plots/subscribers_vs_videos.png')
plt.close()
