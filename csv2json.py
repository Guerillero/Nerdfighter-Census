import csv

inputFile = open ("Countries.csv", 'r')
outputFile = open ("Countries.json", 'w')

fn = ['Country', 'survey takers']
csvData = csv.DictReader(inputFile, fieldnames=fn)

outputFile.write ("[")

foo = 0

for row in csvData:
  if foo > 1:
    outputFile.write(",\n")
  if row['Country'] != 'Country':
    outputFile.write("{\"" + fn[0] + "\":\"" + row['Country'] + "\",\"Survey_Takers\":" + row['survey takers'] + "}")
  foo += 1
  
outputFile.write ("]")
