import requests
from customtkinter import *

root2=CTk()
root2.title('Weather Forecast')
root2.geometry('350x300')

frame2=CTkFrame(root2)
frame2.pack(pady=20, padx=20, fill='both', expand=True)

def start():
    root2.withdraw()
    root = CTk()
    root.title('Weather Forecast')
    root.geometry('500x350')

    frame = CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    label8 = CTkLabel(master=frame, text='Predict Weather', font=('Arial', 50), text_color='#00FF41')
    label8.place(x=65, y=16)

    entry = CTkEntry(frame, placeholder_text='Enter City')
    entry.place(x=155, y=130)

    def get():
        root1 = CTk()
        root1.title('Weather Forecast')
        root1.geometry('500x400')
        root.withdraw()

        frame1 = CTkFrame(master=root1)
        frame1.pack(pady=20, padx=20, fill='both', expand=True)

        BASE_URL = 'https://api.weatherbit.io/v2.0/current'
        API_KEY = '5d30936130e54181a58ae9b9c64e963d'

        # User input for city name or zip code
        location = entry.get()

        # Query parameters
        params = {
            'city': location,
            'key': API_KEY,
            'include': 'minutely'  # Include minutely forecast
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()

            current_observation = weather_data['data'][0]

            label1 = CTkLabel(frame1, text=f'{entry.get()}', font=('TkFixedFont', 50), text_color='#00FF41')
            label1.place(x=140, y=16)

            label2 = CTkLabel(frame1, text="Weather in {city_name}, {state_code}, {country_code}:"
                              .format(**current_observation), font=('TkFixedFont', 20))
            label2.place(x=100, y=90)

            label3 = CTkLabel(frame1, text=f"Temperature: {current_observation['temp']}°C", font=('TkFixedFont', 20))
            label3.place(x=100, y=130)

            label4 = CTkLabel(frame1, text=f"Humidity: {current_observation['rh']}%", font=('TkFixedFont', 20))
            label4.place(x=100, y=170)

            label5 = CTkLabel(frame1, text=f"Wind Speed: {current_observation['wind_spd']} m/s",
                              font=('TkFixedFont', 20))
            label5.place(x=100, y=210)

            label6 = CTkLabel(frame1, text=f"Description: {current_observation['weather']['description']}",
                              font=('TkFixedFont', 20))
            label6.place(x=100, y=250)

            def start1():
                root1.withdraw()
                start()

            button2 = CTkButton(frame1, text='Go Back', text_color='red', command=start1)
            button2.place(x=165, y=300)

            entry.delete(0, 'end')

            if 'minutely' in weather_data:
                minutely_forecast = weather_data['minutely']
                print("Minutely Forecast:")
                for forecast in minutely_forecast:
                    print(f"Time: {forecast['timestamp_local']}, Precipitation: {forecast['precip']} mm/hr")
        else:
            label9 = CTkLabel(frame1, text='Error! Incorrect City Name or Zip Code',font=('Arial',20), text_color='Red')
            label9.place(x=100, y=170)

            def start2():
                root1.withdraw()
                start()

            button2 = CTkButton(frame1, text='Go Back', text_color='red', command=start2)
            button2.place(x=165, y=300)

            entry.delete(0, 'end')
        root1.mainloop()

    button = CTkButton(frame, text='Retrieve Weather', command=get)
    button.place(x=155, y=190)

    root.mainloop()


button3=CTkButton(frame2,text='Start',command=start)
button3.place(x=90, y=150)

label = CTkLabel(master=frame2, text='Weather Forecast', font=('Times',40), text_color='#00FF41')
label.place(x=20, y=16)

root2.mainloop()

