from pymongo import MongoClient

client = MongoClient()
db = client.dog_location_db

def insert_dog_lost(dog):
  dogs = db.dogs_lost
  post = dogs.insert_one(dog)
  if post: 
    return True
  else: 
    return False

def insert_dog_found(dog):
  dogs = db.dogs_found
  post = dogs.insert_one(dog)
  if post:
    return True
  else: 
    return False

