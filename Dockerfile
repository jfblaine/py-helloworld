FROM aio.home.io:5000/ntlsrepo/ubi/ubi7/python-36:1-63.1584463519

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["run.py"]
