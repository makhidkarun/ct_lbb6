FROM alpine:3.5

# Base install
RUN apk update && apk add --no-cache \
    python \
    py-pip \
    nginx \
    supervisor \
    rsyslog

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
COPY requirements.txt manage.py config.py star.sqlite /deploy/
RUN pip install -r /deploy/requirements.txt


# Setup rsyslogd
COPY docker/rsyslog.conf /etc/rsyslog.conf

# Setup nginx
COPY docker/flask.conf /etc/nginx/conf.d/default.conf
COPY docker/nginx.conf /etc/nginx/

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY docker/supervisord.conf /etc/supervisor/supervisord.conf

# Start processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]