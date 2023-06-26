from pymongo import MongoClient
from app.config import MONGO_URL, MONGO_DABASE


def get_client():
    client = MongoClient(MONGO_URL)
    database = client[MONGO_DABASE]
    return database, client
