import csv

# Read the first file and build a dictionary
with open('file1.csv', 'r') as f:
    reader = csv.reader(f)
    file1_dict = {row[1]: row[0] for row in reader}

# Read the second file and build a set of URLs
with open('file2.csv', 'r') as f:
    reader = csv.reader(f)
    file2_urls = set(row[1] for row in reader)

# Open a new file for output
with open('output.csv', 'w', newline='') as out:
    writer = csv.writer(out)

    # For each URL in the dictionary, write to the output file
    # only if the URL exists in the set
    for url, id in file1_dict.items():
        if url in file2_urls:
            writer.writerow([id, url])
