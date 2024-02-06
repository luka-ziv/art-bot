FROM python:latest

ADD ./src .

RUN pip install fastapi "uvicorn[standard]" pydantic openai

CMD ["uvicorn", "app:app"]