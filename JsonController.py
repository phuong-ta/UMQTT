import json

def readJson():
    # Opening JSON file
    f = open('data.json')
      
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
      
    # Closing file
    f.close()
    return json.dumps(data[0])