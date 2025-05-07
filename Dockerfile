# Dùng image chính thức của Playwright (đã có Chromium và headless hỗ trợ)
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && playwright install --with-deps

ENV PORT=8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
