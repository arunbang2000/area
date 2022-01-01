FROM alpine:latest
RUN apk update
RUN apk add python3
RUN apk add py-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]