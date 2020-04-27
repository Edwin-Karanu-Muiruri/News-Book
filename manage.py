from flask_script import Server,Manager
from app import create_app
from config import Config
app = create_app('DevConfig')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    '''
    Running Unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()