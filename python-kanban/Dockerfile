# Run with:
#    podman run -it --publish 8080:8080 --volume kanban.db:kanban.db <image-id>
#
ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN \
    apk add python3 python3-waitress python3-flask python3-flask-sqlalchemy
WORKDIR /python-kanban

COPY *.py .
COPY static ./static
EXPOSE 8080

COPY run.sh /
RUN chmod a+x /run.sh

# CMD [ "/run.sh" ]

CMD waitress-serve --call 'main:create_app'
