import os



# MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "")
CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 1,
    "CACHE_REDIS_URL": "redis://redis:6379/1",
}
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SECRET_KEY = "thisISaSECRET_1234"


# Database config
DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PROTOCOL = "postgresql+psycopg2"
DB_NAME = "superset"
SQLALCHEMY_DATABASE_URI = (
    f"{DB_PROTOCOL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)


# class CeleryConfig(object):
#     BROKER_URL = "redis://redis:6379/0"
#     CELERY_IMPORTS = ("superset.sql_lab",)
#     CELERY_RESULT_BACKEND = "redis://redis:6379/0"
#     CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}


# CELERY_CONFIG = CeleryConfig
# RESULTS_BACKEND = RedisCache(host="redis", port=6379, key_prefix="superset_results")





# Superset specific config
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# SQLALCHEMY_DATABASE_URI = 'sqlite:///superset.db'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''