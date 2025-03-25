import speech_recognition as sr
import pyttsx3
import openai

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume level

# OpenAI API Key (Replace with your own key)
openai.api_key = "your_api_key_here"

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return "I didn't catch that"
    except sr.RequestError:
        return "Sorry, the service is unavailable"

# Function to process AI-generated responses
def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Choose appropriate model
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Main Function
def assistant():
    while True:
        command = listen()
        print(f"You said: {command}")

        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif "your name" in command:
            speak("I am your voice assistant!")
        else:
            ai_response = ask_ai(command)
            speak(ai_response)

# Run the Assistant
if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    assistant()
