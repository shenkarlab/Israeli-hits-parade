from collections import defaultdict
import json
import re
from collections import Counter
from bs4 import BeautifulSoup
import requests 
import urllib.request



# find the common word in each song    
def commonWord(lyrics):
    
    newstr = lyrics.replace("-", "")
    z = Counter(newstr.split())
    #return the the most common word
    most_common,num_most_common = Counter(z).most_common(1)[0]
    return most_common  



def getLyrics(url):
    
        print(url)
        headers = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                   'Cookie' : 'uniqueId=681239d7-30a1-6afb-8bad-a3c2d22dceb0; _gat=1; _gat_private=1; _gat_UA-3886828-10=1; _gat_UA-3886828-1=1; hjIWCVYbBd=cnFpJw"jp"s7XdHazhQG1cVFnTAWsLBKeBxSzFaDnn2_PNOl8SBO4awAxS_d-huPh5a; _gat_stop=1; rbzid=SHhpSnVEVWllSU1DSmFrU2MxbTBsTjhpa0xuWTB5RjJmbjhZeEJaaHN4dDhMZ200QWZtYWU1SHY3cG1tbXVJWWIvNkQyTXBjOHZabklOK2U3MVpQYTFUMUEzRmtla2ZhWGY5RGVla1dROXJlcTN6QnVpejJxWU41Ty92V0g1dmY3dnA0eUc3OE8vaWl0QzJyN1lEQWlxYXovQXE1QzBsa2ZRRndqeEpXU3g1VGtqVzc4eHNYa2RMN2ZwM0h6dnQ5M2FFUDY0azFyeVFsTGp2ZlhPLzRydz09QEBAMUBAQC0xNDgxNDgxNDY4MA--; JSESSIONID=12DB9514D71FC41F62B6139F476688E6; _ga=GA1.3.1031322617.1485298438; _ga=GA1.4.1031322617.1485298438'
                  }
        try:
            r = requests.get(url,headers=headers)
            data = r.content
            data = data.decode('utf-8')
#             print(data)

            soupLyrics = BeautifulSoup(data,'html.parser')
#             print(soupLyrics.prettify())
            
            img = soupLyrics.find('td' ,{"width":"162"}).next_element.next_element.get('src')
            print(img)
                
    
            span = soupLyrics.find_all('span', class_="artist_lyrics_text")
            
            lyricsText = span[0].text.replace("\r\n", " ").replace("\n", "")
            wordsAmount = len(span[0].text.replace("\r\n", " ").replace("\n", "").split())
            
            lyricsHtml = ""
            for item in span[0].contents:
                lyricsHtml = lyricsHtml + str(item)
            lyricsHtml.replace("\r\n", "")
                
            print(lyricsText)
            print(lyricsHtml)
            print(wordsAmount)
            
            commonWordInLyrics = commonWord(lyricsText)
            
            print(commonWordInLyrics)
            
            subject = []
            
            love = ['אהובתי','אהוב','אהבה','לאהוב','אהב']
            family = ['בן','ילד','משפחה','בית','אבא','אמא']
            country = ['מדינה','אדמה','רחוב','ירושלים','ישראל','מולדת','עיר']
            optimic = ['שמש','כחול','אור','שמחה','שמש']
            dance = ['רוקד','קצב','מקצב','רקד','לרקוד']
            pain = ['סדק','לבכות','בודד','רע','נפרדנו','כואב','כאב','עצוב']
            
            for loveWord in love:
                if loveWord in lyricsText:
                    print(loveWord)
                    if "אהבה" not in subject:
                        subject.append("אהבה")
            
            for familyWord in family:
                if familyWord in lyricsText:
                    print(familyWord)
                    if "משפחה" not in subject:
                        subject.append("משפחה")
                        
            for countryWord in country:
                if countryWord in lyricsText:
                    print(countryWord)
                    if "מולדת" not in subject:
                        subject.append("מולדת")
                        
            for optimicWord in optimic:
                if optimicWord in lyricsText:
                    print(optimicWord)
                    if "אופטימיות" not in subject:
                        subject.append("אופטימיות")
                        
            for danceWord in dance:
                if danceWord in lyricsText:
                    print(danceWord)
                    if "ריקודים" not in subject:
                        subject.append("ריקודים")
                        
            for painWord in pain:
                if painWord in lyricsText:
                    print(painWord)
                    if "כאב" not in subject:
                        subject.append("כאב")
            
                        
            print(subject)
            
            
            
            return lyricsText,lyricsHtml,wordsAmount,commonWordInLyrics,img,subject
            
        except Exception: 
              pass
        
listIndex = ['1','2','3','4','5','6','7','8','9','10']
for index in listIndex:   
#     data = open(os.path.join( "jsonYear/1970-1969/" , listIndex + '.json',encoding="utf8").read()
    data = open('jsonYear/2000-2009/'+str(index)+'.json',encoding="utf8").read()
    theJSON = json.loads(data)
    print(theJSON)

    #split object
    for item in theJSON['songs']:  
        print(item)
        if(len(item['lyricsUrl']) > 0): 
            lyricsText,lyricsHtml,wordsAmount,commonWordInLyrics,img,subject = getLyrics(item['lyricsUrl'])

            item['lyricsText'] = lyricsText
            item['lyricsHtml'] = lyricsHtml
            item['wordsAmount'] = wordsAmount
            item['commonWordInLyrics'] = commonWordInLyrics
            item['lyricsUrl'] = img
            item['subject'] = subject

    with open("jsonLast/2000-2009/"+str(index)+".json","w", encoding='utf-8') as jsonfile:
        json.dump(theJSON,jsonfile,ensure_ascii=False)


print("ok")
            