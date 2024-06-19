import os
import typing

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
   
    VERSION: str = "0.1.2"
    APP_TITLE: str = "Vue FastAPI Admin"
    PROJECT_NAME: str = "Vue FastAPI Admin"
    APP_DESCRIPTION: str = "Description"

    CORS_ORIGINS: typing.List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: typing.List = ["*"]
    CORS_ALLOW_HEADERS: typing.List = ["*"]

    DEBUG: bool = True

    # MySQL 数据库连接设置
    DB_URL: str = "mysql+pymysql://drvser:fGiKfjcia3izTLEX@192.168.0.213:3306/drvser"

    # ... 其他设置保持不变 ...
    SECRET_KEY: str = "3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf"  # openssl rand -hex 32
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 day

    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # 更新TORTOISE_ORM配置以使用MySQL
    TORTOISE_ORM: dict = {
        "connections": {
            "default": {  # 将这里的键名从 "sqlite" 更改为 "default" 以匹配DB_CONNECTIONS中的键名
                "engine": "tortoise.backends.mysql",  # 使用MySQL引擎
                "credentials": {
                    "host": "192.168.0.213",  # 数据库主机
                    "port": 3306,  # 数据库端口
                    "user": "drvser",  # 数据库用户名
                    "password": "fGiKfjcia3izTLEX",  # 数据库密码
                    "database": "drvser",  # 数据库名
                },
            }
        },
        "apps": {
            "models": {
                "models": ["app.models"],  # 确保这里的路径正确指向您的模型文件
                "default_connection": "default",  # 使用上面定义的 "default" 连接
            },
        },
        "use_tz": False,
        "timezone": "Asia/Shanghai",  # 确保时区设置正确
    }



settings = Settings()
