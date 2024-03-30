from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
import time

def FansInfo_get(url,list_space,driver):
    #网页用js渲染，普通requests.get()请求无法获取网页源代码
    fans_list,name_list=[],[]
    # driver = webdriver.Firefox()
    for space in list_space:
        driver.get(url+space)
        time.sleep(1)
        soup=BeautifulSoup(driver.page_source,"html.parser")
        all_fans=soup.findAll("a",attrs={"class":"n-data n-fs"})
        # print(all_fans)
        name_info=soup.findAll("span",attrs={"id":"h-name"})
        ret_fan = r'title="(.*?)"'
        fans= re.findall(ret_fan,str(all_fans[0]))
        fans_list+=fans
        name=re.findall(r'<span id="h-name">(.*?)</span>',str(name_info[0]))
        name_list+=name
    print(fans_list)
    print(name_list)
    # driver.close()
    return fans_list,name_list

def info_writein(fans,names,time,uid):
    i,errer=0,0
    while True:
        try:
            fanssum=""
            fannumlist=fans[i].split(',')
            for fannum in fannumlist:
                fanssum+=fannum
            fanssum=FansChange(fanssum)
            with open(f'./up fans/5.21/uid{uid[i]}{names[i]}粉丝量.txt','a',encoding="utf-8") as f:
                f.write(names[i]+"\n粉丝量:"+fanssum+"\n更新于/"+str(time)+"\n\n")
        except Exception:
            errer += 1
            if i < len(uid):
                print(f"errer_code:{errer}/ErrorUid:{uid[i]}")
            else:
                break
        i+=1

def FansChange(fanssum):
    num,lst="",[]
    for i in fanssum:
        lst+=i
    if len(lst)>8:
        ge = lst[-4:]
        wan = lst[-8:-4]
        yi = lst[:-8]
        return ''.join(yi+['亿']+wan+['万']+ge)
    elif len(lst)>4:
        ge = lst[-4:]
        wan = lst[:-4]
        return ''.join(wan + ['万'] + ge)
    else:return ''.join(lst)

if __name__ == "__main__":
    url="https://space.bilibili.com/"
    list_space=["546195","517327498",#老番茄，罗翔说刑法
                "5970160","125526",#小潮院长，-LKs-
                "53456","19319172",#Warma，差评君，
                "90361813","8366990",#三十六贱笑，-欣小萌-
                "480804525","777536"]#阿-岳同学，LexBurner
    # list_space
    header={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
    }
    driver = webdriver.Firefox()
    while True:
        dr = time.time()
        current_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(dr))
        print(current_time)
        fans,names=FansInfo_get(url,list_space,driver)
        info_writein(fans,names,current_time,list_space)
        print("等待9分钟开始下一次爬取")
        time.sleep(60*9)
    driver.close()