import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
from utils import speak  # Import speak from utils.py

# Now you can use speak in this file


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news(field):
    """
    Fetches the top five news headlines from GNews API for the given field and prints them in English.
    :param field: The category or field of news (e.g., sports, technology).
    """
    try:
        # Make the API call to fetch news
        res = requests.get(
            f"https://gnews.io/api/v4/top-headlines?topic={field}&lang=en&token={NEWS_API_KEY}"
        ).json()

        # Extract articles from the response
        articles = res.get("articles", [])

        # Prepare the top 5 headlines
        news_headlines = [article["title"] for article in articles[:5]]

        # Display the headlines
        if news_headlines:
            print(f"Top 5 News Headlines in {field.capitalize()}:")
            for i, headline in enumerate(news_headlines, start=1):
                print(f"{i}. {headline}")
                speak(headline)  # Reads out the headline
        else:
            print(f"No news articles found for {field}.")
            speak(f"I couldn't fetch any news articles for {field} right now.")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("I encountered an error while fetching the news. Please try again later.")



WEATHER_API_KEY = config("OPENWEATHER_APP_ID")  # Add your WeatherAPI key to the .env file

def get_weather_report(city):
    """
    Fetches the weather report for a given city using WeatherAPI.
    :param city: The name of the city to fetch weather for.
    :return: Tuple containing weather condition, temperature, and feels-like temperature.
    """
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
        )
        data = response.json()

        if "current" in data:
            weather = data["current"]["condition"]["text"]
            temperature = f"{data['current']['temp_c']}℃"
            feels_like = f"{data['current']['feelslike_c']}℃"
            return weather, temperature, feels_like
        else:
            error_message = data.get("error", {}).get("message", "Unknown error")
            print(f"Error in fetching weather: {error_message}")
            return None, None, None
    except Exception as e:
        print(f"Exception occurred while fetching weather data: {e}")
        return None, None, None


def get_city_from_ip():
    """
    Fetches the city name based on the user's IP address using ipapi.
    :return: City name as a string or None if unable to fetch.
    """
    try:
        # Fetch the IP address using the find_my_ip function
        ip_address = find_my_ip()

        # Use the IP to fetch the location data
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        data = response.json()

        # Extract and return the city
        city = data.get("city")
        if city:
            return city
        else:
            print(f"Error fetching city from IP: {data.get('error', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Exception occurred while fetching city from IP: {e}")
        return None






def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

