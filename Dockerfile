FROM python:latest

ADD app.py .

RUN pip install fastapi "uvicorn[standard]" pydantic openai

CMD ["uvicorn", "app:app"]