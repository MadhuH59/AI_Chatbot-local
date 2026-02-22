import speech_recognition as sr
import pyttsx3

# Text-to-Speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            # ⭐ IMPORTANT FIX
            audio = recognizer.listen(
                source,
                timeout=5,          # wait max 5 sec to start speaking
                phrase_time_limit=8 # max speaking time
            )

        print("Recognizing...")

        text = recognizer.recognize_google(audio)
        print("You said:", text)

        return text

    except sr.WaitTimeoutError:
        return "No speech detected."

    except sr.UnknownValueError:
        return "Could not understand audio."

    except Exception as e:
        return f"Voice error: {str(e)}"