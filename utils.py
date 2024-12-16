import pyttsx3

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)  # Set speech rate
engine.setProperty('volume', 1.0)  # Set volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Define the speak function to use text-to-speech
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()


opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]
