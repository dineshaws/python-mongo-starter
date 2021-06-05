import os
import sys

class BaseConfig():
    ENV = ''

    def __init__(self, env) -> None:
        self.ENV = env

class DevelopmentConfig(BaseConfig):
    DB_URI = 'mongodb://localhost:27017'
    DB_NAME = 'pythonStarterDev'

class StagingConfig(BaseConfig):
    DB_URI = 'mongodb://localhost:28000'
    DB_NAME = 'pythonStarterStage'

class ProductionConfig(BaseConfig):
    DB_URI = 'mongodb://localhost:28000'
    DB_NAME = 'pythonStarterProd'


class ConfigFactory():

    def create(self):
        try: 
            ENV = os.environ.get('ENV')
        except KeyError:
            print('ENV KEYERROR')
            sys.exit(1)
        
        if ENV == None:
            print('Please set the environment variable: ENV')
            sys.exit(1)

        print('\n\n ENV-------',ENV)
        if ENV not in ['development','staging','production']:
            print("The ENV environment variable must be development, staging or production")
            sys.exit(1)
        
        if ENV == 'production':
            return ProductionConfig(ENV)
        elif ENV == 'staging':
            return StagingConfig(ENV)
        else:
            return DevelopmentConfig(ENV)