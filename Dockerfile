FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 5050

CMD ["python", "app.py"]

#ENTRYPOINT ["python", "app.py"]