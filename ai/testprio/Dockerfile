FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./models ./models
COPY serve.py .
EXPOSE 8082
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8082"]
