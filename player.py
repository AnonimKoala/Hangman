import json


class Player:
    playersArr = []
    LOGGED = []

    def __init__(self, name, password, score):
        self.name = name
        self.password = password
        self.score = score

    def loadPlayers():
        f = open("data/players/data.json")
        data = dict(json.load(f))

        for p in data['players']:
            Player.playersArr.append(p)

    def login():
        name = str(input("Podaj nazwe gracza: "))
        password = str(input("Podaj haslo: "))

        obj= None
        for el in Player.playersArr:
            if(name in el):
                obj = el[name]

        if(obj):
            if(obj['password'] == password):

                gotScore = 0
                for el in Player.playersArr:
                    if(name in el):
                        gotScore = el[name]['score']

                Player.LOGGED.append({
                    "name": name,
                    "score": int(gotScore)
                })
                print("Witaj ",name)

                together = str(input("Czy kolejny gracz chce dołaczyć? T/N: "))
                if together.upper() == 'T':
                    Player.login()

            else:
                print("Bład loginu!")
                exit()

        else:
            Player.playersArr.append({
                name: {
                    "password": password,
                    "score": 0
                }
            })
            Player.LOGGED.append({
                "name": name,
                "score": 0
            })
        
    def save():
        print(Player.LOGGED)
        print(Player.playersArr)

        for log in Player.LOGGED:
            for arrEl in Player.playersArr:
                if (log['name'] in arrEl):
                    arrEl[log['name']]['score'] = log['score']
                    break

        outObj = {
            "players": Player.playersArr
        }

        json_object = json.dumps(outObj, indent=4)
        
        with open("./data/players/data.json", "w") as outfile:
            outfile.write(json_object)