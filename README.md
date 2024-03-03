Certainly! Here's the updated documentation with the installation instructions and git clone command:

---

# WeatherBot

WeatherBot is a conversational chatbot built using Rasa Open Source, designed to provide users with live weather forecasts for cities around the world.

## Overview

WeatherBot features a single custom action that retrieves live weather information for a specified city using the OpenWeatherMap API. Users can interact with the bot by asking about the weather conditions in a particular city using various natural language queries.

## Usage

### Training the Bot

Before using the bot, you need to train it with the latest changes. Run the following command in the terminal:

```bash
rasa train
```

### Starting the Bot

To start the chatbot, run the following commands:

```bash
rasa shell
```

```bash
rasa run actions
```

The first command launches the Rasa shell for interacting with the bot, while the second command starts the action server to handle custom actions.

### Intents

WeatherBot supports the following intents for querying weather information:

- `live_weather`: This intent covers various natural language queries about the current weather conditions in a specific city. Examples include:
  - How is the weather in [city]?
  - Is it raining in [city] right now?
  - What's the temperature in [city]?
  - Can you give me a weather update in [city]?

You can find these intents defined in the `nlu.yml` file.

### Custom Action

The custom action implemented in WeatherBot retrieves live weather forecasts for cities using the OpenWeatherMap API. The action is triggered when the user asks about the weather in a particular city.

## Dependencies

- Rasa Open Source
- OpenWeatherMap API

- Please note that WeatherBot is compatible with Python versions from 3.6 to 3.8. It will not work with Python versions above 3.8.

## Getting Started

To get started with WeatherBot, follow these steps:

1. Clone the WeatherBot repository:

   ```bash
   git clone https://github.com/mujjasaikumar/live_weather_with_Rasa_chatbot.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the bot using `rasa train`.

4. Start the bot using `rasa shell` and `rasa run actions`.

5. Interact with the bot by asking about the weather in different cities.

---

Author: Saikumar Mujja

---
