from aiohttp import web
import aiohttp_jinja2
import jinja2
from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect
from models import Price
from sqlalchemy.orm import sessionmaker
   
engine = create_engine('sqlite:///prices.db', connect_args={'check_same_thread': False})  
DBSession = sessionmaker(bind=engine)
session = DBSession()



@aiohttp_jinja2.template('index.html')
async def handle(request):
    prices = session.query(Price).all()
    #return web.Response(text=str(price.id))
    return {"prices": prices}

app = web.Application()
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader(str('templates')))

app.add_routes([web.get('/', handle)])
web.run_app(app, host='localhost')


