FROM python:3.10

ENV TINI_VERSION v0.18.0
RUN curl -Lo /tini https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini && \
    chmod +x /tini

ENV PYTHONFAULTHANDLER=1

RUN mkdir -p /usr/src/app/home && \
    useradd -d /usr/src/app/home -s /usr/sbin/nologin -u 998 appuser && \
    chown appuser /usr/src/app/home
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt

COPY client_code client_code
COPY server_code server_code
COPY theme theme
COPY __init__.py .

RUN python -m compileall /usr/src/app

USER 998
ENTRYPOINT ["/tini", "--"]
CMD ["anvil-app-server", "--app", "."]
EXPOSE 3030
