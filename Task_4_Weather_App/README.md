# 🌦️ Weather App

A professional Python weather application that fetches and displays real-time weather information using the OpenWeatherMap API.

This project was developed as part of my **Python Programming Internship – Task 4: Basic Weather App**.

---

## 📌 Project Overview

The Weather App allows users to search for a city and view current weather information through a clean and user-friendly graphical interface.

The application retrieves live weather data from the OpenWeatherMap API and displays important weather details including temperature, humidity, wind speed, weather condition, pressure, visibility, and forecast information.

---

## ✨ Features

### 🌤️ Current Weather

- 🔍 Search weather by city name
- 🌡️ Current temperature
- 🌡️ Celsius and Fahrenheit units
- 🌧️ Current weather condition
- 🌡️ Feels-like temperature
- 💧 Humidity
- 💨 Wind speed
- 🌡️ Atmospheric pressure
- 👁️ Visibility
- 📅 Current date
- 🕐 Local time

### 📅 Forecast

- 5-day weather forecast
- Daily maximum temperature
- Daily minimum temperature
- Weather conditions for upcoming days

### 🛡️ Error Handling

- Empty location validation
- City not found handling
- Invalid API key handling
- Network connection errors
- Request timeout handling
- Unexpected API response handling

### 🔐 Security

- API key stored in `.env`
- `.env` excluded from GitHub using `.gitignore`

---

## 📸 Screenshots

### 🏠 Weather Dashboard

![Weather Dashboard](screenshots/weather-dashboard.png)

The main dashboard displays the current weather information, temperature, humidity, wind speed, and forecast.

---

### ❌ City Not Found

![City Not Found](screenshots/city-not-found.png)

The application displays an error message when an invalid or unavailable city is entered.

---

### 🌡️ Fahrenheit Mode

![Fahrenheit Mode](screenshots/fahrenheit-mode.png)

Users can switch between Celsius and Fahrenheit using the unit toggle.

---

### ⚠️ Empty Input Validation

![Empty Input](screenshots/empty-input.png)

The application prevents an empty search from being submitted.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Requests | API requests |
| JSON | Processing API responses |
| Tkinter | Graphical user interface |
| python-dotenv | Secure API key management |
| OpenWeatherMap API | Real-time weather data |

---

## 📂 Project Structure

```text
Weather App/
│
├── screenshots/
│   ├── weather-dashboard.png
│   ├── city-not-found.png
│   ├── empty-input.png
│   └── fahrenheit-mode.png
│
├── .env
├── .gitignore
├── requirements.txt
├── Weather.py
└── README.md