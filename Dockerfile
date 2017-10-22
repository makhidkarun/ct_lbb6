FROM ubuntu:17.04
MAINTAINER Daniel Riti <dmriti@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Base install
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-virtualenv \
    nginx \
    gunicorn \
    supervisor \
    rsyslog\
    && rm -rf /var/lib/apt/lists/*

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