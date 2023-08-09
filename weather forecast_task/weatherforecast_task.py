import tkinter as tk
from tkinter import messagebox
import tkinter as requests

def get_weather():
    api_key = '87cf00b9b487444fbf2cad14fe94c409'
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            main_info = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            weather_label.config(text=f"Weather: {main_info}, {description}")
            temperature_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found!")
    except requests.ConnectionError:
        messagebox.showerror("Error", "Please check your internet connection!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
app = tk.Tk()
app.title("Weather Forecast report by viral parmar")
app.geometry("400x300")

# Create GUI elements
city_label = tk.Label(app,fg='white',bg='dark blue', text="Enter City:")
city_label.pack(pady=5)
city_entry = tk.Entry(app)
city_entry.pack(pady=5)

get_weather_button = tk.Button(app, text="Get Weather",fg='white',bg='dark blue',command=get_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(app,fg='blue',bg='black', text="")
weather_label.pack(pady=5)
temperature_label = tk.Label(app,fg='blue',bg='black', text="")
temperature_label.pack(pady=5)
humidity_label = tk.Label(app,fg='blue',bg='black', text="")
humidity_label.pack(pady=5)
wind_speed_label = tk.Label(app,fg='blue',bg='black', text="")
wind_speed_label.pack(pady=5)

# Start the main event loop
app.mainloop()
