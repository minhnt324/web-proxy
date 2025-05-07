# Sử dụng image chính thức từ Microsoft Playwright
FROM mcr.microsoft.com/playwright/python:latest

# Tạo thư mục làm việc
WORKDIR /app

# Copy toàn bộ mã nguồn vào container
COPY . .

# Cài đặt Python dependencies và trình duyệt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && playwright install --with-deps

# Railway sẽ set PORT động nên cần ENV
ENV PORT=8000

# Chạy FastAPI bằng Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
