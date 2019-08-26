import random
import requests

from pip._vendor.distlib.compat import raw_input


greetings = ['hello', 'hi', 'hey', 'hey!']
random_greetings = random.choice(greetings)
question1 = ['i want to book a train ticket','book me a train ticket','train ticket for me','train ticket','ticket','tickets','book ticket']
responses = ['Sure! Please tell me your name.']
random_response = random.choice(responses)
question2 = ['what are the trains available from pondy to chennai ?','trains from pondy to chennai','pondy to chennai','chennai to pondy']
trains = ['16116 PDY MS EXP daily,22403 PDY NDLS WEEKLY EXP wed,56038 PDY MS PASS daily,12897 PDY BBS WEEKLY EXP wed']
random_responses = random.choice(trains)
question3 = ['how are you ?','how are you','how do you do','how do you do?']
reply = ['i am fine','going good']
random_reply = random.choice(reply)
question4 = ['what is your name ?','what is your name','your name please','your name']
intro = ['I am chatto','My name is chatto']
random_intro = random.choice(intro)
question5 = ['what is your job?','who are you','who are you ?','your job','your work','your job?','your work ?']
working = ['I am a railway reservation chatbot','I am a chatbot and I book train tickets']
random_working = random.choice(working)
question6 = ['current station']
question7 = ['thank you','thanks']
compliment = ['You are welcome']
random_compliment = random.choice(compliment)

while True:
    userInput = raw_input(">>> ")
    if userInput in greetings:
        print(random_greetings)
    elif userInput in question1:
        print(random_response)
    elif userInput in question2:
        print(random_responses)
    elif userInput in question3:
        print(random_reply)
    elif userInput in question4:
        print(random_intro)
    elif userInput in question5:
        print(random_working)
    elif userInput in question7:
        print(random_compliment)
    elif userInput in question6:
        trainNo = "24678"
        trainDate = "20190824"
        StationCode = "NJP"
        r1 = requests.get('http://indianrailapi.com/api/v2/livetrainstatus/apikey/3d0c1d958e0c6b0ab391f83e8567fc0f/trainnumber/'+trainNo+'/date/'+trainDate)
        r2 = requests.get('http://indianrailapi.com/api/v2/AllTrainOnStation/apikey/3d0c1d958e0c6b0ab391f83e8567fc0f/StationCode/'+StationCode)         
        data1 = r1.json()
        data2 = r2.json()
        ListOfTrains = data2['Trains']

        for x in ListOfTrains:
          #if x['TrainName'] == 'SWATANTRTA S':
            print('The train '+x['TrainName']+' is at the station')
    else:
      print("I did not understand what you said")