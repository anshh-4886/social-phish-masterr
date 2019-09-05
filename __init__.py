import os

from flask import Flask, current_app
import click

from .core.view import head
from .core.cleanFake import cleanFake
from .core.dbsf import init_db_command
from .core.config import DATABASE

head()
cleanFake()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping({
        'SEND_FILE_MAX_AGE_DEFAULT': 0,
        'SECRET_KEY': os.urandom(16),
        'DATABASE': os.path.join(app.instance_path, DATABASE),
        }
    )
    # cria diretorio instance ex: mkdir ../instance
    # exist_ok - não levanta uma exceção caso o diretório já exista
    os.makedirs(app.instance_path, exist_ok=True)
    # adicionar comando init_db_command ex: flask init-db
    app.cli.add_command(init_db_command)

    return app