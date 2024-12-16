Vision AI Assistant

Vision is a smart AI-based voice assistant project built using Python. It can recognize voice commands, perform various system operations, and provide helpful responses like playing YouTube videos, searching Wikipedia, and reporting the weather.

📚 Table of Contents

Project Overview

Features

Technologies Used

Project Structure

Installation

Configuration

How to Run

Usage

File Descriptions

Acknowledgements

📖 Project Overview

Vision is a voice-controlled AI assistant that can automate tasks like opening apps, searching online, playing YouTube videos, sending WhatsApp messages, checking the weather, and more. The assistant listens for voice commands, recognizes them using speech recognition, and performs actions accordingly.

✨ Features

Voice Interaction: Vision responds to user voice commands.

App Control: Open common desktop applications like Notepad, Calculator, VS Code, and Discord.

Online Search: Search Google, Wikipedia, and YouTube directly from voice commands.

Email & Messaging: Send emails and WhatsApp messages.

Weather Reports: Get real-time weather information.

News Updates: Stay updated with the latest news by category.

Fun Features: Get jokes, advice, and more.

🛠️ Technologies Used

Language: Python

Libraries:

speech_recognition: To recognize and convert user speech to text.

pyttsx3: Text-to-speech conversion.

requests: API requests for news, weather, etc.

decouple: For environment variable management.

pprint: Pretty print output for readability.

📂 Project Structure

project-root/
├── .env                # Environment variables file
├── main.py             # Main script that controls the assistant
├── utils.py            # Utility functions for speech and text responses
├── PyWhatKit_DB.txt    # Log of messages sent via WhatsApp
├── pyvenv.cfg          # Python virtual environment configuration
└── functions/          # Folder containing function modules for app control and online operations

📦 Installation

Prerequisites

Python 3.8+

pip (Python package installer)

Step-by-Step Installation

Clone the Repository:

git clone https://github.com/ABHAYSARIYAL/jarvis.git
cd jarvis

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Required Packages:

pip install -r requirements.txt

Set Up Environment Variables:
Create a .env file in the root directory with the following content:

USER=YourName
BOTNAME=Vision
NEWS_API_KEY=your_news_api_key
OPENWEATHER_APP_ID=your_openweather_api_key
EMAIL=your_email@example.com
PASSWORD=your_email_password

Replace your_news_api_key, your_openweather_api_key, your_email@example.com, and your_email_password with your actual API keys and email credentials.

⚙️ Configuration

API Keys: You will need API keys for OpenWeather and News API.

Email Credentials: For sending emails, you may need to enable "Less Secure Apps" access in your email provider.

🚀 How to Run

Activate the Virtual Environment:

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Run the Application:

python main.py

💻 Usage

Here are some of the commands you can give to Vision:

System Control: "Open Notepad", "Open Calculator", "Open Discord", "Open VS Code"

Online Search: "Search on Google", "Search on Wikipedia", "Play on YouTube"

Messaging: "Send WhatsApp message", "Send an email"

Weather & News: "What's the weather?", "Show me the latest tech news"

Fun Commands: "Tell me a joke", "Give me some advice"

📁 File Descriptions

.env: Contains sensitive API keys and email credentials.

main.py: The main script that handles user input, triggers actions, and manages the assistant's logic.

utils.py: Utility file containing helper functions for text-to-speech and random opening text responses.

functions/: This folder contains all the specific modules for operations like sending emails, controlling apps, and fetching online data.

PyWhatKit_DB.txt: Stores logs of WhatsApp messages sent.

🤝 Acknowledgements

Special thanks to the creators of the following libraries and APIs used in this project:

SpeechRecognition

pyttsx3

OpenWeather API

News API

If you have any issues or suggestions, feel free to create a pull request or raise an issue on the repository.