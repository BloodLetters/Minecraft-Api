import re
import json
import asyncio

from mcstatus import JavaServer

def config():
    js = open("config.json")
    rd =  json.load(js)
    return rd

def color(text):
    pattern = re.compile(r'\$\w')
    clean = re.sub(pattern, '', text)
    return clean

async def server(server_address):
    try:
        server = JavaServer.lookup(server_address)
        status = await server.async_status()
        return status
    except Exception as e:
        return str(e)

async def query():
    server_address = config()['ip'] + ":" + str(config()['port'])  # Ganti dengan alamat server Minecraft yang sesuai
    status = await server(server_address)
    return status