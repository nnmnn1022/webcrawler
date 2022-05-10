import csv

def write(data, path) :
    if "'" or '"' in path :
        path = path.replace('"', '').replace("'", '')
    if path.startswith('& ') :
        path = path.replace('& ', '', 1)
    file_path = f'{path}/setting.csv'
    try :
        with open(file_path, 'w', encoding='utf-8-sig', newline='') as writeFile:
            try:
                csvWriter = csv.writer(writeFile)
                csvWriter.writerows(data)
            except Exception as e:
                print(e)
    except Exception as e :
        print(e)

def read(path) :
    if "'" or '"' in path :
        path = path.replace('"', '').replace("'", '')
    if path.startswith('& ') :
        path = path.replace('& ', '', 1)
    try :
        with open(path, 'r', encoding='utf-8-sig') as csvFile:
                csvReader = list(csv.reader(csvFile))
    except Exception as e :
        print(e)

    return csvReader