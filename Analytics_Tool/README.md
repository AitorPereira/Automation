# 📊 Data Analyzer #

Data Analyzer is a Python application that allows you to analyze CSV files interactively.
It provides tools to explore datasets, calculate statistics, and generate bar or line charts from numeric columns.

## 🚀 Features ##

•Load CSV files and parse data into dictionaries.

•Display dataset summary (rows, columns, first 5 records).

•Analyze numeric columns with key statistics:

•Minimum, Maximum, Sum, Average, Median, Standard Deviation.

•Group values by one column and calculate averages for another.

•Generate Bar Charts and Line Charts using matplotlib.

•Interactive menu for easy navigation.

_____________________________________________________________________________________________________________________________________________________________________________________

### 📂 Project Structure ###
Data-Analyzer/

│── app.py                # Main program

│── README.md             # Project documentation

│── requirements.txt      # Python dependencies (optional)

│── sample_data.csv       # Example dataset

_____________________________________________________________________________________________________________________________________________________________________________________
### 🛠️ Requirements ###

•Python 3.8+

•Libraries:

    -matplotlib
  
    -statistics (comes with Python standard library)

You can install dependencies with:
pip install matplotlib
_____________________________________________________________________________________________________________________________________________________________________________________
### ▶️ Usage ###

Run the application from the terminal:
python app.py

Example Flow:

1.Enter the path of a CSV file.

2.View dataset summary.

3.Choose an option from the interactive menu:

  •Analyze numeric column → shows statistics.
  
  •Generate bar chart → average of Y by X.
  
  •Generate line chart → average of Y by X over time/sequence.
  •Exit
_____________________________________________________________________________________________________________________________________________________________________________________
### 📈 Example Output ###
Data Summary:

=== DATA SUMMARY ===
Rows: 500
Columns: age, height, weight, gender, score

First 5 rows:

Row 1: {'age': 25, 'height': 175, 'weight': 70, 'gender': 'M', 'score': 85}

Row 2: {'age': 30, 'height': 180, 'weight': 82, 'gender': 'F', 'score': 90}
...

Chart Example:

•Bar Chart (Average score by gender)

•Line Chart (Average weight by age)
_____________________________________________________________________________________________________________________________________________________________________________________
### 📌 Next Steps ###

•Add support for exporting charts as images.

•Handle missing values more robustly.

•Extend analysis with correlation or trend detection.

_____________________________________________________________________________________________________________________________________________________________________________________
### 📜 License ###

This project is open-source under the MIT License.
