FROM python:slim-buster
RUN apt-get -y update && apt-get -y install git

# TODO: Make poetry install globally instead.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir workspace
WORKDIR workspace

# TODO: Copy folder to docker instead for faser dev.
RUN git clone https://github.com/kdop/microservices.git

WORKDIR microservices/nameko-basic-http
RUN pip install poetry
RUN poetry install

WORKDIR nameko_basic_http
CMD ["nameko", "run", "--config", "config.yaml", "helloworld"]
