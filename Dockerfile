FROM alpine:3.5

# Base install
RUN apk update && apk add --no-cache \
    python \
    py-pip \
    nginx \
    supervisor \
    rsyslog

# Setup gunicorn
RUN pip install gunicorn

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
# COPY requirements.txt /deploy/app/requirements.txt
COPY requirements.txt manage.py config.py star.sqlite /deploy/
# COPY config.py /deploy
# COPY star.sqlite /deploy
# RUN pip install -r /deploy/app/requirements.txt
RUN pip install -r /deploy/requirements.txt


# Setup rsyslogd
COPY docker/rsyslog.conf /etc/rsyslog.conf

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY docker/flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
COPY docker/nginx.conf /etc/nginx/

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Start processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]