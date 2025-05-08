# ベースイメージ
FROM python:3.10

# 作業ディレクトリを作成
WORKDIR /app

# 必要ファイルをコピー
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# Flaskを起動
# CMD ["python", "app.py"]

# Flask を Gunicorn 経由で起動
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]