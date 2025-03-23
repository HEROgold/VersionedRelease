FROM python:3.13-alpine


ADD info.json /info.json
COPY versioning.py /versioning.py

ENTRYPOINT [ "executable" ]