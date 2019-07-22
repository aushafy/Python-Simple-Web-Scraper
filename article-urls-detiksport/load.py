# load urls.json and unpack it
import json # import json library

filename = 'urls.json' # filename of json file

with open(filename) as url_files: # open json file
    json_load = json.load(url_files) # read all data with json.load

for url in json_load: # unpack from list to dict
    for k, v in url.items(): # unpack from dict
        print(k + ": " + v) # print those data from dict and make it keys and values