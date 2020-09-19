#-*- coding:utf-8 -*-


#client id  :   692220179903676417
#reveal token  :   NjkyMjIwMTc5OTAzNjc2NDE3.XnrXEg.aRMV8x4h72ji_Z0J4gCs7dYlYiI
#pip install: discord, asyncio, websockets, aiohttp
#requests, beautifulsoup4


import asyncio
import discord
import os

import datetime
import bs4
import requests
from discord.ext import commands

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}





session = requests.session()
lmsLogIn = 'https://course.pcu.ac.kr/login.php'
LOGIN_INFO={
    'username': '2061025',
    'password': 'zjarhd123!'
}
login = session.post(lmsLogIn,data=LOGIN_INFO)
print(login.status_code)
#loginhtml = login.text





req = requests.get('http://www.pcu.ac.kr/www/04_campus/campus_0401.html')
html = req.text
soup = bs4.BeautifulSoup(html,'html.parser',from_encoding='utf-8')
student = soup.find("h4")




client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('================')
   




# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await message.channel.send('커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
    elif message.content.startswith('학식'):
        await message.channel.send('학식')
    elif message.content.startswith('테스트'):
        await message.channel.send('testing')
        await message.channel.send(student)
        
        
    else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        await  message.channel.send("<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
