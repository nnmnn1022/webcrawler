from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
#chrome to stay open
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-gpu-blocklist')
driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=chrome_options)

# 사이즈조절
driver.set_window_size(1400, 1000)  # (가로, 세로)
driver.get('https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Pages/MyPage/MyPageMain.aspx') # 페이지 이동

# driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'SMemberID')
userId.send_keys('') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'SMemberPassword')
userPwd.send_keys('') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)

# 예매 페이지 접속
try:
    driver.get('http://ticket.yes24.com/Perf/42802')

# driver.get('http://ticket.yes24.com/Special/' + '42804')
except Exception as e :
    print(e)

# 예매하기 버튼 클릭
driver.find_element(By.XPATH, "//div[@class='rn-05']/a[@class='rn-bb03']").click()

# # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

# # 예매안내가 팝업이 뜨면 닫기. ( ticketingInfo_check : True, False )
# ticketingInfo_check = self.check_exists_by_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']")
# if ticketingInfo_check:
#     driver.find_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']").click()

# 날짜선택
calHead = driver.find_elements(By.XPATH, "//div[@class='step01_date']/div[@class='calendar']/span")
year_month = calHead[1].find_elements(By.XPATH, "//em")
year = year_month[0].text  # 년
month = year_month[1].text  # 월

yearC = wantYear - int(year)	# wantYear : 예매 원하는 년
monthC = wantMonth - int(month)	# wantMonth : 예매 원하는 월

s = yearC * 12 + monthC
i = 0
# 월 이동
if s > 0:
    while i < s:
        calHead[2].click()
        i = i + 1
        calHead = driver.find_elements(By.XPATH, "//div[@class='calHead']/div[@class='month']/span")
elif s < 0:
    while i < s:
        calHead[0].click()
        i = i - 1
        calHead = driver.find_elements(By.XPATH, "//div[@class='calHead']/div[@class='month']/span")

# 선택 가능한 날짜 모두 불러오기
CellPlayDate = driver.find_elements(By.NAME, "CellPlayDate")

# 일 선택
for cell in CellPlayDate:
    if cell.text == wantDate:	# wantDate : 예매 원하는 일
        cell.click()
        break

while True :
    pass