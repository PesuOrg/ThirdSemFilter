import csv
import json

def parseCsv():
    people = {}
    with open('input.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if(row['SRN'] not in people):
                people[row['SRN']] = { 'Name': '', 'Email': row['Username']}
    return people

def parseJson():
    with open('people.json', 'r') as jsonFile:
        return json.load(jsonFile)

people = parseJson()

while True:
    print("Enter SRN, enter exit to end the program")
    srn = input()
    
    if(srn == 'exit'):
        break
    
    if(srn in people):
        print(people[srn])
    
    else:
        print("Please enter a valid usn")

