from . import csv_module, crawling
import pathlib, os
from datetime import datetime


saved_folder = pathlib.Path.cwd()
file_list = os.listdir(saved_folder)
setting = False

if 'setting.csv' not in file_list :
    myfolder = input('파일을 저장할 폴더 절대 경로를 입력하세요.\n')
    csv_module.write(myfolder, saved_folder)

data = input('크롤링이 필요한 파일을 넣어주세요.(.csv)\n')
