
import redis

SECRET_KEY = "WINDAH_BASUDARA"

# Setup MONGODB
MONGO_CONNECTION_STRING = "mongodb+srv://672023165:321Billal.@kapita-selekta.xgg367i.mongodb.net/?retryWrites=true&w=majority&appName=kapita-selekta"
MONGO_DATABASE_NAME = "kapita"
MONGO_COLLECTION_PRODUCTS = "product"
MONGO_COLLECTION_USER = "users"

# Setup Redis
SESSION_TYPE = "redis"
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True
SESSION_REDIS = redis.Redis(host="localhost", port=6379, db=0)