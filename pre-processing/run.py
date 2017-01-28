from collections import defaultdict
import json
import re
from collections import Counter


def data1():
    
    data = open('input.json',encoding="utf8").read()
    theJSON = json.loads(data)

    for element in theJSON: 
        for element in element['songs']:
#          del element['lyrics']
           word = data3(element['lyrics'])
           element['mostCommomWord'] = word 
           print(word) 
        
    print(theJSON)

    with open("data1.json","w", encoding='utf-8') as jsonfile:
            json.dump(theJSON,jsonfile,ensure_ascii=False)
            


def data2():
    
    output = []
    
    data = open('input.json',encoding="utf8").read()
    theJSON = json.loads(data)
    
    #split by year objects
    for yearObject in theJSON:
            #for each year split by song object 
            for song in yearObject['songs']:
                #if the artist not exist in output array
                if not any(song['artist'] == output[index]['artist'] for index in range(len(output))): 
                    output.append({"artist" : song['artist'] , "songs" : [{"year" : yearObject['year'] , "songName" : song['songName'] , "lyrics" : song['lyrics']  }] })
                #if the artist already exist in output array we add song details to array
                else:
                    index = next(index for (index, d) in enumerate(output) if d["artist"] == song['artist'])
                    output[index]['songs'].append({"year" : yearObject['year'] , "songName" : song['songName'] ,"lyrics" : song['lyrics']})
                         
               
    print(output)
    
    for object in output:
        lenght = len(object['songs'])
        object['winAmount'] = lenght 

    print(output)
    
    with open("data2.json","w", encoding='utf-8') as jsonfile:
            json.dump(output,jsonfile,ensure_ascii=False)
    
    
# find the common word in each song    
def data3(lyrics):
    
#     #with open('lyrics.json',encoding="utf8") as f:
    
#     data = open('lyrics.json',encoding="utf8").read()
#     theJSON = json.loads(data)    
    
#     lyrics = theJSON['lyrics']
    newstr = lyrics.replace("-", "")

    
    z = Counter(newstr.split())
    print(z)
    
    #return the the most common word
    most_common,num_most_common = Counter(z).most_common(1)[0]
    print(most_common)
    print(num_most_common)
    return most_common    
    
data1()
data2()
