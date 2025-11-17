import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Функция для генерации случайных данных
def generate_passenger_data(num_days=30, avg_passengers_per_day=1000):
    data = []
    start_date = datetime(2023, 1, 1)

    airlines = ['Aeroflot', 'S7 Airlines', 'UTair', 'Rossiya Airlines', 'Ural Airlines', 'Pobeda', 'Nordwind Airlines']
    terminals = ['Terminal A', 'Terminal B', 'Terminal C']
    directions = ['Domestic', 'International']

    for day in range(num_days):
        current_date = start_date + timedelta(days=day)
        daily_passengers = int(np.random.normal(avg_passengers_per_day, 200))  # Нормальное распределение

        for hour in range(24):
            for _ in range(random.randint(10, 50)):  # Случайное количество записей в час
                time = current_date.replace(hour=hour, minute=random.randint(0, 59), second=random.randint(0, 59))
                direction = random.choice(directions)
                airline = random.choice(airlines)
                terminal = random.choice(terminals)
                passengers = random.randint(1, 10)  # Количество пассажиров в записи
                processing_time = random.randint(5, 60)  # Время прохождения в минутах

                data.append({
                    'Date': time.date(),
                    'Time': time.time(),
                    'Direction': direction,
                    'Airline': airline,
                    'Terminal': terminal,
                    'Passengers': passengers,
                    'Processing_Time_Min': processing_time
                })

    return pd.DataFrame(data)

# Генерация данных
df = generate_passenger_data(num_days=30, avg_passengers_per_day=1500)

# Сохранение в XLSX
df.to_excel('passenger_data.xlsx', index=False)

print("Данные сохранены в passenger_data.xlsx")