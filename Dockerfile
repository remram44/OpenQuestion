FROM python:3.10

ENV TINI_VERSION v0.18.0
RUN curl -Lo /tini https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini && \
    chmod +x /tini

RUN apt-get update && \
    apt-get install -yy openjdk-17-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONFAULTHANDLER=1

RUN mkdir -p /usr/src/app/home && \
    useradd -d /usr/src/app/home -s /usr/sbin/nologin -u 998 appuser && \
    chown appuser /usr/src/app/home
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt

RUN python -c "import anvil_app_server; anvil_app_server.find_or_download_app_server()"

COPY client_code client_code
COPY server_code server_code
COPY theme theme
COPY __init__.py .anvil_editor.yaml anvil.yaml .

RUN python -m compileall /usr/src/app

RUN mkdir .anvil-data && chown appuser .anvil-data
VOLUME /usr/src/app/.anvil-data

USER 998
ENTRYPOINT ["/tini", "--"]
CMD ["anvil-app-server", "--app", "."]
EXPOSE 3030
