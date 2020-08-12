FROM python:slim-buster

RUN apt-get -y update && apt-get -y install git

RUN mkdir workspace
WORKDIR workspace

# TODO: Copy folder to docker instead for faser dev.
RUN git clone https://github.com/kdop/microservices.git

WORKDIR microservices/nameko-basic-http

# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# suppress pip updates warning
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR nameko_basic_http
CMD ["nameko", "run", "--config", "config.yaml", "helloworld"]
