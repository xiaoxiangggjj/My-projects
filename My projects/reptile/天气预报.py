import requests
import re
import datetime
from bs4 import BeautifulSoup

def weather():
    provide = "湖南省"
    city = "长沙市"
    url = f"https://www.msn.cn/zh-cn/weather/forecast/in-{provide},{city}?loc=eyJsIjoi5bKz6bqT5Yy6IiwiciI6Iua5luWNl%2BecgSIsInIyIjoi6ZW%2F5rKZ5biCIiwiYyI6IuS4reWNjuS6uuawkeWFseWSjOWbvSIsImkiOiJDTiIsImciOiJ6aC1jbiIsIngiOiIxMTIuOTE0IiwieSI6IjI4LjIyOSJ9&ocid=ansmsnweather&weadegreetype=C"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }
    content = requests.get(url, headers=header)
    soup = BeautifulSoup(content.text, "html.parser")
    all_tem = soup.findAll("div", attrs={"id": "OverviewCurrentTemperature"})
    all_wet = soup.findAll("div", attrs={"id": "CurrentDetailLineHumidityValue"})
    all_see = soup.findAll("div", attrs={"id": "CurrentDetailLineVisibilityValue"})
    weater, tem = re.findall(r'title="(.*?)"', str(all_tem[0]))
    wet = re.findall(r'<span>(.*?)</span>', str(all_wet[0]))[0]
    see = re.findall(r'<span>(.*?)</span>', str(all_see[0]))[0]
    current_time = str(datetime.datetime.now()).split(" ")[-1].split(":")
    timenow = str(int(current_time[0])) + "点" + str(int(current_time[1])) + "分"
    tem, see, wet = tem.split("\u200e")[0], see.split(" ")[0], wet.split("%")[0]
    weather = f"现在是{timenow}，天气{weater}，{tem}摄氏度，能见度{see}公里，湿度为百分之{wet}"
    print(weather)
    return weather

if __name__ == '__main__':
    weather()






