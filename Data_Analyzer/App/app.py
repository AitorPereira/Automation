import os
import csv
import statistics
import matplotlib.pyplot as plt

def load_data_csv(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        tuple: (headers, data) where headers is a list of column names 
               and data is a list of dictionaries containing the rows.
    """

    try:
        # Verify that the file exists
        if not os.path.exists(file_path):
            print(f"Error: The file {file_path} does not exist.")
            return None, None  # Tuple

        # Initialize containers
        headers = []
        data = []

        # Open and read the CSV file
        with open(file_path, 'r', newline='', encoding='utf-8') as file_csv:
            reader = csv.reader(file_csv)

            # First row is the header
            headers = next(reader)

            # Process rows
            for row in reader:
                # Create a dictionary only if row length matches headers
                if len(row) == len(headers):
                    row_dict = {}
                    for i, value in enumerate(row):
                        try:
                            # Try converting to int
                            row_dict[headers[i]] = int(value)
                        except ValueError:
                            try:
                                # If not int, try converting to float
                                row_dict[headers[i]] = float(value)
                            except ValueError:
                                # Otherwise, keep as string
                                row_dict[headers[i]] = value
                    data.append(row_dict)

            print(f"{len(data)} rows loaded with {len(headers)} columns.")
            return headers, data

    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None, None  # Tuple

def display_data_summary(headers, data):
    """
    Display a summary of the loaded dataset.

    Args:
        headers (list): List of column names.
        data (list): List of dictionaries containing the dataset.
    """

    if not data:
        print("No data available to display.")
        return

    print("\n=== DATA SUMMARY ===")
    print(f"Rows: {len(data)}")
    print(f"Columns: {', '.join(headers)}")

    # Display the first 5 rows
    print("\nFirst 5 rows:")
    for i, row in enumerate(data[:5]):
        print(f"Row {i+1}: {row}")

def analyze_numerical_column(data, column):
    """
    Perform a statistical analysis of a numerical column.

    Args:
        data (list): List of dictionaries containing the dataset.
        column (str): Name of the column to analyze.
    
    Returns:
        dict: Dictionary with column statistics, or None if no numeric values are found.
    """

    # Extract values from the column, filtering only numeric values
    values = []
    for row in data:
        if column in row and isinstance(row[column], (int, float)):
            values.append(row[column])

    # Verify that numeric values exist
    if not values:
        print(f"No numeric values found in column '{column}'.")
        return None
    
    # Calculate statistics
    statistic = {
        'column': column,
        'total_values': len(values),
        'minimum': min(values),
        'maximum': max(values),
        'sum': sum(values),
        'average': sum(values) / len(values),
        'median': statistics.median(values),
        'standard_deviation': statistics.stdev(values) if len(values) > 1 else 0
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

def calculate_group_average(data, column_x, column_y):
    """
    Group the dataset by the values of column_x and calculate the average 
    of column_y for each group.

    Args:
        data (list): List of dictionaries containing the dataset.
        column_x (str): Name of the column to group by (X-axis).
        column_y (str): Name of the column to average (Y-axis).

    Returns:
        tuple: (values_x, averages_y), where:
            - values_x is a list of unique values from column_x.
            - averages_y is a list of averages of column_y for each group.
    """

    # Group data by X values and collect Y values
    groups_x = {}

    for row in data:
        if column_x in row and column_y in row and isinstance(row[column_y], (int, float)):
            value_x = str(row[column_x])
            value_y = row[column_y]

            if value_x not in groups_x:
                groups_x[value_x] = []

            groups_x[value_x].append(value_y)

    # Calculate averages per group
    values_x = []
    averages_y = []

    for value_x in sorted(
        groups_x.keys(),
        key=lambda v: float(v) if str(v).replace('.', '', 1).isdigit() else str(v)
    ):
        values_y = groups_x[value_x]
        if values_y:  # Verify that there are values
            values_x.append(value_x)
            averages_y.append(sum(values_y) / len(values_y))

    return values_x, averages_y

def generate_bars_graphic(data, column_x, column_y, title=None):
    """
    Generate a bar chart showing the average of Y values for each X value.

    Args:
        data (list): List of dictionaries with the dataset.
        column_x (str): Name of the column for the X axis.
        column_y (str): Name of the column for the Y axis.
        title (str, optional): Title of the chart. Defaults to None.

    Returns:
        bool: True if the chart was generated successfully, False otherwise.
    """

    try:
        values_x, averages_y = calculate_group_average(data, column_x, column_y)
        
        if len(values_x) < 2:
            print("Not enough data to generate the chart")
            return False

        # Create the chart
        plt.figure(figsize=(10, 6))
        plt.plot(values_x, averages_y, color='darkblue')

        # Add labels and title
        plt.xlabel(column_x)
        plt.ylabel(f"Average of {column_y}")
        plt.title(title or f"Average of {column_y} by {column_x}")

        # Rotate X-axis labels if there are many
        if len(values_x) > 5:
            plt.xticks(rotation=45, ha='right')

        # Adjust layout
        plt.tight_layout()

        # Display chart
        plt.show()

        return True

    except Exception as e:
        print(f"Error generating the chart: {e}")
        return False

def generate_lines_graphic(data, column_x, column_y, title=None):
    """
    Generate a line chart showing the average of Y values for each X value.

    Args:
        data (list): List of dictionaries with the dataset.
        column_x (str): Name of the column for the X axis.
        column_y (str): Name of the column for the Y axis.
        title (str, optional): Title of the chart. Defaults to None.

    Returns:
        bool: True if the chart was generated successfully, False otherwise.
    """

    try:
        values_x, averages_y = calculate_group_average(data, column_x, column_y)
        
        if len(values_x) < 2:
            print("Not enough data to generate the chart")
            return False
        
        # Create the chart
        plt.figure(figsize=(10, 6))
        plt.plot(values_x, averages_y, marker='o', linestyle='-', color='green')

        # Add labels and title
        plt.xlabel(column_x)
        plt.ylabel(f"Average of {column_y}")
        plt.title(title or f"Average of {column_y} by {column_x}")

        # Rotate X-axis labels if there are many
        if len(values_x) > 5:
            plt.xticks(rotation=45, ha='right')

        # Adjust layout
        plt.tight_layout()

        # Display chart
        plt.show()

        return True

    except Exception as e:
        print(f"Error generating the chart: {e}")
        return False

def main():
    """
    Main function to run the interactive Data Analyzer application.
    It allows the user to load a CSV file, analyze numeric columns,
    and generate bar or line charts from the data.
    """
    print("=== DATA ANALYZER ===")

    # Request CSV file path
    file_path = input("Insert the CSV file path to analyze: ")

    # Load data
    headers, data = load_data_csv(file_path)

    if not data:
        print("Failed to load data. Exiting program.")
        return

    # Display data summary
    display_data_summary(headers, data)

    while True:
        print("\nOptions:")
        print("1. Analyze numeric column")
        print("2. Generate bar chart")
        print("3. Generate line chart")
        print("4. Exit")

        option = input("\nSelect your option (1-4): ")
        
        if option == "1":
            # Analyze a numeric column
            print("\nAvailable columns:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_column = int(input("\nSelect the number of the column to analyze: ")) - 1
            if 0 <= index_column < len(headers):
                column = headers[index_column]
                statistic = analyze_numerical_column(data, column)
                if statistic:
                    display_statistic(statistic)
                else:
                    print("No numeric values found in the selected column.")
            
        elif option == "2":
            # Generate bar chart
            print("\nSelect columns for the bar chart:")

            print("\nColumns for X axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_x = int(input("\nSelect the column number for the X axis: ")) - 1

            print("\nColumns for Y axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_y = int(input("\nSelect the column number for the Y axis: ")) - 1

            if 0 <= index_x < len(headers) and 0 <= index_y < len(headers):
                column_x = headers[index_x]
                column_y = headers[index_y]
                title = input("\nInsert a title for the chart (optional): ")

                generate_bars_graphic(data, column_x, column_y, title)
            
            else:
                print("Invalid option.")

        elif option == "3":
            # Generate line chart
            print("\nSelect columns for the line chart:")

            print("\nColumns for X axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_x = int(input("\nSelect the column number for the X axis: ")) - 1

            print("\nColumns for Y axis:")
            for i, column in enumerate(headers, 1):
                print(f"{i}. {column}")

            index_y = int(input("\nSelect the column number for the Y axis: ")) - 1

            if 0 <= index_x < len(headers) and 0 <= index_y < len(headers):
                column_x = headers[index_x]
                column_y = headers[index_y]
                title = input("\nInsert a title for the chart (optional): ")

                generate_lines_graphic(data, column_x, column_y, title)
            
            else:
                print("Invalid option.")  

        elif option == "4":
            # Exit
            print("\nThank you for using Data Analyzer.")
            break

        else:
            print("Invalid option.")  

if __name__ == "__main__":
    main()

    
