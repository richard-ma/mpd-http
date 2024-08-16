from fastapi import FastAPI
from client import Client
import json

client = Client("192.168.1.100")
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/player/next")
def player_next():
    client.next()
    return {"success": True}

@app.get("/player/prev")
def player_prev():
    client.prev()
    return {"success": True}

@app.get("/player/pause")
def player_pause():
    client.pause()
    return {"success": True}

@app.get("/player/play")
def player_play():
    client.play()
    return {"success": True}

@app.get("/player/stop")
def player_stop():
    client.stop()
    return {"success": True}

@app.get("/playlist/add/{uri}")
def playlist_add(uri: str):
    client.add(uri)
    return {"success": True}

@app.get("/playlist/playlist")
def playlist_playlist():
    return client.playlist()