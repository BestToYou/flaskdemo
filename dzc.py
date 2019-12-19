

from flask_script import Shell


from app import create_app,db
app =create_app()
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

def make():
	return dict(app=app, db=db)

migrate = Migrate(app,db)


manager = Manager(app)
manager.add_command('shell', Shell(make_context=make))
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
	manager.run()

