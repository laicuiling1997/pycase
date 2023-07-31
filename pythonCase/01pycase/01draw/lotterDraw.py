# 让我们的电脑支持服务访问
# 需要一个web框架
# pip install Flask

from flask import Flask,render_template
from random import randint

app = Flask(__name__,template_folder='templates')   
print(app,'----')   #<Flask 'lotterDraw'>

heros = [
    '战争之王',
    '玛西亚之力',
    '沙漠死神',
    '金属大师',
    '野兽之灵',
    '迷失之牙',
    '机械公敌',
    '狂战士',
    '海洋之灾',
    '蛮族之王',
    '虚空恐惧',
    '诡术妖姬',
    '不祥之刃'
]

# print(len(heros),'------')

# 服务器地址：http://127.0.0.1:5000
# 进入index页面：http://127.0.0.1:5000/index
@app.route('/index')
def index():
    return render_template('index.html',heros= heros)


@app.route('/choujiang')
def choujiang():
    random_hero = randint(0,len(heros)-1)
    return render_template('index.html',heros=heros,h=heros[random_hero])

#不用每次改代码后重启终端
app.run(debug=True)