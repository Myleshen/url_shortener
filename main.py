from fastapi import FastAPI
from url_shortner.shortener import Shortener
from payloads_post.URLModel import URL

app = FastAPI()
shortener = Shortener()


@app.post("/create")
async def create_url(got_url: URL):
    url = got_url.url
    return {"response": f"Created URL is: {shortener.create_unique_url(url)}"}


@app.get("/list")
async def list_urls():
    return shortener.list_urls_in_db()


@app.get("/find")
async def get_short_url(q: str):
    return shortener.get_original_url(q)