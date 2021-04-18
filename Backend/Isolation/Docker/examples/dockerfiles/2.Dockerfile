FROM python:3.7.2-alpine3.8
LABEL maintainer="mkone112@gmail.com"
# Install requirements
RUN apk add --update git
WORKDIR /usr/src/my_app_directory
COPY . .
# Set default value for variable
ARG my_var=my_default_value
# Настраиваем команду для запуска во время выполнения
ENTRYPOINT ["python", "./app/my_script.py", "my_var"]
EXPOSE 8000
# создаем том для хранения данных
VOLUME /my_volume