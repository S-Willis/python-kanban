# Run with:
#    podman run -it --publish 8080:8080 --volume kanban.db:kanban.db <image-id>
#
ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN \
    apk add --no-cache \
        python3 \
        py3-waitress \
        py3-flask \
        py3-flask-sqlalchemy\
        \
        && python -m ensurepip
WORKDIR /python-kanban

COPY *.py .
COPY static ./static
EXPOSE 8080

COPY run.sh /
RUN chmod a+x /run.sh


CMD ["/run.sh"]
