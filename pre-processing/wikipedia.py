from bs4 import BeautifulSoup
import requests 
import urllib.request
import re
import json
import os


def getLyrics(songName,artist):
    print(artist)
    payload = {'q': songName}
   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               'Cookie' : 'uniqueId=681239d7-30a1-6afb-8bad-a3c2d22dceb0; HOAXFBK=55nnL68kPFr_6dHazhQG1cVFnTAWsLBKeBxSzFaDnfw9NxOl3m7O4awAxS_d-huPh5a; rbzid=ZVhBMnRGNmdTZmY2QU03b04ray9QZldBS1NWaHRqZXlaaGtQYnZYWkpoVFBUUDJRb0gvUU0vZnhYTy8vaGJjcHJKcnJLZ2FTTndYMklETWpRN21NcVNjcmR0b2tieGxCNTEyNXpWNE1uazROUUZDbVh6NUZEYmxEaUM5MzBiVmxNQXRjNFNEdU55OXlHcDFvYzgrSDUvU0I3S05Xc09sWnNCOW5ETmNNR0d5MlJUTEx2WVNvK2pHNDkyV3AxRXRzSk5QdHJ6a0h5NHdENnd5MjBIVUo0UT09QEBANEBAQC0xNDgxNDgxNDY4MA--; JSESSIONID=215146E223BA8ACD59F38EE7AE902E15; _gat_UA-3886828-10=1; _gat_UA-3886828-1=1; _gat=1; _gat_private=1; _gat_stop=1; _ga=GA1.3.1031322617.1485298438; _ga=GA1.4.1031322617.1485298438'
               
              }
    
    try:

        r = requests.get('http://shironet.mako.co.il/search?',params=payload,headers=headers)
        data = r.content
        data = data.decode('utf-8')

        soupSearchBySong = BeautifulSoup(data,'html.parser')
    #     print(soupSearchBySong.prettify())
    #     print("outside")

        for item in soupSearchBySong.find_all('a'):
    #         print("inside")
    #       remove space from artist name
    #         print(str(item.string).strip())
            if(str(item.string).strip() == artist):
    #             print(item.previous_sibling.previous_sibling.get('href'))

                urlData = 'http://shironet.mako.co.il'+item.previous_sibling.previous_sibling.get('href')
                print(urlData)
                return urlData
            
    except Exception: 
          pass
        

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def getWikiArtistPage(wikiUrl,songName,artist):
    
    type(wikiUrl)
    print(artist)
    print(wikiUrl)
#     getLyrics(songName,artist)
    

    webUrl = urllib.request.urlopen("https://he.wikipedia.org"+wikiUrl )
    data = webUrl.read()
    data = data.decode("utf-8")
    soup = BeautifulSoup(data,'html.parser')
#     print(soup.prettify())
    td_data = soup.find_all("a")
     
    categorySongs = []
    gender = ""
    
    for item in td_data:
#       print(item.next_element)
        if(item.next_element == "פופ"):
            print("פופ")
            categorySongs.append("פופ")
        if(item.next_element == "מוזיקה מזרחית"):
            print("מוזיקה מזרחית")
            categorySongs.append("מוזיקה מזרחית")
        if(item.next_element == "רוק"):
            print("רוק")
            categorySongs.append("רוק")
        if(item.next_element =="זמר עברי"):
            print("זמר עברי")
            categorySongs.append("זמר עברי")
        if(item.next_element =="רוק ישראלי"):
            print("רוק ישראלי")
            categorySongs.append("רוק ישראלי")
        if(item.next_element == "זמרת"):
            print("זמרת")
            gender = "זמרת"
        if(item.next_element =="זמר"):
            print("זמר")
            gender = "זמר"
        if(item.next_element == "להקת"):
            print("להקת")
            gender = "להקה"
            
    tbody = soup.find_all('img')[0].get('src')
    print("http:"+tbody)
    
    print(f7(categorySongs))
    if(len(categorySongs) == 0):
        categorySongs.append("זמר עברי")
    return gender , f7(categorySongs) , "http:"+tbody


