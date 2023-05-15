import csv

# Read the first file and build a dictionary
with open('file1.csv', 'r') as f:
    reader = csv.reader(f)
    file1_dict = {row[1]: row[0] for row in reader}

# Open the second file and a new file for output
with open('file2.csv', 'r') as f, open('output.csv', 'w', newline='') as out:
    reader = csv.reader(f)
    writer = csv.writer(out)

    # For each URL in the second file, write to the output file
    # the ID from the first file and the URL, favicon_hash, and favicon_path
    for row in reader:
        url = row[0]
        favicon_hash = row[1]
        favicon_path = row[2]
        if url in file1_dict:
            writer.writerow([file1_dict[url], url, favicon_hash, favicon_path])
