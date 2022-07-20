import aiohttp
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

brain = "https://brain.com.ua/ukr/Procesor_INTEL_Core_i5_10400F_BX8070110400F-p688386.html"
telemart = "https://telemart.ua/ua/products/intel-core-i5-10400f-2943ghz-s1200-box/?gclid=CjwKCAjwrNmWBhA4EiwAHbjEQJsb65-GxmbV4Pi-4u_wnJs8mocp5N9tOQ3NnGbkOMOR-M8TBAhkghoCVB0QAvD_BwE"
compx = "https://compx.com.ua/ru/protsessor-intel-core-i5-10400f-bx8070110400f/"

async def brain_parser(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            price= soup.find('span', itemprop="price").get_text(strip=True)
            print(f"Brain price: {int(price)}")
            with sqlite3.connect('prices.db') as con:
                cur = con.cursor()
                sql_to_brain = """INSERT INTO prices(brain_price)
                    VALUES (?)"""
                cur.execute(sql_to_brain, [int(price), ])
                con.commit()

async def telemart_parser(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            price= soup.find('meta', itemprop="price")
            a=str(price).split('"')            
            print(f"Telemart price: {int(a[1])}")
            with sqlite3.connect('prices.db') as con:
                cur = con.cursor()
                sql_to_brain = """INSERT INTO prices(telemart_price)
                    VALUES (?)"""
                cur.execute(sql_to_brain, [int(a[1]), ])
                con.commit()


async def compx_parser(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            price= soup.find('meta', property="product:price:amount")
            a=str(price).split('"')
            print(f"Compx price: {int(a[1])}")
            with sqlite3.connect('prices.db') as con:
                cur = con.cursor()
                sql_to_brain = """INSERT INTO prices(compx_price)
                    VALUES (?)"""
                cur.execute(sql_to_brain, [int(a[1]), ])
                con.commit()            


async def futures(futures):
    await asyncio.gather(*futures)

list_futures = [brain_parser(brain), telemart_parser(telemart), compx_parser(compx)]

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(futures(list_futures))
    #asyncio.run([brain_parser(brain), telemart_parser(telemart), compx_parser(compx)])
