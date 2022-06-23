import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from openpyxl import Workbook

# refURL - https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
# refURL - https://book.coalastudy.com/data-crawling/week-3/stage-2

headers = {
    "Access-Control-Allow-Origin": "*",
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
}

url = input("url을 입력해주세요\n")

print("%s 의 html문서를 수집합니다.\n"%(url))
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, "html.parser")

data = soup.prettify()
# print(data)

fileName = urlparse(url).hostname

savePath = "./result/"
isDir = os.path.isdir(savePath)
if isDir == False:
    print("savePath가 일치하지 않습니다.")
    print("현재 경로에 data 디렉터리를 생성합니다.")
    os.mkdir("result")

# .txt로 저장하기
# print("파일을 %s.txt 형식으로 저장합니다.\n"%(fileName))
# with open("%s%s.txt"%(savePath, fileName), "w") as file:
#     file.write(soup.prettify())

# .xlsx로 저장하기
wb = Workbook()

ws1 = wb.active
ws1.title = "sheet1"
# ws1.cell(row=1, column=1, value=soup)
ws1 = soup

print("파일을 %s.xlsx 형식으로 저장합니다.\n"%(fileName))
wb.save("%s%s.xlsx"%(savePath, fileName))
