import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#postgresql:
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://ivan:G7RWX0YvaUrIl8VPQaLlMR0J6xyWS72s@dpg-ctulv0i3esus739e41c0-a.oregon-postgres.render.com/dbase_3k8p'
SQLALCHEMY_TRACK_MODIFICATIONS=False
