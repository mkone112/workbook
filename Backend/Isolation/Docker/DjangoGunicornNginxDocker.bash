можно запускать PostgreSQL локально используя инструмент Postgres.app,или Docker

Docker
№ может содержать
	зависимости
	бд
	службы кеширования
	etc
бля докер контейнер делает все что я пытался сделать в шаблоне

# pacman -Syu
# pacman -Su
# pacman -Sy docker
# pip install docker-compose
# systemctl start docker.service
# systemctl enable docker.service
# docker version
#число запущенных контейнеров
	# docker info
#run without root
# usermod -aG docker $USER
$ reboot
# поиск образа docker
	docker search nginx
docker pull hello-world
docker run hello-world
docker container ls
#all docker images
docker images
#cpu/mem
docker stats
docker network ls

docker-compose build
docker-compose up -d
docker-compose logs -f