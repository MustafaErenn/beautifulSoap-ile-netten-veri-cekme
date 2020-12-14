import requests
from bs4 import BeautifulSoup

def winRate(zippedListParam):
    win=0;
    lose=0;
    for i in range(len(zippedListParam)):
        if(zippedListParam[i][0]=="Defeat"):
            lose = lose+1
        elif(zippedListParam[i][0]=="Victory"):
            win=win+1
    for i in range(len(zippedListParam)):
        print("Oyun Türü: ",zippedListParam[i][3],"- Tarih: ",zippedListParam[i][2],"- Şampiyon: ",zippedListParam[i][1],"- Sonuc: ",zippedListParam[i][0])
    print("10 Mactaki kazanma orani= %",win*10)




while(True):
    nickName = input('Enter your nickname:')

    url = "https://tr.op.gg/summoner/userName="+nickName

    r = requests.get(url)

    soup = BeautifulSoup(r.content,"html.parser")

    try:
        gelenVeri = soup.find("div",{"class":"GameItemList"}).find_all("div",{"class":"GameItemWrap"})

        matchHistoryArray = []
        characterNameArray = []
        timeStamp = []
        gameTypeList = []

        for matches in gelenVeri:
            result = matches.find("div", {"class": "GameResult"})
            name = matches.find("div", {"class": "ChampionName"})
            time = matches.find("div", {"class": "TimeStamp"})
            type = matches.find("div", {"class": "GameType"})


            gameResult = result.text
            gameResult = gameResult.replace("\n", "")
            gameResult = gameResult.replace("\t", "")

            characterName = name.text
            characterName = characterName.replace("\n", "")

            timeAgo = time.text
            timeAgo = timeAgo.replace("\n","")

            gameType = type.text
            gameType = gameType.replace("\n","")
            gameType = gameType.replace("\t", "")





            matchHistoryArray.append(gameResult)
            characterNameArray.append(characterName)
            timeStamp.append(timeAgo)
            gameTypeList.append(gameType)

        zippedList = zip(matchHistoryArray, characterNameArray,timeStamp,gameTypeList)

        zippedList = list(zippedList)

        winRate(zippedList)

        devamMi = input("Sorgulamaya devam etmek icin D/d tuşuna basiniz:")
        if(devamMi=="D" or devamMi=="d"):
            print("\n")
        else:
            print("Sorgulama Bitmistir.")
            break

    except:
        print("TR serverinde olmayan bir nickname girdiniz !")




