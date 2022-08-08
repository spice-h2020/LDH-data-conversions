import json

inputFilename = '../data/original_data.json'
outputFilename = '../output/individual_docs.json'

masterArray = []

# Load original source data
jsonInputFile = open(inputFilename)
inputData = json.load(jsonInputFile)

# create an array to store all the individual objects in
newArray = []

# For each element in the original data, add it to the new array as a separate object
for key in inputData.keys():
    # exclude items that start with an underscore - these are the object attributes that were automatically
    # added by the LDH in your original 'PUSH', eg '_id', 'timestamp' etc.
    # (see at the end of the original_data.json file)
    if key[:1] != "_":
        newArray.append(inputData[key])

# write new data structure out to a new JSON file
with open(outputFilename, 'w', encoding='utf-8') as f:
    json.dump(newArray, f, ensure_ascii=False, indent=4)



