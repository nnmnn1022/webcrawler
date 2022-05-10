import csv_module, crawling
import pathlib, os
from datetime import datetime
import pandas as pd

# 설정 파일이 있는지 확인
saved_folder = str(pathlib.Path.cwd())
file_list = os.listdir(saved_folder)
myfolder = ''

# 설정 파일이 없으면 설정 시킴
if 'setting.csv' not in file_list :
    while myfolder == '' :
        myfolder = [[input('파일을 저장할 폴더 절대 경로를 입력하세요.\n')]]
    csv_module.write(myfolder, saved_folder)

# file = input('크롤링이 필요한 파일을 넣어주세요.(.csv)\n')
file = "D:\\!Project\\Umoo\\umoo\\Wemade\\1_Work\\0504_0517_REGULAR\\0509_xlsx\\[BG_Mir4] Mini Glossary - 0517 update.csv"
if "'" or '"' in file :
    file = file.replace('"', '').replace("'", '')
if file.startswith('& ') :
        file = file.replace('& ', '', 1)

data =[]
word_list = pd.read_csv(file, header=0)
# col_num = int(input('몇 번째 열을 불러올까요?\n'))
col_num = 1
col_info = word_list.columns[col_num - 1]
# pandas dataframe 객체 - dataframe[컬럼] 열 조회 / dataframe.ix[인덱스] 행 조회
for word in word_list[col_info] :
    data.append(word)
    data.extend(crawling.run(word))

# 오늘 날짜 반환
date = datetime.today().strftime('%m%d')

# 아까 myfolder를 만들었으면 그걸 쓰고, 아니면 setting 파일을 찾아서 myfolder 위치 반환

if myfolder == '' :
    setting_file = csv_module.read(f'{saved_folder}/setting.csv')
    file_path = f'{setting_file[0][0]}\\{date}_크롤링.txt'
else :
    file_path = f'{myfolder}/{date}_크롤링.txt'

with open(file_path, 'w', encoding='utf-8-sig') as writeFile:
    for d in data :
        if d is not None :
            writeFile.write(d + '\n')
