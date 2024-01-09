# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# # 크롬 드라이버 자동 업데이트을 위한 모듈
# from webdriver_manager.chrome import ChromeDriverManager
#
# # 크롬 드라이버 최신 버전 설정
# service = Service(executable_path=ChromeDriverManager().install())

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)