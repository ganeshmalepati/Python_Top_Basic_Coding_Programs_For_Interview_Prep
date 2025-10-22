FROM python

WORKDIR /app

COPY . /app

CMD [ "python", "Ten_Code.py" ]