import os

try:
    import secrets
    SECRET_KEY = secrets.secret_key
    GOOGLE_CLIENT_ID = secrets.google_client_id
    GOOGLE_CLIENT_SECRET = secrets.google_client_secret
except:
    SECRET_KEY = os.environ['SECRET_KEY']
    GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']

DB = os.environ['DATABASE_URL']
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
