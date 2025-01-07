import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#postgresql:
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://ivan:0qf6sPLSbBxFphNjo3oJ6Z6gZJOh5n8y@dpg-ctuh4sl2ng1s739e5mgg-a.oregon-postgres.render.com/dbase_0wpt'
SQLALCHEMY_TRACK_MODIFICATIONS=False

