NAME=docker-flask-nginx-mecab-w2v
DC_PATH=/usr/local/bin

run:
	${DC_PATH}/docker-compose build
	${DC_PATH}/docker-compose up -d

stop:
	docker stop ${NAME}_uwsgi_1 ${NAME}_nginx_1
	docker rm ${NAME}_uwsgi_1 ${NAME}_nginx_1
