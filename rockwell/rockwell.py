import requests
from datetime import datetime
from fake_useragent import UserAgent
from pytz import timezone

ua = UserAgent()
HEADERS = {"User-Agent": ua.chrome}

def watch(url):
   return requests.get(url, headers=HEADERS).status_code


def judge(status_code):
   eastern = timezone("US/Eastern")
   now = datetime.now(eastern).strftime("%Y-%m-%d %H:%M")
   if status_code in (200, 301, 302):
      return {"status": "up", "timestamp": now}
   else:
      return {"status": "down", "timestamp": now}

