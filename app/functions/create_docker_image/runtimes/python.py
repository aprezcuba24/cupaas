template = """
FROM python:{VERSION}-slim

RUN pip3 install --upgrade pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE {PORT}

ENTRYPOINT [{ENTRYPOINT}]

"""


def python(version, docker_port, data):
    entrypoint = ",".join([f'"{item}"' for item in data["entrypoint"]])
    return template.format(
        VERSION=version,
        ENTRYPOINT=entrypoint,
        PORT=docker_port,
    )
