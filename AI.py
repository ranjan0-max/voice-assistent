# ctrl+w will use for close browser tab 
#  ctrl+tab is use for switch between tabs

import os
import sysinfo
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import sys
import ctypes
import win10toast
from csv import DictWriter
import psutil
import weather_location
import command
import shortcut
import downloading_link


engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice',voices[0].id)
engin.setProperty('rate', 175)  # speed of talking

def speak (audio):
    engin.say(audio)
    engin.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("sir Good morning. Welcome back")
    elif 12 <= hour < 18:
        speak("sir Good afternoon. Welcome back")
    else:
        speak("sir good evening. Welcome back")
    speak("What you want to do sir")

def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold=0.5
            print("listening...")
            audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"user said : {query}\n")
            except Exception :
                # speak("say that again please")
                return "none"
            return query
    except:
        print("your internet is not working")
        print("check your connection")
        print("and run it again")


def birthday_note():
    speak("sir tell me the date")
    date=take_command()
    speak("what is the name ")
    pname=take_command()
    with open('birthday.csv','a') as wf:
        csv_writer = DictWriter(wf, fieldnames=['date','name'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'date':date,
        'name':pname
    })

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def write_note():
    speak("sir tell me the name of note")
    name_note=take_command()
    speak("What should i write sir")
    note = take_command()
    
    file = open(f'{name_note}.txt', 'w')
    speak("Sir, Should i include date and time")
    snfm = take_command()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        strdate=datetime.datetime.now().date()
        file.write(f"{strTime}\n")
        file.write(f"{str(strdate)}\n")
        file.write(" :---  ")
        file.write(note)
    else:
        file.write(note)        

