import bs4 as B
import requests
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}
title_list,grade_list,info_list=[],[],[]
for num in range(0,250,25):
    content=requests.get(f"https://movie.douban.com/top250?start={num}&filter=",headers=header)
    soup=B.BeautifulSoup(content.text,"html.parser")
    all_titles=soup.findAll("span",attrs={"class":"title"})
    all_grade=soup.findAll("span",attrs={"class":"rating_num"})
    all_infos=soup.findAll("p",attrs={"class":""})
    for intro in all_infos:
        with open("change.txt","w",encoding="utf-8") as f:
            f.write(str(intro))
        with open("change.txt","r",encoding="utf-8") as f:
            for i in range(3):
                strrr=f.readline()
        i,item=0,0
        years,country,mtype="","",""
        for m in strrr:
            if m=="/":
                item+=1
            elif item==0:
                if m!=" ":
                    years+=m
            elif item==1:
                if m!="\t":
                    country+=m
                else:country+=","
            elif item==2:
                if m=="\n":
                    break
                if m!="\t":
                    mtype+=m
                else:mtype += ","
        info_list+=["年份："+years+"/国家："+country+"/类型："+mtype]
    for title in all_titles:
        cont=title.string
        if "/" not in cont:
            title_list+=[title.string]
    for grade in all_grade:
        grade_list += [grade.string]
i=0
f=open("豆瓣电影top250名单.txt","w",encoding="utf-8")
while True:
    try:
        line=str(i+1)+"."+title_list[i] + "\n评分：" + grade_list[i] + "\n信息（" +info_list[i]+"）\n"
        print(line)
        f.write(line+"\n")
    except:
        print("//电影展示完毕//")
        break
    i+=1
