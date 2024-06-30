import datetime
import speech_recognition as sr
import os
from google.cloud import texttospeech

def GoogleTTS(text, filename):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient.from_service_account_json("ai-customer-service-428015-b73c28091855.json")

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN",
        name="en-IN-Wavenet-A",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(f"{filename}", "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{filename}"')

def speech(text, filename):
    print("Google tts is generating voice output.")
    GoogleTTS(text, filename)

def say(text):
    filename = "assistant-replies.wav"
    speech(text, filename)
    os.system(f"afplay {filename}")


def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising the audio...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except:
            return ""
            # return "Sorry. I couldn't understand that. Can you repeat?"

def write_text_to_file(text, file_path):
    try:
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(text)  # Write the text to the file
        print(f"Text written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")



###############################################################################################################

def site_opener(query):
    if "open" in query.lower():
        import webbrowser
        site_open_query = ''.join(query.split()[1:])
        print(site_open_query)
        webbrowser.open(f"https://{site_open_query}.com")
        say(f"Opening {site_open_query} sir")

#TODO: add app opening functionalities.
def file_opener(query):
    if "play music" in query.lower():
        musicPath = r"/Users/ratanprakash/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/IIT Techfest 2020  - SHKHR.mp3"
        os.system(f"open '{musicPath}'")
        say("Playing Music.")

def datetime_teller(query):
    if "time right now" in query.lower():
        say(f"the time right now is {datetime.datetime.now().strftime('%H:%M:%S')}")



