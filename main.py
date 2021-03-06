from fastapi import FastAPI
from url_shortner.shortener import Shortener
from payloads_post.URLModel import URL
from starlette.responses import RedirectResponse
import uvicorn

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
    url = shortener.get_original_url(q)
    return RedirectResponse(url=url)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)