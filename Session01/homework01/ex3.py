import matplotlib

matplotlib.use("TkAgg")

from matplotlib import pyplot

from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

customers = db['customers']

wom = customers.find({"ref":"wom"}).count()
events = customers.find({"ref":"events"}).count()
ads = customers.find({"ref":"ads"}).count() 

print('ref wom: ', wom)
print('ref events: ', events)
print('ref ads: ', ads)


labels = ['wom','events','ads']
values = [wom,events,ads]

pyplot.pie(values,labels=labels)
pyplot.axis ("equal")
pyplot.show()