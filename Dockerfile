FROM python:3.7
ENV PYTHONBUFFERED 1

WORKDIR /usr/src/app

COPY requirements/* requirements/
RUN pip install --no-cache-dir -r requirements/docker.txt

COPY . .

RUN mv scripts/start.sh start.sh
RUN chmod a+x start.sh

EXPOSE 5000
CMD './start.sh'
