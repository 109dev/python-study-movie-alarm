import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '1225880838:AAH5daALDex_7Zj_sYpAHxfiBKo1zSuRMpw')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200624&screencodes=&screenratingcode=&regioncode='

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=1058108324, text="[{}] IMAX 예매가 열렸습니다.".format(title))
        schde.pause()
    # else:
    #     bot.sendMessage(chat_id=1058108324, text="IMAX 예매가 아직 열리지 않았습니다.")

schde = BlockingScheduler()
schde.add_job(job_function, "interval", seconds=30)
schde.start()