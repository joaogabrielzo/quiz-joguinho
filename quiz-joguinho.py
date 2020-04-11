import requests
import json
from random import shuffle
import pyfiglet
import vlc
import os


path = os.path.abspath(os.path.dirname(__file__))

quiz_jogo = pyfiglet.figlet_format("QUIZ JOGUINHO")
print(quiz_jogo, "\t\t\t\t\t\t\t\tTá em inglês fodase")

start = input("\nVamo começar? (s/n): " )

if start == "s":

    continua = "s"

    while continua == "s":
        gugu = vlc.MediaPlayer(path + "/resources/valendoooo.mp3")
        gugu.play()

        r = requests.get("https://opentdb.com/api.php?amount=1")

        content = r.content.decode("us-ascii")

        originalJson = json.loads(content)

        jsonVal = originalJson["results"][0]    

        if jsonVal["type"] == "multiple":

            listMultiple = [jsonVal["correct_answer"], 
                            jsonVal["incorrect_answers"][0], 
                            jsonVal["incorrect_answers"][1], 
                            jsonVal["incorrect_answers"][2]]

            shuffle(listMultiple)

            toPrint = """\n
            Question: {}

            1) {}
            2) {}
            3) {}
            4) {}
            """.format(jsonVal["question"], 
                    listMultiple[0],
                    listMultiple[1],
                    listMultiple[2],
                    listMultiple[3])
        else:
            listBool = [
                        jsonVal["correct_answer"], 
                        jsonVal["incorrect_answers"][0]
                        ]

            shuffle(listBool) 
                   
            toPrint = """
            Question: {}

            1) {}
            2) {}
            """.format(jsonVal["question"], 
                    listBool[0], 
                    listBool[1])

        print(toPrint)
        resposta = input("\nDigita a resposta: ")

        respostaCerta = jsonVal["correct_answer"]

        if (resposta == respostaCerta) | (resposta == bool(respostaCerta)):
            kasinao = vlc.MediaPlayer(path + "/resources/ae-kasinao.mp3")
            kasinao.play()
        else:
            faustao = vlc.MediaPlayer(path + "/resources/faustao-errou.mp3")
            faustao.play()

        continua = input("\nVai de novo? (s/n): ")

else:
    print("\nTá bom então.")

print("\nTá bom então.")
