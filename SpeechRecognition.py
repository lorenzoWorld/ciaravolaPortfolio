from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  Utilizzare il comando SAY integrato del sistema invece di mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')



def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(' Ready... ')
        r.pause_threshold = 3.0
        #r.adjust_for_ambient_noise(source, duration=3.0)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #Torna indietro per continuare ad ascoltare i comandi se viene ricevuto un parlato irriconoscibile
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    

    
    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'Lorenzo' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('Ciao Lorenzo', 'juventinolory@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('I am ready for your command')

#ciclo per continuare l'esecuzione di più comandi
while True:
    assistant(myCommand())



