import os
import csv
import statistics
from tracemalloc import Statistic
import matplotlib
import matplotlib.pyplot as plt
from numpy import minimum

def load_data_csv(file_path):
    """
    Load data from a CSV file

    Args:
        file_path: File CSV path to load
    
    Return:
        tuple: (headers, data) where headers is a column name list and data is a list of dictionaries with data
    """

    try:
        #Verify that the file exists
        if not os.path.exists(file_path):
            print (f"Error: the file {file_path} does not exist.")
            return None, None #Tuple

        #Read CSV file
        headers = []
        data = []

        with open(file_path, 'r', newline='', encoding='utf-8') as file_csv:
            #Create a reader CSV
            reader = csv.reader(file_csv)
            #Read the first row as header
            headers = next(reader)

            #Read data
            for row in reader:
                #Create a dictionary for each row
                if len(row) == len(headers):
                    row_dict = {}
                    for i, value in enumerate(row):
                        try:
                        #First try to convert it into an int
                            row_dict[headers[i]] = int(value)
                        except ValueError:
                            try:
                                #If it's not integer, try to convert it into a float
                                row_dict[headers[i]] = value
                            except ValueError:
                                #If it's not a number, leave it a string
                                row_dict[headers[i]] = value
                    data.append(row_dict)
            print (f"{len(data)} rows of data has been loaded with {len(headers)} columns")
            return headers, data

    except Exception as e:
        print(f" Error loading CSV file: {e}")
        return None, None #Tuple

def display_data_summary(headers, data):
    """
    Display a summary of loaded data
    
    Args:
        headers: List of column names
        data: List of dictionaries with data
    """

    if not data:
        print("No data to display")
        return

    print ("\n=== DATA SUMMARY ===")
    print (f"Data rows: {len(data)}")
    print (f"Columns: {'. '.join(headers)}")

    #Display the first 5 rows
    print ("\nFirst 5 rows:")
    for i, row in enumerate(data[:5]):
        print(f"Row {i+1}: {row}")

headers, data = load_data_csv("/Users/aitor/Documents/Python/Automation/Analytics_Tool/gym_data_500.csv")
display_data_summary(headers, data)

def analize_numerical_column(data, column):
    """
    Performs a statistical analysis of a numerical column

    Args:
        data: List of dictionaries with data
        column: Name of the column to analyze
    
    Return:
        dict: Dictionaire with column statistic
    """

    #Extract values of the column, filtering only numerics values
    values=[]
    for row in data:
        if column in row and isinstance(row[column], (int, float)):
            values.append(row[column])

    #Verify there are numeric values
    if not values:
        print (f"There are not numeric values found in the column: '{column}' .")
        return None
    
    #Calculate statistics
    statistic = {
        'column' : column,
        'total_values' : len(values),
        'minimum' : min(values),
        'maximum' : max(values),
        'sum' : sum(values),
        'average' : sum(values) / len(values),
        'median' : statistics.median(values),
        'standard_deviation' : statistics.stdev(values) if len(values) > 1 else 0 
    }

    return statistic

def display_statistic(statistic):
    """
    Display statistics of a column

    Args:
        statistics: Dictionary with statistics of the column
    """

    if not statistic:
        return

    print (f"\n=== COLUMN STATISTICS '{statistic['column']}' ===")
    print (f"Total values: {statistic['total_values']}")
    print (f"Minimum value: {statistic['minimum']}")
    print (f"Maximum value: {statistic['maximum']}")
    print (f"Sum: {statistic['sum']}")
    print (f"Average: {statistic['average']:.2f}")
    print (f"Median: {statistic['median']:.2f}")
    print (f"Standard deviation: {statistic['standard_deviation']:.2f}")

def generate_bars_graphic(data, column_x, column_y, title=None):
    """
    Generate bars graphic displaying the average of Y values for X values

    Args:
        data: List of dictionaries with data
        column_x: Name of the column for X axis
        column_y: Name of the colum for Y axis
        title: Graphic title (optional)

    Returns:
        bool: True if it generated succesfully, False in oposite case
    """

    try:
        #Group data for X values and calculate Y average
        groups_x = {}

        for row in data:
            if column_x in row and column_y in row and isinstance(row[column_y], (int, float)):
                value_x = str(row[column_x])
                value_y = row[column_y]

                if value_x not in groups_x:
                    groups_x[value_x] = []

                groups_x[value_x].append(value_y)

        #Calculate average per group
        values_x = []
        averages_y= []

        for value_x, values_y in groups_x.items():
            if values_y: #Verify there are values
                values_x.append(value_x)
                averages_y.append(sum(values_y) / len(values_y))

        #Verify if there is enough data
        if len(values_x) < 2:
            print("There is not enough data to generate traffic")
            return False
        
        #Create graphic
        plt.figure(figsize=(10, 6))
        plt.plot(values_x, averages_y, color='green')

        #Add labels and title
        plt.xlabel(column_x)
        plt.ylabel(f"Average of {column_y}")
        plt.title(title or f"Average of {column_y} by {column_x}")

        #Rotate labels of X axis if there are many
        if len(values_x) > 5:
            plt.xticks(rotation=45, ha='right')

        #Adjust layout
        plt.tight_layout()

        #Display graphic
        plt.show()

        return True

    except Exception as e:
        print(f"Error generating the grafic: {e}")
        return False

