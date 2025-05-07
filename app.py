from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

@app.get("/")
def read_thegioididong():
    url = "https://www.thegioididong.com/game-app/ransomware-la-gi-muc-do-nguy-hiem-va-cach-ngan-chan-1371507"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        page = context.new_page()
        try:
            page.goto(url, timeout=120000, wait_until="domcontentloaded")
            page.wait_for_selector(".trangchitiet", timeout=10000)
            content = page.query_selector(".trangchitiet")
            return {
                "url": url,
                "content": content.inner_text() if content else "Không tìm thấy nội dung"
            }
        except Exception as e:
            return {"error": str(e)}
        finally:
            browser.close()
