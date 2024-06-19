FROM python:3.11-slim-bullseye

WORKDIR /www/fastapi/drvser/vue-fastapi-drv
ADD . .
COPY /deploy/entrypoint.sh .

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,id=core-apt \
    --mount=type=cache,target=/var/lib/apt,sharing=locked,id=core-apt \
    sed -i "s@http://.*.debian.org@http://mirrors.ustc.edu.cn@g" /etc/apt/sources.list \
    && rm -f /etc/apt/apt.conf.d/docker-clean \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev bash nginx vim curl procps net-tools

RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install aiomysql\
    && poetry config virtualenvs.create false \
    && poetry install

# COPY --from=web /www/fastapi/drvser/vue-fastapi-drv /www/fastapi/drvser/vue-fastapi-drv
ADD /deploy/web.conf /etc/nginx/sites-available/web.conf
RUN rm -f /etc/nginx/sites-enabled/default \ 
    && ln -s /etc/nginx/sites-available/web.conf /etc/nginx/sites-enabled/ 

ENV LANG=zh_CN.UTF-8

ENTRYPOINT [ "sh", "entrypoint.sh" ]