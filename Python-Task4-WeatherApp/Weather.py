from dotenv import load_dotenv
import os
import customtkinter as ctk
import requests
import threading
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

# ============================================================
# CONFIGURATION
# ============================================================

# IMPORTANT:
# Replace this with your NEW OpenWeatherMap API key
API_KEY = "798f7aa4ee42111e9ca25d3890cc6d8f"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# ============================================================
# COLORS
# ============================================================

BG = "#0F172A"
BG2 = "#172554"

BLUE = "#2563EB"
BLUE_HOVER = "#1D4ED8"

PURPLE = "#7C3AED"
PURPLE_HOVER = "#6D28D9"

WHITE = "#FFFFFF"
TEXT = "#172033"
MUTED = "#64748B"

CARD = "#FFFFFF"
CARD_SOFT = "#F8FAFC"
BORDER = "#E2E8F0"

SUCCESS = "#16A34A"
ERROR = "#DC2626"


# ============================================================
# APP
# ============================================================

class WeatherApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Weather App")
        self.geometry("1250x850")
        self.minsize(850, 650)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.current_data = None
        self.forecast_data = None

        self.unit = "C"
        self.loading = False

        self.configure(fg_color=BG)

        self.create_interface()

        self.city_entry.insert(0, "Pune")

        self.update_clock()

        # Automatically load Pune
        self.after(500, self.search_weather)


    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def create_interface(self):

        self.container = ctk.CTkScrollableFrame(
            self,
            fg_color=BG,
            corner_radius=0
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        self.container.grid_columnconfigure(
            0,
            weight=1
        )


        # ====================================================
        # HEADER
        # ====================================================

        header = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=40,
            pady=(30, 10)
        )

        header.grid_columnconfigure(
            1,
            weight=1
        )


        # Logo

        ctk.CTkLabel(
            header,
            text="☁️",
            font=("Segoe UI Emoji", 42)
        ).grid(
            row=0,
            column=0,
            rowspan=2,
            padx=(0, 12)
        )


        # App title

        title_box = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_box.grid(
            row=0,
            column=1,
            sticky="w"
        )

        ctk.CTkLabel(
            title_box,
            text="Weather App",
            font=("Segoe UI", 30, "bold"),
            text_color=WHITE
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_box,
            text="Real-time weather, anytime, anywhere ✦",
            font=("Segoe UI", 13),
            text_color="#CBD5E1"
        ).pack(
            anchor="w"
        )


        # Date

        self.date_card = self.small_header_card(
            header,
            "TODAY",
            "",
            2
        )


        # Time

        self.time_card = self.small_header_card(
            header,
            "LOCAL TIME",
            "",
            3
        )


        # ====================================================
        # DASHBOARD TITLE
        # ====================================================

        ctk.CTkLabel(
            self.container,
            text="Weather Dashboard",
            font=("Segoe UI", 38, "bold"),
            text_color=WHITE
        ).grid(
            row=1,
            column=0,
            pady=(25, 25)
        )


        # ====================================================
        # SEARCH BAR
        # ====================================================

        search = ctk.CTkFrame(
            self.container,
            fg_color=CARD,
            corner_radius=20
        )

        search.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=40,
            pady=(0, 18)
        )

        search.grid_columnconfigure(
            0,
            weight=1
        )


        self.city_entry = ctk.CTkEntry(
            search,
            placeholder_text="Search for a city...",
            placeholder_text_color="#94A3B8",
            font=("Segoe UI", 16),
            height=55,
            border_width=0,
            fg_color=CARD,
            text_color=TEXT
        )

        self.city_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(20, 8),
            pady=7
        )

        self.city_entry.bind(
            "<Return>",
            lambda event: self.search_weather()
        )


        self.search_button = ctk.CTkButton(
            search,
            text="🔍  Search",
            width=145,
            height=48,
            corner_radius=14,
            font=("Segoe UI", 14, "bold"),
            fg_color=PURPLE,
            hover_color=PURPLE_HOVER,
            command=self.search_weather
        )

        self.search_button.grid(
            row=0,
            column=1,
            padx=8,
            pady=7
        )


        # ====================================================
        # CONTROLS
        # ====================================================

        controls = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        controls.grid(
            row=3,
            column=0,
            pady=(0, 18)
        )


        self.unit_switch = ctk.CTkSegmentedButton(
            controls,
            values=["°C", "°F"],
            width=150,
            height=42,
            corner_radius=14,
            font=("Segoe UI", 13, "bold"),
            selected_color=PURPLE,
            selected_hover_color=PURPLE_HOVER,
            unselected_color=CARD,
            unselected_hover_color="#E2E8F0",
            text_color=TEXT,
            command=self.change_unit
        )

        self.unit_switch.set("°C")

        self.unit_switch.pack(
            side="left",
            padx=6
        )


        self.refresh_button = ctk.CTkButton(
            controls,
            text="↻  Refresh",
            width=130,
            height=42,
            corner_radius=14,
            font=("Segoe UI", 13, "bold"),
            fg_color=CARD,
            hover_color="#E2E8F0",
            text_color=TEXT,
            border_width=1,
            border_color=BORDER,
            command=self.refresh_weather
        )

        self.refresh_button.pack(
            side="left",
            padx=6
        )


        self.loading_label = ctk.CTkLabel(
            controls,
            text="",
            font=("Segoe UI", 12),
            text_color="#CBD5E1"
        )

        self.loading_label.pack(
            side="left",
            padx=10
        )


        self.progress = ctk.CTkProgressBar(
            controls,
            width=110,
            height=7,
            mode="indeterminate"
        )

        self.progress.pack(
            side="left"
        )

        self.progress.set(0)


        # ====================================================
        # LOCATION
        # ====================================================

        self.location_label = ctk.CTkLabel(
            self.container,
            text="●  Pune, IN",
            font=("Segoe UI", 20, "bold"),
            text_color=WHITE
        )

        self.location_label.grid(
            row=4,
            column=0,
            pady=(0, 18)
        )


        # ====================================================
        # MAIN WEATHER CARD
        # ====================================================

        self.weather_card = ctk.CTkFrame(
            self.container,
            fg_color=CARD,
            corner_radius=25,
            border_width=1,
            border_color=BORDER
        )

        self.weather_card.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=40,
            pady=(0, 20)
        )

        self.weather_card.grid_columnconfigure(
            0,
            weight=1
        )

        self.weather_card.grid_columnconfigure(
            1,
            weight=1
        )

        self.weather_card.grid_columnconfigure(
            2,
            weight=1
        )


        # Weather icon

        self.weather_icon = ctk.CTkLabel(
            self.weather_card,
            text="☁️",
            font=("Segoe UI Emoji", 75)
        )

        self.weather_icon.grid(
            row=0,
            column=0,
            rowspan=3,
            padx=40,
            pady=35
        )


        # Temperature

        self.temperature_label = ctk.CTkLabel(
            self.weather_card,
            text="--°C",
            font=("Segoe UI", 58, "bold"),
            text_color=BLUE
        )

        self.temperature_label.grid(
            row=0,
            column=1,
            sticky="w",
            pady=(30, 0)
        )


        # Condition

        self.condition_label = ctk.CTkLabel(
            self.weather_card,
            text="Loading weather...",
            font=("Segoe UI", 19, "bold"),
            text_color=TEXT
        )

        self.condition_label.grid(
            row=1,
            column=1,
            sticky="w"
        )


        # Feels like

        self.feels_label = ctk.CTkLabel(
            self.weather_card,
            text="Feels like --°C",
            font=("Segoe UI", 13),
            text_color=MUTED
        )

        self.feels_label.grid(
            row=2,
            column=1,
            sticky="w",
            pady=(0, 35)
        )


        # Details

        details = ctk.CTkFrame(
            self.weather_card,
            fg_color="transparent"
        )

        details.grid(
            row=0,
            column=2,
            rowspan=3,
            sticky="nsew",
            padx=35,
            pady=30
        )


        self.wind_value = self.create_detail(
            details,
            "💨",
            "Wind"
        )

        self.humidity_value = self.create_detail(
            details,
            "💧",
            "Humidity"
        )

        self.pressure_value = self.create_detail(
            details,
            "◉",
            "Pressure"
        )

        self.visibility_value = self.create_detail(
            details,
            "◎",
            "Visibility"
        )


        # ====================================================
        # STATISTICS
        # ====================================================

        self.stats = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.stats.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=40,
            pady=(0, 20)
        )

        for i in range(4):
            self.stats.grid_columnconfigure(
                i,
                weight=1
            )


        self.max_value = self.create_stat(
            self.stats,
            "🌡️",
            "Max Temperature",
            "--°C",
            0
        )

        self.min_value = self.create_stat(
            self.stats,
            "🌡️",
            "Min Temperature",
            "--°C",
            1
        )

        self.humidity_stat = self.create_stat(
            self.stats,
            "💧",
            "Humidity",
            "--%",
            2
        )

        self.wind_stat = self.create_stat(
            self.stats,
            "💨",
            "Wind Speed",
            "-- m/s",
            3
        )


        # ====================================================
        # FORECAST
        # ====================================================

        self.forecast_card = ctk.CTkFrame(
            self.container,
            fg_color=CARD,
            corner_radius=25,
            border_width=1,
            border_color=BORDER
        )

        self.forecast_card.grid(
            row=7,
            column=0,
            sticky="ew",
            padx=40,
            pady=(0, 20)
        )

        self.forecast_card.grid_columnconfigure(
            0,
            weight=1
        )


        ctk.CTkLabel(
            self.forecast_card,
            text="📅  5-Day Forecast",
            font=("Segoe UI", 22, "bold"),
            text_color=TEXT
        ).grid(
            row=0,
            column=0,
            pady=(22, 18)
        )


        self.forecast_frame = ctk.CTkFrame(
            self.forecast_card,
            fg_color="transparent"
        )

        self.forecast_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 25)
        )


        for i in range(5):
            self.forecast_frame.grid_columnconfigure(
                i,
                weight=1
            )


        # ====================================================
        # STATUS
        # ====================================================

        self.status_label = ctk.CTkLabel(
            self.container,
            text="Ready",
            font=("Segoe UI", 12),
            text_color="#CBD5E1"
        )

        self.status_label.grid(
            row=8,
            column=0,
            pady=(0, 25)
        )


    # ========================================================
    # HEADER CARD
    # ========================================================

    def small_header_card(
        self,
        parent,
        title,
        value,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            width=215,
            height=75,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color=BORDER
        )

        card.grid(
            row=0,
            column=column,
            rowspan=2,
            padx=6
        )

        card.grid_propagate(False)


        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 10, "bold"),
            text_color=MUTED
        ).pack(
            anchor="w",
            padx=18,
            pady=(12, 0)
        )


        label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 12, "bold"),
            text_color=TEXT
        )

        label.pack(
            anchor="w",
            padx=18
        )

        return label


    # ========================================================
    # DETAIL
    # ========================================================

    def create_detail(
        self,
        parent,
        icon,
        title
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            pady=7
        )


        ctk.CTkLabel(
            row,
            text=icon,
            font=("Segoe UI Emoji", 14)
        ).pack(
            side="left",
            padx=(0, 8)
        )


        ctk.CTkLabel(
            row,
            text=title,
            font=("Segoe UI", 12),
            text_color=MUTED
        ).pack(
            side="left"
        )


        value = ctk.CTkLabel(
            row,
            text="--",
            font=("Segoe UI", 12, "bold"),
            text_color=TEXT
        )

        value.pack(
            side="right"
        )

        return value


    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat(
        self,
        parent,
        icon,
        title,
        value,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color=BORDER
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=5
        )


        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 25)
        ).pack(
            side="left",
            padx=(15, 10),
            pady=17
        )


        text = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        text.pack(
            side="left",
            fill="both",
            expand=True,
            pady=12
        )


        ctk.CTkLabel(
            text,
            text=title,
            font=("Segoe UI", 10),
            text_color=MUTED
        ).pack(
            anchor="w"
        )


        value_label = ctk.CTkLabel(
            text,
            text=value,
            font=("Segoe UI", 19, "bold"),
            text_color=BLUE
        )

        value_label.pack(
            anchor="w"
        )


        ctk.CTkLabel(
            text,
            text="Today",
            font=("Segoe UI", 9),
            text_color=MUTED
        ).pack(
            anchor="w"
        )


        return value_label


    # ========================================================
    # CLOCK
    # ========================================================

    def update_clock(self):

        now = datetime.now()

        self.date_card.configure(
            text=now.strftime(
                "%A, %d %B %Y"
            )
        )

        self.time_card.configure(
            text=now.strftime(
                "%I:%M:%S %p"
            )
        )

        self.after(
            1000,
            self.update_clock
        )


    # ========================================================
    # SEARCH WEATHER
    # ========================================================

    def search_weather(self):

        city = self.city_entry.get().strip()

        if not city:

            self.status_label.configure(
                text="⚠ Please enter a city name.",
                text_color="#FCA5A5"
            )

            return


        if API_KEY == "YOUR_NEW_API_KEY":

            self.status_label.configure(
                text="⚠ Add your OpenWeatherMap API key first.",
                text_color="#FCA5A5"
            )

            return


        if self.loading:
            return


        self.start_loading()


        threading.Thread(
            target=self.fetch_weather,
            args=(city,),
            daemon=True
        ).start()


    # ========================================================
    # REFRESH
    # ========================================================

    def refresh_weather(self):

        if not self.loading:
            self.search_weather()


    # ========================================================
    # LOADING
    # ========================================================

    def start_loading(self):

        self.loading = True

        self.search_button.configure(
            state="disabled",
            text="Loading..."
        )

        self.refresh_button.configure(
            state="disabled"
        )

        self.unit_switch.configure(
            state="disabled"
        )

        self.loading_label.configure(
            text="Fetching weather..."
        )

        self.status_label.configure(
            text="Updating weather...",
            text_color="#CBD5E1"
        )

        self.progress.start()


    def stop_loading(self):

        self.loading = False

        self.search_button.configure(
            state="normal",
            text="🔍  Search"
        )

        self.refresh_button.configure(
            state="normal"
        )

        self.unit_switch.configure(
            state="normal"
        )

        self.loading_label.configure(
            text=""
        )

        self.progress.stop()


    # ========================================================
    # API
    # ========================================================

    def fetch_weather(self, city):

        try:

            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }


            # Current weather

            response = requests.get(
                BASE_URL,
                params=params,
                timeout=5
            )


            if response.status_code == 404:

                raise Exception(
                    "City not found. Check the spelling."
                )


            if response.status_code == 401:

                raise Exception(
                    "Invalid API key."
                )


            if response.status_code != 200:

                raise Exception(
                    f"Weather service error: {response.status_code}"
                )


            weather = response.json()


            # Forecast

            forecast_response = requests.get(
                FORECAST_URL,
                params=params,
                timeout=5
            )


            if forecast_response.status_code != 200:

                raise Exception(
                    "Unable to load forecast."
                )


            forecast = forecast_response.json()


            self.after(
                0,
                lambda: self.update_weather(
                    weather,
                    forecast
                )
            )


        except requests.exceptions.Timeout:

            self.after(
                0,
                lambda: self.show_error(
                    "Request timed out. Check your internet."
                )
            )


        except requests.exceptions.ConnectionError:

            self.after(
                0,
                lambda: self.show_error(
                    "No internet connection."
                )
            )


        except Exception as error:

            message = str(error)

            self.after(
                0,
                lambda: self.show_error(
                    message
                )
            )


    # ========================================================
    # UPDATE WEATHER
    # ========================================================

    def update_weather(
        self,
        weather,
        forecast
    ):

        self.current_data = weather
        self.forecast_data = forecast


        city = weather["name"]
        country = weather["sys"]["country"]


        self.location_label.configure(
            text=f"●  {city}, {country}"
        )


        # Temperature

        self.update_temperature()


        # Condition

        condition = weather[
            "weather"
        ][0][
            "description"
        ].title()


        self.condition_label.configure(
            text=condition
        )


        # Icon

        weather_id = weather[
            "weather"
        ][0][
            "id"
        ]


        self.weather_icon.configure(
            text=self.get_icon(weather_id)
        )


        # Details

        wind = weather[
            "wind"
        ].get(
            "speed",
            0
        )

        humidity = weather[
            "main"
        ].get(
            "humidity",
            0
        )

        pressure = weather[
            "main"
        ].get(
            "pressure",
            0
        )

        visibility = weather.get(
            "visibility",
            0
        ) / 1000


        self.wind_value.configure(
            text=f"{wind:.1f} m/s"
        )

        self.humidity_value.configure(
            text=f"{humidity}%"
        )

        self.pressure_value.configure(
            text=f"{pressure} hPa"
        )

        self.visibility_value.configure(
            text=f"{visibility:.1f} km"
        )


        # Statistics

        self.update_statistics()


        # Forecast

        self.create_forecast()


        self.status_label.configure(
            text="✓ Weather updated successfully",
            text_color="#BBF7D0"
        )


        self.stop_loading()


    # ========================================================
    # TEMPERATURE
    # ========================================================

    def update_temperature(self):

        if not self.current_data:
            return


        main = self.current_data["main"]


        temperature = main["temp"]

        feels = main["feels_like"]


        if self.unit == "F":

            temperature = self.to_fahrenheit(
                temperature
            )

            feels = self.to_fahrenheit(
                feels
            )

            symbol = "°F"

        else:

            symbol = "°C"


        self.temperature_label.configure(
            text=f"{round(temperature)}{symbol}"
        )


        self.feels_label.configure(
            text=f"Feels like {round(feels)}{symbol}"
        )


    # ========================================================
    # STATISTICS
    # ========================================================

    def update_statistics(self):

        if not self.current_data:
            return


        main = self.current_data["main"]


        maximum = main["temp_max"]
        minimum = main["temp_min"]


        if self.unit == "F":

            maximum = self.to_fahrenheit(
                maximum
            )

            minimum = self.to_fahrenheit(
                minimum
            )

            symbol = "°F"

        else:

            symbol = "°C"


        self.max_value.configure(
            text=f"{round(maximum)}{symbol}"
        )

        self.min_value.configure(
            text=f"{round(minimum)}{symbol}"
        )


        self.humidity_stat.configure(
            text=f"{main['humidity']}%"
        )


        wind = self.current_data[
            "wind"
        ].get(
            "speed",
            0
        )


        self.wind_stat.configure(
            text=f"{wind:.1f} m/s"
        )


    # ========================================================
    # UNIT CONVERSION
    # ========================================================

    def change_unit(self, selected):

        if selected == "°F":

            self.unit = "F"

        else:

            self.unit = "C"


        self.update_temperature()
        self.update_statistics()
        self.create_forecast()


    def to_fahrenheit(self, celsius):

        return (
            celsius * 9 / 5
        ) + 32


    # ========================================================
    # FORECAST
    # ========================================================

    def create_forecast(self):

        if not self.forecast_data:
            return


        # Remove previous cards

        for widget in self.forecast_frame.winfo_children():

            widget.destroy()


        entries = self.forecast_data[
            "list"
        ]


        daily = {}


        for item in entries:

            date = datetime.fromtimestamp(
                item["dt"]
            ).date()


            if date not in daily:

                daily[date] = item


        days = list(
            daily.values()
        )[:5]


        for index, item in enumerate(days):

            date = datetime.fromtimestamp(
                item["dt"]
            )


            day = date.strftime("%a")

            date_text = date.strftime(
                "%d %b"
            )


            temperature = item[
                "main"
            ][
                "temp"
            ]


            if self.unit == "F":

                temperature = self.to_fahrenheit(
                    temperature
                )

                symbol = "°F"

            else:

                symbol = "°C"


            temperature = round(
                temperature
            )


            icon = self.get_icon(
                item[
                    "weather"
                ][0][
                    "id"
                ]
            )


            condition = item[
                "weather"
            ][0][
                "description"
            ].title()


            card = ctk.CTkFrame(
                self.forecast_frame,
                fg_color=CARD_SOFT,
                corner_radius=18,
                border_width=1,
                border_color=BORDER
            )


            card.grid(
                row=0,
                column=index,
                sticky="nsew",
                padx=5
            )


            ctk.CTkLabel(
                card,
                text=day,
                font=("Segoe UI", 15, "bold"),
                text_color=TEXT
            ).pack(
                pady=(18, 2)
            )


            ctk.CTkLabel(
                card,
                text=date_text,
                font=("Segoe UI", 10),
                text_color=MUTED
            ).pack()


            ctk.CTkLabel(
                card,
                text=icon,
                font=("Segoe UI Emoji", 35)
            ).pack(
                pady=10
            )


            ctk.CTkLabel(
                card,
                text=f"{temperature}{symbol}",
                font=("Segoe UI", 21, "bold"),
                text_color=BLUE
            ).pack()


            ctk.CTkLabel(
                card,
                text=condition,
                font=("Segoe UI", 10),
                text_color=MUTED,
                wraplength=110
            ).pack(
                pady=(3, 18)
            )


    # ========================================================
    # WEATHER ICONS
    # ========================================================

    def get_icon(self, weather_id):

        if weather_id == 800:
            return "☀️"

        if weather_id in [801, 802]:
            return "🌤️"

        if weather_id == 803:
            return "🌥️"

        if weather_id == 804:
            return "☁️"

        if 200 <= weather_id <= 232:
            return "⛈️"

        if 300 <= weather_id <= 321:
            return "🌦️"

        if 500 <= weather_id <= 531:
            return "🌧️"

        if 600 <= weather_id <= 622:
            return "❄️"

        if 700 <= weather_id <= 781:
            return "🌫️"

        return "🌤️"


    # ========================================================
    # ERROR
    # ========================================================

    def show_error(self, message):

        self.stop_loading()

        self.status_label.configure(
            text=f"⚠ {message}",
            text_color="#FECACA"
        )


# ============================================================
# START APP
# ============================================================

if __name__ == "__main__":

    app = WeatherApp()

    app.mainloop()