from app import create_app
from flask_script import Manager, Server
'''
If connecting to a database make sure to initialize
'''
# from app import create_app, db (add db to line 1)
# from app.models import User
# from flask_migrate import Migrate, MigrateCommand

# creating app instance
# TODO(S) 
'''DEVELOPMENT'''
app = create_app('development')
'''PRODUCTION'''
# app = create_app('production')
'''TESTING'''
# app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)


# IF HOOKING TO A DATABASE
# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app)
    # return dict(app=app, db=db, '''User=User''' )


if __name__ == '__main__':
    manager.run()
