FROM python:3.10.8-alpine3.16

WORKDIR /app/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip install -U 'pip>=8' && \
    pip install --no-cache-dir 'kent==1.0.0'

USER guest

ENTRYPOINT ["/usr/local/bin/kent-server"]
CMD ["run"]