if is_admin():
    if __name__ == "__main__":
        # wish_me()
        while True:
            query = take_command().lower()
            if "jarvis" in query:
                query=query.replace("jarvis","")
                if "wikipedia" in query:
                    speak('searching wikipedia...')
                    query = query.replace('wikipedia',"")
                    results = wikipedia.summary(query, sentences=2)
                    speak("according to wikipedia ")
                    speak(results) 

                elif "setup my pc" in query or "make my pc" in query:
                    webbrowser.open_new(downloading_link.broser())
                    webbrowser.open(downloading_link.vscode())
                    webbrowser.open(downloading_link.winrar())
                    webbrowser.open_new(downloading_link.idm())
                    webbrowser.open_new(downloading_link.office())

                elif "movies" in query or "web series" in query:
                    speak("sir you want to open all website")
                    rp=take_command()
                    if "yes" in query or "Yes" in query:
                        for i in downloading_link.movies_link():
                            webbrowser.open_new(i)
                    else:
                        webbrowser.open_new(downloading_link.movies_link()[0])          

                elif "open whatsapp" in query or "start whatsapp" in query:
                    try:
                        os.startfile('C:\\Users\\boom\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
                    except:
                        speak("sir i can't find whatsapp")
                        speak("whould you like to download it ?")
                        w=take_command()
                        if "yes" in query or "sure" in query:
                            webbrowser.open_new(downloading_link.whatsapp())
                            speak("sir after go to you download folder and install it")    

                elif "change window" in query:
                    shortcut.change_window()

                elif "next song" in query or "change song" in query:
                    shortcut.nexttrack()

                elif "previous song" in query or "last song" in query:
                    shortcut.prevtrack()   

                elif "open word pad" in query or "open wordpad" in query:
                    try:
                        shortcut.word_pad()
                    except:
                        speak("can't able to open wordpad")     
                
                elif "open ms word" in query or "open word" in query:
                    try:
                        shortcut.msword()
                    except:
                        speak("can't able to open M s word")    

                elif "open control panel" in query:
                    os.startfile("appwiz.cpl")

                elif "open drive D" in query or "open drive d" in query:
                    try:
                        os.startfile("D:")
                    except:
                        speak("sir you don't have D drive")

                elif "open drive C" in query or "open drive c" in query:
                    os.startfile("C:") 
                           

                elif "system information" in query or "system config" in query or "system configration" in query:
                    try:
                        sys_info=sysinfo.info()
                        memory_info=sysinfo.memory()
                        speak(f"sir, Your O S is {sys_info[0]} {sys_info[1]}")
                        speak(f"you have {sys_info[3]} bit architecture. And {sys_info[2]} Processor")
                        speak(f"you have {memory_info[0]} G B ram")
                        speak(f"and {memory_info[3]} G B hard disk")
                    except:
                        speak("sir for some reason i don't having your system information")                                   

                # elif "camera" in query or "take a photo" in query:
                #     cname=random.randint(1,9999)
                #     ec.capture(0, "Jarvis Camera ",f"img{cname}.jpg")    

                elif "open youtube" in query:
                    speak("opening youtube")
                    try:
                        webbrowser.open_new('www.youtube.com')
                    except:
                        speak("sir i'm not able to open youtube")
                        speak("you mush check your internet connection")    

                elif "facebook" in query or "open facebook" in query:
                    try:
                        speak("opening facebook")
                        webbrowser.open_new("www.facebook.com")
                    except:
                        speak("for some reason facebook is not opening")
                        speak("you should check what is the problem")    

                elif "open stackoverflow" in query:
                    try:
                        speak("opening stack overflow")
                        webbrowser.open_new("www.stackoverflow.com")
                    except:
                        speak("not able to open stack over flow")    

                elif "vs code" in query:
                    speak("ok sir")
                    try:
                        os.startfile('C:\\Users\\boom\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
                    except:
                        speak("i didn't find VS code sir")
                        speak('would you like me to download it')
                        ans=take_command()
                        if "yes" in ans or "sure" in ans:
                            webbrowser.open_new(downloading_link.vscode())
                        else:
                            pass

                elif  "play songs" in query:
                    speak("ok sir")
                    webbrowser.open_new("https://music.youtube.com/watch?v=L7T6UOkHkJo&list=RDAMVML7T6UOkHkJo")

                elif "weather" in query:
                    try:
                        speak("tell me the location sir.")
                        location=take_command()
                        city,format_add,temp=weather_location.weather(location)
                        speak(f"current weather of {city} is {format_add} , and temperature is {temp}")   
                    except:
                        speak("right now i don't have any information")
                        speak("try again")

                elif "tell me time" in query or "time" in query or "what's the time" in query:
                    try:
                        curr_time = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"sir time is {curr_time}")
                    except:
                        speak("not able to tell time right now")
                        speak("try again")

                elif "date" in query or "what's the date" in query or "tell me the date" in query or "todays date" in query:
                    try:
                        curr_date = datetime.datetime.now().date()
                        print(curr_date)
                        speak(f"sir the date is {curr_date}")
                    except:
                        speak("something is wrong")
                        speak("try again")

                elif "quit" in query or "exit" in query or "close" in query or "bye" in query:
                    speak("Good bye sir, Have a nice day ")
                    sys.exit()

                elif "wish me" in query:
                    wish_me()

                elif "open run" in query:
                    shortcut.run()

                elif "get password" in query:
                    wifi_list=command.wifipassword()
                    for x in range(len(wifi_list)):
                        speak("Here is the list sir")
                        print(wifi_list[x])

                elif "what is my ip"in query or "my ip" in query or "my ip address" in query or "what's my ip address"in query:
                    speak("sir Our ip address is ")
                    speak(weather_location.ip())

                elif "location" in query:
                    try:
                        data=weather_location.location()
                        speak(f"{data['country']},{data['region']} and somewhere around {data['city']}")
                    except:
                        speak("API is not working properly")

                elif "find on youtube" in query:
                    speak("what you want to search sir")
                    s=take_command().lower()
                    pywhatkit.playonyt(s)

                elif "shutdown pc" in query:
                    speak("Ok sir good Bye, take care")
                    os.system("shutdown /s /t 15")

                elif "cancel shutdown" in query:
                    os.system("shutdown /a")

                elif "take screenshot" in query:
                    try:
                        shortcut.screan_shot()
                        speak("Sir done.")
                    except:
                        speak("something is not right")
                        speak("try again")

                elif "volume up" in query:
                    try:
                        query=query.replace("volume up","")
                        query=query.replace("x","")
                        query=query.replace("by","")
                        shortcut.volumeup(query)
                        speak(f"volume up by {query}")
                    except ValueError:
                        speak("sir value error occured")
                        speak("try again sir")

                elif "volume down" in query:
                    try:
                        query=query.replace("volume down","")
                        query=query.replace("x","")
                        query=query.replace("by","")
                        shortcut.volumedown(query)    
                        speak(f"volume down by {query}")    
                    except ValueError:
                        speak("sir value error occured")
                        speak("try again sir")

                elif "pause music" in query:
                    try:
                        shortcut.pausemusic()
                        speak("ok sir")
                    except:
                        speak("not able to pause music")
                        speak("try again")

                elif "play music" in query:
                    try:
                        shortcut.resumemusic()
                        speak("ok sir")        
                    except:
                        speak("can't able to do")
                        speak("try again")

                elif "disable wi-fi" in query:
                    try:
                        command.disabelwifi()
                        speak("Sir done") 
                    except:
                        speak("not able to disable wi-fi")

                elif "enable wi-fi" in query:
                    try:
                        command.enablewifi()
                        speak("sir done.")    
                    except:
                        speak("not able to enable wi-fi")

                elif "open notepad" in query:
                    try:
                        shortcut.notepad()    
                    except:
                        speak("sir not able to open notepad")
                        speak("something is wrong")

                elif 'how are you' in query:
                    speak("I am fine sir")
                    speak("How are you Sir")
                    ans=take_command().lower()
                    if 'fine' in ans or "good" in ans:
                        speak("It's good to know that your fine")     

                elif "who made you" in query or "who created you" in query: 
                    speak("I have been created by Ranjan.")    

                elif 'what is love' in query or 'what do you think about love' in query:
                    speak("sir It is 7th sense that destroy all other senses")    

                elif 'lock window' in query:
                    try:
                        speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()    
                    except:
                        speak("sir something wrong")
                        speak("try again")

                elif "write a note" in query:
                    write_note()

                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")  
                    print(file.read())
                    speak(file.read(6))   

                elif "will you be my gf" in query or "will you be my bf" in query:   
                    speak("I'm not sure about, may be you should give me some time")     

                elif "set reminder" in query:
                    speak("tell me the reminder")
                    rem = take_command()
                    toaster = win10toast.ToastNotifier()
                    toaster.show_toast('pc',f'{rem}',duration=5)     

                elif "help me" in query:
                    speak("tell me what to do sir")
                    query=take_command()
                    pywhatkit.search(query)    

                elif "what is "in query :
                    query=query.replace("what is ","")
                    pywhatkit.search(query)      
                
                elif "search" in query or "search about":
                    query=query.replace("search","")
                    query=query.replace("about","")
                    pywhatkit.search(query) 

                elif "how much power we have" in query :
                    try:
                        battery=psutil.sensors_battery()
                        parcentage = battery.percent
                        print(parcentage)
                        if parcentage >= 75:
                            speak("we have enough power to do perfomes various taks") 
                        elif parcentage >= 40 and parcentage <= 75:
                            speak(f"we have {parcentage} power , I think you should plug the charger") 
                        elif parcentage >= 15 and parcentage <=30:
                            speak(f"we have only {parcentage} power , please connect charger") 
                        elif parcentage <= 15:
                            speak(f"we left with {parcentage} only , so please connect charger")            
                    except:
                        speak("something went worng")
                        speak("i will be report developer to fix it")
                else:
                    pass 
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)                