
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


def get_weather_report(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=3333f1121fb3237384cd5caf21f597e5&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_report = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return weather_report
    else:
        return None


class WeatherReport(Action):
    def name(self) -> Text:
        return "action_weather_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get user message text
        user_message = tracker.latest_message.get('text', '')

        # Extract city entity from user input text
        city_entity = self.extract_city_entity(user_message)

        if city_entity:
            weather_report = get_weather_report(city_entity)
            if weather_report:
                dispatcher.utter_message(text=f"City Name: {city_entity}\nTemperature: {weather_report['temperature']}°C\n"
                                              f"Humidity: {weather_report['humidity']}%\nPressure: {weather_report['pressure']} hPa\n"
                                              f"Wind Speed: {weather_report['wind_speed']} m/s\nDescription: {weather_report['description']}")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't retrieve the weather information for {city_entity}. Please try again.")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find any city name in your message. Please enter a valid city name.")

        return []

    def extract_city_entity(self, text: Text):
        # Split the text into words
        words = text.lower().split()

        # Find the index of "in" in the words list
        index_of_in = None
        if "in" in words:
            index_of_in = words.index("in")

        # If "in" is found and there's a word after it, assume it's the city name
        if index_of_in is not None and index_of_in < len(words) - 1:
            city_name = words[index_of_in + 1]
            return city_name
        else:
            return None


class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected {food_entity} as your food choice.")
        else:
            dispatcher.utter_message(text="Iam sorry. I could not detect the food choice")

        return []


class OrderFoodAction(Action):
    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, which kind of food would you like to order?")

        return []


class ConfirmOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"I have ordered {food_entity} for you.")
        else:
            dispatcher.utter_message(text="Iam sorry. I could not detect the food choice")

        return []