# urlData_1980 = 'https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%22%D7%9D_-_%D7%94%27%D7%AA%D7%A9%D7%9E%22%D7%98)'
# urlData_1970 = 'https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%22%D7%9C_-_%D7%94%27%D7%AA%D7%A9%D7%9C%22%D7%98)'
# urlData_1990 ='https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%22%D7%9F_-_%D7%94%27%D7%AA%D7%A9%D7%A0%22%D7%98)'
# urlData_2000 = 'https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%22%D7%A1_-_%D7%94%27%D7%AA%D7%A9%D7%A1%22%D7%98)'
#urlData_2010 = 'https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%22%D7%A2_%D7%95%D7%90%D7%99%D7%9C%D7%9A)'
urlData = 'https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%A2%D7%93_%D7%94%D7%A4%D7%96%D7%9E%D7%95%D7%A0%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99_%D7%94%D7%A9%D7%A0%D7%AA%D7%99_(%D7%94%27%D7%AA%D7%A9%D7%9B%22%D7%92_-_%D7%94%27%D7%AA%D7%A9%D7%9B%22%D7%98)'
webUrl = urllib.request.urlopen(urlData)
data = webUrl.read()
data = data.decode("utf-8")

soup = BeautifulSoup(data,'html.parser')
# print(soup.prettify())

h3_data = soup.find_all("h3")

# get only the top 10 years from each decade
countYear = 0

# the list will contain decade year 
yearList = [];

# extrect the 10 year from each recent
for item in h3_data:
        print(item)
        if(countYear < 7 ):
            yearList.append(item.contents[0].text.split("-",1)[1])
            countYear = countYear + 1
       
    
    
getWikiArtistPageCount = 0  
yearListCount = 0
count = 1
liCount = 1
# check if the song name is empty
songNameValid = 0

lyricsUrl = ""

artistImg = ""
gender = ""
categorySongs = []

# get td from wiki page - the page conatin 2 td for each year 15 song for each td
td_data = soup.find_all("td" , { "valign" : "top" })
for item in td_data:
# json template
    output = {'songs' : []}
#   get two ul for each year we want only the first ul from each year
    if((count%2) != 0 and count):
#       print(item.find_all('ul')) 
        for ul in item.find_all('ul'): 
#           year for each list of top 10
            print(yearList[yearListCount])
            output['year'] = yearList[yearListCount]
#           get the top 10 songs
            for li in item.find_all('li'):
                if(liCount < 11):
                    try:
    #                   send to function artist page and artist name 
                        if(len(re.findall('"([^"]*)"', li.next_element)) > 0):
                           gender , categorySongs , artistImg  = getWikiArtistPage(li.next_element.next_element.get('href'),re.findall('"([^"]*)"', li.next_element)[0],li.next_element.next_element.text)
                           lyricsUrl =  getLyrics(str(re.findall('"([^"]*)"', li.next_element)[0]),li.next_element.next_element.text)
                           print(artistImg)
    #                   get position
                        print(li.next_element.split('. ')[0])
    #                   get song name
                        if(len(re.findall('"([^"]*)"', li.next_element)) > 0):
                            songNameValid = 1
                            print( re.findall('"([^"]*)"', li.next_element)[0])
    #                   get artist
                        print(li.next_element.next_element.text)
                        if(songNameValid == 1):
                            output['songs'].append({'songName' : re.findall('"([^"]*)"', li.next_element)[0] ,'position' : li.next_element.split('. ')[0] , 'artist' : li.next_element.next_element.text , 'gender' : gender , 'category' : categorySongs , 'image' : artistImg , "lyricsUrl" : lyricsUrl})
                            songNameValid = 0
                        else:
                             output['songs'].append({'position' : li.next_element.split('. ')[0] , 'artist' : li.next_element.next_element.text , 'gender' : gender , 'category' : categorySongs , 'image' : artistImg , "lyricsUrl" : lyricsUrl})
                        print("-----------------------------------------------------------------")
                        liCount = liCount + 1
                    except Exception: 
                        pass
            with open(os.path.join( "json" , str(yearListCount+1) + '.json') ,"w", encoding='utf-8') as jsonfile:
                json.dump(output,jsonfile,ensure_ascii=False)
            yearListCount = yearListCount + 1
    count = count + 1
    liCount = 1

    