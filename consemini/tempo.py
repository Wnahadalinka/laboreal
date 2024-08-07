import csv

# Open the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_output = csv.writer(file)

    # Define the data to write
    datachunk = ['John', 'Doe', 25]

    # Write the data to the CSV file
    csv_output.writerow(datachunk)
