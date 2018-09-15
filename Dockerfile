FROM python:3.6-alpine

RUN adduser -D microblog
WORKDIR /home/microblog

COPY Pipfile Pipfile
COPY app app
COPY migrations migrations
COPY microblog.py boot.sh ./

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./ \
    && chmod +x boot.sh \
    && dos2unix boot.sh \
    && pip install pipenv 

USER microblog
RUN pipenv install
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]