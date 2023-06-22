from pymongo import MongoClient
from app.config import MONGO_URL


def startup_db_client():
    return MongoClient(MONGO_URL)


def shutdown_db_client(mongodb_client):
    mongodb_client.close()
