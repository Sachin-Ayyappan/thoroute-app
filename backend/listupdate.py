import pymongo
from pyparsing import condition_as_parse_action
import os
import json

client = pymongo.MongoClient(
    "mongodb+srv://thoroute-app:thoroute%402022adi@thoroute.vd7gshc.mongodb.net/?retryWrites=true&w=majority")

db = client.users
buses = client.users.buses
busdata=list(buses.find({},{'_id':0,'qualityrating':0,'number':0}))
tempholder={
          "id": "TEMP01",
          "provider": "SELF",
          "mileage": "NaN",
          "condition": "Undefined",
          "distancedriven": "NaN",
          "age": "NaN",
          "capacity": "NaN"}

#json_object = json.dumps(dictionary, indent=4)

with open('./assets/dashboard/js/data.txt','w') as businfo:
    businfo.write('{"data":[')
    for i in busdata:
        businfo.write(json.dumps(i,indent=10)+',')
    businfo.seek(businfo.tell() - 1, os.SEEK_SET)
    businfo.write(']}')

    

print("Data fetched and written successfully")

"""
for files in os.listdir("./assets/dashboard/js/data.txt"):
  print(files)
"""