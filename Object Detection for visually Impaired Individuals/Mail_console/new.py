import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust microphone for ambient noise
            voice = listener.listen(source, timeout=5)  # Listen for up to 5 seconds
            print('processing...')
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Could you please repeat?")
        return get_info()  # Retry if speech is not recognized
    except sr.RequestError:
        talk("Sorry, I'm having trouble accessing the Google API. Please try again later.")
        return None



def send_email(receiver, subject, message):
    print("Inside send_email function")  # Add this line
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login('utkarshnileshawasthi@gmail.com', 'bvectqzeeeacogtl')
        email = EmailMessage()
        email['From'] = 'Sender_Email'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
    except Exception as e:
        print("An error occurred:", e)  # Print the error message


email_list = {
    'ayush': 'yadavas_2@rknec.edu',
}


def get_email_info():
    talk('Hi Sir I am your assistant for today, To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Thankyou sir for using me. Your email has been send')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()