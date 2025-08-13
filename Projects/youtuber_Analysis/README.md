📺 YouTube Channels Data Analysis & Visualization
📌 Overview
This project analyzes the most subscribed YouTube channels dataset to uncover patterns in subscriber counts, content categories, years active, and video production.
Using Python, Pandas, Seaborn, and Matplotlib, the project creates clear, professional visualizations to communicate insights effectively.

📂 Dataset
The dataset most_subscribed_youtube_channels.csv contains the following columns:

Column Name	Description
channel	Name of the YouTube channel
subscribers	Total number of subscribers
video count	Number of videos uploaded
category	Channel's main content category
started	Year the channel started

🛠 Analysis & Visualizations
The analysis focuses on four main questions:

What is the distribution of subscriber counts across all channels?

Visualization: Histogram with kernel density estimate (KDE)

Insight: Reveals whether most channels have modest subscriber bases or if the distribution is skewed by a few massive channels.

What is the distribution of channels by content category?

Visualization: Pie chart

Insight: Shows which categories dominate the platform by number of channels.

When did most top channels start?

Visualization: Box plot of the started year

Insight: Highlights growth patterns and entry periods for popular channels.

Is there a relationship between number of videos and subscribers?

Visualization: Scatter plot with log-scaled X-axis

Insight: Identifies whether consistent content production correlates with subscriber count.

🔍 Key Insights
📈 Subscriber distribution is highly skewed — a few channels have subscriber counts in the hundreds of millions, while most are below 50M.

🎭 Entertainment and Music categories dominate in terms of channel representation.

📅 Many top channels were started between 2010–2015, aligning with YouTube’s rapid growth period.

🎥 High subscriber counts don’t always require massive video libraries — quality and virality matter more than quantity.

🚀 Requirements
Install dependencies:

pip install pandas matplotlib seaborn

▶️ How to Run
Place most_subscribed_youtube_channels.csv in the same folder as the Python script.

Run: 
python youtube_analysis.py

Generated plots will be saved as:

subscriber_histogram.png

subscribers_by_category.png

years_started_boxplot.png

subscribers_vs_videos.png

📈 Skills Demonstrated
Data cleaning & formatting with Pandas

Professional visualization with Matplotlib & Seaborn

Scaling & formatting large numeric values for clarity

Data storytelling through visual insights