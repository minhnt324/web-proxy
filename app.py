import requests
from bs4 import BeautifulSoup

@app.get("/")
def get_static_html():
    url = "https://www.thegioididong.com/game-app/ransomware-la-gi-muc-do-nguy-hiem-va-cach-ngan-chan-1371507"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    content = soup.select_one(".trangchitiet")
    return {
        "url": url,
        "content": content.get_text(strip=True) if content else "Không tìm thấy nội dung"
    }
