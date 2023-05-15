import csv

# Read the first file and build a dictionary
with open('file1.csv', 'r') as f:
    reader = csv.reader(f)
    file1_dict = {row[1]: row[0] for row in reader}

# Open the second file and a new file for output
with open('file2.csv', 'r') as f, open('output.csv', 'w', newline='') as out:
    reader = csv.reader(f)
    writer = csv.writer(out)

    # For each line in the second file, write to the output file
    # only if the URL exists in the dictionary
    for row in reader:
        if row[1] in file1_dict:
            writer.writerow(row)
