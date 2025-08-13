📚 Bestsellers Data Analysis
📌 Overview
This project analyzes a dataset of bestselling books to uncover:

📖 Which authors appear most frequently

⭐ How average ratings vary by genre

The analysis uses Python and Pandas for data cleaning, aggregation, and exporting results to CSV files.

📂 Dataset
The dataset bestsellers_with_categories.csv contains the following columns before cleaning:

Column Name	Description
Name	Title of the book
Author	Author's name
User Rating	Average rating given by users
Reviews	Number of user reviews
Price	Price in USD
Year	Publication year
Genre	Genre category of the book

🛠 Data Cleaning & Transformation
Load dataset into a Pandas DataFrame.

Preview data with .head() and .tail().

Inspect dataset using .columns and .describe().

Clean the data:

🧹 Remove duplicates → drop_duplicates()

✏️ Rename columns:

Name → Title

Year → Publication Year

User Rating → Rating

💲 Convert Price to a float data type.

Aggregate data:

👑 Top Authors → Count occurrences of each author.

📊 Average Ratings by Genre → Group by Genre and calculate the mean.

📊 Example Output
👑 Top 10 Bestselling Authors
Author	Book Count
Author A	12
Author B	10
Author C	9

📁 Saved as top_10_authors.csv

⭐ Average Rating by Genre
Genre	Avg Rating
Fiction	4.63
Non-Fiction	4.55

📁 Saved as avg_rating_by_genre.csv

🔍 Project Insights (from dataset)
🥇 Top Author: INSERT AUTHOR NAME with X books on the bestseller list.

📚 Most Popular Genre: INSERT GENRE with an average rating of X.XX.

💡 Books in INSERT GENRE tend to have slightly higher ratings than INSERT OTHER GENRE.

🚀 Requirements
Install dependencies with:

bash
Copy
Edit
pip install pandas
▶️ How to Run
Place bestsellers_with_categories.csv in the same folder as analysis.py.

Run:

bash
Copy
Edit
python analysis.py
Output files will be generated in the same directory:

top_10_authors.csv

avg_rating_by_genre.csv

📈 Skills Demonstrated

📥 Data loading & exploration with Pandas

🧹 Data cleaning (duplicates removal, column renaming, type conversion)

📊 Grouping and aggregation

💾 Exporting results to CSV