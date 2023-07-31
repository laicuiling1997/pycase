#怎么发请求
import requests
# pip install lxml
from lxml import etree

#发给谁
url = "https://www.douluodalu.cc/book/douluodalu1/1.html"
a= 0
while a<3:
    #伪装自己
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    #发送请求
    resp = requests.get(url,headers=header)

    #设置编码
    resp.encoding ='utf-8'

    #响应信息
    print(resp.text)


    e = etree.HTML(resp.text)

    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    #下一页地址
    url = f'https://www.douluodalu.cc{e.xpath("//tr/td[2]/a/@href")[0]}'
    print(info)
    print(title)

    # 保存
    with open('斗罗大陆.txt','a+',encoding='utf-8') as f:
        f.write(title+'\n\n'+info+'\n\n')
        
    a+=1

    