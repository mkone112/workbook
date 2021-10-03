#python поверх linux
FROM python:3.7.2-alpine3.8
LABEL maintainer="mkone112@gmail.com"
ENV ADMIN="admin"
RUN apk update && apk upgrade && apk add bash
COPY . ./app
ADD https://raw.githubusercontent.com/discdiver/pachy-vid/master/sample_vids/vid1.mp4 \
/my_app_directory
RUN ["mkdir", "/a_directory"]
CMD ["python", "./my_script.py"]