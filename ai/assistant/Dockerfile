FROM python:3.10-slim
WORKDIR /app
COPY serve.py .
RUN pip install --no-cache-dir fastapi uvicorn pydantic
EXPOSE 8083
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8083"]
