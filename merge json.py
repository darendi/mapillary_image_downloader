import json

# Read the contents of the first JSON file
with open('0_10.json') as file1:
    data1 = json.load(file1)

# Read the contents of the second JSON file
with open('350_360.json') as file2:
    data2 = json.load(file2)

# Merge the two dictionaries
merged_data = {**data1, **data2}

# Write the merged data into a new JSON file
with open('merged.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)