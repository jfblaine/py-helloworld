FROM aio.home.io:5000/ntlsrepo/openshift/python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
USER 1001
CMD python ./index.py
