import csv

def read_csv_as_tuples(file_path):
    data_tuples = []
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            if row:  # Check if row is not empty
                data_tuples.append(row[0])  # Convert list to tuple and add to list
    
    return data_tuples 