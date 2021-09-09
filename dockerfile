FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["GuessGame.py"]
ENTRYPOINT ["python3"]