def generate_lines_graphic(data, column_x, column_y, title=None):
    """
    Generate lines graphic displaying the average of Y values for X values

    Args:
        data: List of dictionaries with data
        column_x: Name of the column for X axis
        column_y: Name of the colum for Y axis
        title: Graphic title (optional)

    Returns:
        bool: True if it generated succesfully, False in oposite case
    """

    try:
        #Group data for X values and calculate Y average
        groups_x = {}

        for row in data:
            if column_x in row and column_y in row and isinstance(row[column_y], (int, float)):
                value_x = str(row[column_x])
                value_y = row[column_y]

                if value_x not in groups_x:
                    groups_x[value_x] = []

                groups_x[value_x].append(value_y)

        #Calculate average per group
        values_x = []
        averages_y= []

        for value_x, values_y in groups_x.items():
            if values_y: #Verify there are values
                values_x.append(value_x)
                averages_y.append(sum(values_y) / len(values_y))

        #Verify if there is enough data
        if len(values_x) < 2:
            print("There is not enough data to generate traffic")
            return False
        
        #Create graphic
        plt.figure(figsize=(10, 6))
        plt.bar(values_x, averages_y, color='skyblue')

        #Add labels and title
        plt.xlabel(column_x)
        plt.ylabel(f"Average of {column_y}")
        plt.title(title or f"Average of {column_y} by {column_x}")

        #Rotate labels of X axis if there are many
        if len(values_x) > 5:
            plt.xticks(rotation=45, ha='right')

        #Adjust layout
        plt.tight_layout()

        #Display graphic
        plt.show()

        return True

    except Exception as e:
        print(f"Error generating the grafic: {e}")
        return False

def main():
    print ("=== DATA ANALYZER ===")

    #Request CSV file path
    file_path = input("Insert the CSV file path to analyze: ")

    #Load data
    headers, data = load_data_csv(file_path)

    if not data:
        print("Loading files was not possible. Finishing program.")
        return

    #Display data summary
    display_data_summary(headers, data)

    while True:
        print ("\nOptions:")
        print("1. Analyze numeric column")
        print("2. Generate bars graphic")
        print("3. Generate lines graphic")
        print("4. Exit")

        option = input("\nSelect your option (1-4): ")
        
        if option == "1":
            #Analize a numeric column
            print ("\nAvailable columns:")
            for i, column in enumerate(headers, 1):
                print (f"{i}. {column}")

            index_column = int(input("\Select the number of columns to analyze: ")) -1
            if 0 <= index_column < len(headers):
                column = headers[index_column]
                statistic = analize_numerical_column(data, column)
                if statistic:
                    display_statistic(statistic)
                else:
                    print("Invalid option")
            
        elif option == "2":
            #Generate graphic bars
            print("\nSelect the columns for the bars graphic:")

            print("\n Columns for X axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_x = int(input("\Select the number of column for the X axis: ")) -1

            print("\n Columns for Y axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_y = int(input("\Select the number of column for the Y axis: ")) -1

            if 0 <= index_x < len(headers) and 0 <= index_y < len(headers):
                column_x = headers[index_x]
                column_y = headers[index_y]
                title = input("\nInsert a title for the graphic (optional): ")

                generate_bars_graphic(data, column_x, column_y, title)
            
            else:
                print ("Invalid option")

        elif option == "3":
            #Generate graphic bars
            print("\nSelect the columns for the lines graphic:")

            print("\n Columns for X axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_x = int(input("\Select the number of column for the X axis: ")) -1

            print("\n Columns for Y axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_y = int(input("\Select the number of column for the Y axis: ")) -1

            if 0 <= index_x < len(headers) and 0 <= index_y < len(headers):
                column_x = headers[index_x]
                column_y = headers[index_y]
                title = input("\nInsert a title for the graphic (optional): ")

                generate_lines_graphic(data, column_x, column_y, title)
            
            else:
                print ("Invalid option")  

        elif option == "4":
            #Exit
            print ("\n Thank you for using Data Analyzer")
            break

        else:
            print ("Invalid option")  

if __name__ == "__main__":
    main()