from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

@app.get("/")
def read_thegioididong():
    url = "https://www.thegioididong.com/game-app/ransomware-la-gi-muc-do-nguy-hiem-va-cach-ngan-chan-1371507"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector(".trangchitiet", timeout=10000)
        content = page.query_selector(".trangchitiet")
        browser.close()
        return {
            "url": url,
            "content": content.inner_text() if content else "Không tìm thấy nội dung"
        }
