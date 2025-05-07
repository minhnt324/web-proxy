from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def get_static_html():
    url = "https://www.thegioididong.com/game-app/ransomware-la-gi-muc-do-nguy-hiem-va-cach-ngan-chan-1371507"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()  # Báo lỗi nếu HTTP trả về lỗi (4xx, 5xx)

        soup = BeautifulSoup(res.text, "html.parser")
        content = soup.select_one(".trangchitiet")

        return {
            "url": url,
            "content": content.get_text(strip=True) if content else "Không tìm thấy nội dung"
        }

    except Exception as e:
        return {"error": str(e)}
