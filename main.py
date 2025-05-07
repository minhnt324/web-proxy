from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/read")
async def read_url(url: str = Query(..., description="URL của trang web cần trích xuất")):
    try:
        content = await fetch_page_content(url)
        return JSONResponse(content={"text": content})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

async def fetch_page_content(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=60000, wait_until='networkidle')
        html = await page.content()
        await browser.close()

        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])