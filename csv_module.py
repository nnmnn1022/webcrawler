import csv

def write(data, path) :
    with open(path, 'w', encoding='utf-8-sig', newline='') as writeFile:
        try:
            csvWriter = csv.writer(writeFile)
            csvWriter.writerows(data)
        except Exception as e:
            print(e)

def read(path) :
    with open(path, 'r', encoding='utf-8-sig') as csvFile:
            csvReader = list(csv.reader(csvFile))

    return csvReader