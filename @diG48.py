from tkinter import *
from tkinter import StringVar
import time
import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit
import wikipedia
import smtplib
import pyjokes
from email.message import EmailMessage
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
window = Tk()

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def send(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('example@gmail.com', 'password')
        smtp.send_message(msg)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour <= 12):
        var.set("Good Morning Sir")
        window.update()
        speak("Good Morning Sir!")
    elif (hour >= 12) and (hour <= 18):
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("Myself @diG48! How may I help you sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn1.configure(bg='orange')
    btn2.configure(bg='#5C85FB')
    wishme()
    while True:
        btn1.configure(bg='orange')
        query = takecommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn2.configure(bg='#12cee3')
            label.configure(image=frames10)
            window.update()
            speak("Bye sir")
            break

        elif 'play' in query:
            label.configure(image=frames8)
            window.update()
            song = query.replace('play', '')
            speak('Playing' + song)
            pywhatkit.playonyt(song)
            continue

        elif 'who is' in query:
            person = query.replace('who is', '')
            label.configure(image=frames11)
            window.update()
            info = wikipedia.summary(person, 1)
            speak(info)

        elif 'greet' in query:
            var.set('Hello Sir, have a nice day')
            window.update()
            speak("Hello Sir, have a nice day")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            label.configure(image=frames2)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'whatsapp message' in query:
            label.configure(image=frames5)
            d = {'name': '+91'phone number''}
            speak('to whom u want to message')
            c = takecommand()
            e = d[c]
            speak('Tell me the message')
            f = takecommand()
            speak("at what hour u want to send")
            a = int(takecommand())
            speak(" at what minute u want to send")
            b = int(takecommand())
            window.update()
            pywhatkit.sendwhatmsg(e, f, a, b, 10)
            continue

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            label.configure(image=frames4)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'thank you' in query:
            var.set("Welcome Sir")
            label.configure(image=frames12)
            window.update()
            speak("Welcome Sir")

        elif 'your name' in query:
            label.configure(image=frames0)
            var.set("Hi, Im @diG48 the Robot. Speed 1 terahertz, memory 1 gigabyte  ")
            window.update()
            speak('Hi, Im @diG48 the Robot. Speed 1 terahertz, memory 1 gigabyte ')

        elif 'who created you' in query:
            label.configure(image=frames9)
            var.set('I was created by AdithyaaG48')
            window.update()
            speak('I was created by AdithyaaG48')

        elif 'hello' in query:
            label.configure(image=frames6)
            var.set('Hello Everyone! My self @diG48')
            window.update()
            speak('Hello Everyone! My self @diG48')

        elif 'email' in query:
            label.configure(image=frames3)
            window.update()
            try:
                msg = EmailMessage()
                c = {'name': 'example@gmail.com'}
                speak('To Whom You Want To Send Email')
                b = takecommand()
                d = c[b]
                msg['To'] = d
                speak('Tell Me The Subject In Your Email')
                a = takecommand()
                msg['Subject'] = a
                msg['From'] = 'adithyaaaibot@gmail.com'
                speak('Tell Me The Content Of The Email')
                e = takecommand()
                msg.set_content(e)
                send(msg)
                var.set('Your Email Has Been Sent Sir!!')
                speak('Your Email Has Been Sent Sir!!')
                time.sleep(1)
            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
        elif 'joke' in query:
            label.configure(image=frames7)
            window.update()
            speak(pyjokes.get_joke())
        else:
            if 'None' in query:
                speak('Unable to detect your voice')


def update(ind):
    frame = frames[ind % 100]
    ind += 2
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()
frames = [PhotoImage(file='Assistant3.gif', format='gif -index %i' % i) for i in range(100)]
frames0 = [PhotoImage(file='name.png')]
frames1 = [PhotoImage(file='creator.png')]
frames2 = [PhotoImage(file='time.png')]
frames3 = [PhotoImage(file='MAIL.png')]
frames4 = [PhotoImage(file='date.png')]
frames5 = [PhotoImage(file='WA.png')]
frames6 = [PhotoImage(file='hello.png')]
frames7 = [PhotoImage(file='joker.png')]
frames8 = [PhotoImage(file='YT.png')]
frames9 = [PhotoImage(file='creator.png')]
frames10 = [PhotoImage(file='bye.png')]
frames11 = [PhotoImage(file='who.png')]
frames12 = [PhotoImage(file='welcome.png')]

window.title('@diG48')

label = Label(window, width=1000, height=700)
label.pack()
window.after(0, update, 0)

btn1 = Button(text='START', width=23, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=25, command=window.destroy, bg='#12cee3')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()
