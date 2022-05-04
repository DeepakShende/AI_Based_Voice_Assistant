from google import google
import boto3
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import ctypes

from fb import facebook

speech = sr.Recognizer()

greeting_dict = {'hello': 'hello', 'hi': 'hi', 'hey': 'hey'}
open_launch_dict = {'open': 'open', 'launch': 'launch', 'start': 'start'}
search_dict = {'search': 'search','google':'google','calculate':'calculate','translate':'translate'}
wiki_dict = {'wikipedia': 'wikipedia'}
google_searches_dict = {'what': 'what', 'who': 'who', 'why': 'why', 'when': 'when', 'tell': 'tell', 'from': 'from',
                        'for': 'for', 'if': 'if', 'find': 'find', 'get': 'get', 'give': 'give', 'how': 'how',
                        'by': 'by'}
social_media_dict = {'facebook': 'https:facebook.com', 'fb': 'https:facebook.com', 'twitter': 'https://www.twitter.com',
                     'snapchat': 'https://www.snapchat.com', 'whatsapp': 'https://web.whatsapp.com',
                     'gmail': 'https://mail.google.com', 'linkedin': 'https://in.linkedin.com',
                     'instagram': 'https://www.instagram.com', 'insta': 'https://www.instagram.com',
                     'word': 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word',
                     'excel': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel',
                     'powerpoint': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint',
                     'onedrive': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneDrive for Business',
                     'access': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access',
                     'outlook': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook',
                     'publisher': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publisher',
                     'kdk': 'https://www.kdkce.edu.in/',
                     'gl':'https://www.greatlearning.in/'}
social_post = {'post': 'post'}

mp3_thankyou_list = ['Aiva Mp3/Thanku1.mp3', 'Aiva Mp3/Thanku2.mp3']
mp3_system_locked = ['Aiva Mp3/Your system is locked. You need to login to continue.mp3',
                     'Aiva Mp3/Your windows is locked. You need to login to countinue.mp3']
mp3_namaste_list = ['Aiva Mp3/namaste.mp3']
mp3_network_list = ['Aiva Mp3/Network Error1.mp3', 'Aiva Mp3/Network Error2.mp3']
mp3_google_search = ['Aiva Mp3/Google Search1.mp3', 'Aiva Mp3/Google Search2.mp3']
mp3_listening_problem_list = ['Aiva Mp3/Problem Hearing1.mp3', 'Aiva Mp3/Problem Hearing2.mp3']
mp3_struggling_list = ['Aiva Mp3/I am struggling to get you please try again later .mp3',
                       'Aiva Mp3/I think i need a reboot.mp3']
mp3_greeting_list = ['Aiva Mp3/Hello! How may i help you.mp3', 'Aiva Mp3/Hi! How may i help you.mp3',
                     'Aiva Mp3/Hey! How may i help you.mp3']
mp3_open_launch_list = ['Aiva Mp3/Okay! Getting results..mp3', 'Aiva Mp3/Got it!.mp3']
mp3_Bye_list = ['Aiva Mp3/I will say goodbye in French. Au revoir.mp3', 'Aiva Mp3/OK then! i am  going for a sleep.mp3',
                'Aiva Mp3/Bye buddy! have a nice day..mp3', 'Aiva Mp3/See you soon .mp3',
                'Aiva Mp3/Au revoir! thats goodbye in french.mp3', 'Aiva Mp3/Goodbye.mp3']

error_occurrence = 0
counter = 0

polly = boto3.client('polly')


def to_be_posted(voice_note):
    for key in social_media_dict.keys():
        if key in voice_note:
            return key


def play_sound_from_polly(result, is_google=False):
    global counter
    mp3_name = "output{}.mp3".format(counter)
    obj = polly.synthesize_speech(Text=result, OutputFormat='mp3', VoiceId='Matthew')
    play_sound(mp3_google_search)
    with open(mp3_name, 'wb') as file:
        file.write(obj['AudioStream'].read())
        file.close()
    playsound(mp3_name)
    os.remove(mp3_name)
    counter += 1


def google_search_result(query):
    search_result = google.search(query)
    for result in search_result:
        print(result.description.replace('...', '').rsplit('.', 3)[0])
        if result.description != '':
            play_sound_from_polly(result.description.replace('...', '').rsplit('.', 3)[0])
            break



def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('Listening.....')

    global error_occurrence

    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:

        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    except sr.RequestError as e:
        print('Network Error.')
        play_sound(mp3_network_list)
    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except IndexError:
            pass

    return False


if __name__ == '__main__':

    playsound('Aiva Mp3/Hi! This is your Artificial Intelligence AVA.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In Greeting.....')
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_note(open_launch_dict, voice_note):
            print('In Open.....')
            play_sound(mp3_open_launch_list)
            if (is_valid_note(social_media_dict, voice_note)):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer c:\\"{}"'.format(voice_note.replace('open ', '').replace('launch ', '')))
            continue

        elif is_valid_google_search(voice_note):
            print('On Web.....')
            playsound('Aiva Mp3/Got it!.mp3')
            # webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            google_search_result(voice_note)
            continue

        elif is_valid_note(search_dict, voice_note):
            print('On Web.....')
            playsound('Aiva Mp3/Got it!.mp3')
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            # google_search_result(voice_note)
            continue

        elif is_valid_note(wiki_dict, voice_note):
            print('On Web.....')
            playsound('Aiva Mp3/Got it!.mp3')
            webbrowser.open('https://en.wikipedia.org/wiki/{}'.format(voice_note))
            # google_wikipedia_result(voice_note)
            continue

        elif 'namaste' in voice_note:
            play_sound(mp3_namaste_list)
            continue

        elif 'post' in voice_note:
            media = to_be_posted(voice_note)
            if media == 'facebook':
                facebook().post_on_wall(voice_note.split(media + ' ')[1].capitalize())
                play_sound_from_polly('The Post is liive now.')
                continue

        elif 'lock' in voice_note:
            for value in ['pc', 'system', 'window', 'windows']:
                ctypes.windll.user32.LockWorkStation()
                play_sound(mp3_system_locked)
                exit()

        elif 'thank you' in voice_note:
            play_sound(mp3_thankyou_list)
            continue

        elif 'goodbye' in voice_note:
            play_sound(mp3_Bye_list)
            exit()
