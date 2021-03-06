#!/usr/bin/env python
from  app import create_app,db
from app.models import User
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')
manage = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User)

manage.add_command("shell",Shell(make_context=make_shell_context))
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()