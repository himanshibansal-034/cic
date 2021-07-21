FROM python

WORKDIR /var/www/

ENV REDIRECT_TO https://vmothra.fun

COPY . /var/www/

RUN pip install -r /var/www/requirements.txt

CMD gunicorn --config gunicorn_config.py --worker-tmp-dir /dev/shm app:app
