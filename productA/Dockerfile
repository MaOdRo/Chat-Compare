FROM rasa/rasa:3.6.0-full
WORKDIR '/app'
COPY . /app
COPY ./data /app/data
RUN  rasa train --domain domain.yml --data data --out models
VOLUME /app
VOLUME /app/data
VOLUME /app/models
EXPOSE 5005 
CMD ["run","-m","/app/models","--enable-api","--cors","*","--port","5005","--debug"]