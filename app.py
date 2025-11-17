import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_excel('passenger_data.xlsx')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    return df

df = load_data()

# Настройки темы и фона
st.sidebar.header("Настройки")
theme = st.sidebar.selectbox("Тема", ["Светлая", "Темная"], index=0)

# Фон и тема
if theme == "Светлая":
    bg_color = "rgba(255, 255, 255, 0.8)"
    text_color = "#000000"
else:
    bg_color = "rgba(0, 0, 0, 0.7)"
    text_color = "#ffffff"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("assets/AirPlane.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: {bg_color};
        z-index: -1;
    }}
    .stMarkdown, .stText, .stHeader {{
        color: {text_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Заголовок
st.title("🛫 Анализ пассажиропотока в аэропорту")
st.markdown("Интерактивный дашборд для анализа данных о пассажирах.")

# Боковая панель для фильтров
st.sidebar.header("Фильтры")

# Фильтр по дате
date_range = st.sidebar.date_input("Выберите диапазон дат", [df['Date'].min(), df['Date'].max()])
start_date, end_date = date_range

# Фильтр по направлению
directions = df['Direction'].unique()
selected_directions = st.sidebar.multiselect("Направления", directions, default=directions)

# Фильтр по авиакомпании
airlines = df['Airline'].unique()
selected_airlines = st.sidebar.multiselect("Авиакомпании", airlines, default=airlines)

# Фильтр по терминалу
terminals = df['Terminal'].unique()
selected_terminals = st.sidebar.multiselect("Терминалы", terminals, default=terminals)

# Применение фильтров
filtered_df = df[
    (df['Date'] >= pd.to_datetime(start_date)) &
    (df['Date'] <= pd.to_datetime(end_date)) &
    (df['Direction'].isin(selected_directions)) &
    (df['Airline'].isin(selected_airlines)) &
    (df['Terminal'].isin(selected_terminals))
]

# Вариации таблиц
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Обычная таблица", "Фильтрованная таблица", "Стилизованная таблица", "Сводная таблица", "Графики"])

with tab1:
    st.header("Обычная таблица данных")
    st.dataframe(df.head(100))  # Показать первые 100 строк

with tab2:
    st.header("Фильтрованная таблица")
    st.dataframe(filtered_df.head(100))

with tab3:
    st.header("Стилизованная таблица")
    # Стилизация с помощью CSS
    st.markdown("""
    <style>
    .dataframe th {
        background-color: #f0f0f0;
        color: black;
        font-weight: bold;
    }
    .dataframe td {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    st.dataframe(filtered_df.head(100))

with tab4:
    st.header("Сводная таблица")
    # Сводная таблица: среднее время обработки по терминалу и направлению
    pivot_df = filtered_df.pivot_table(values='Processing_Time_Min', index='Terminal', columns='Direction', aggfunc='mean')
    st.dataframe(pivot_df)

with tab5:
    st.header("Графики и визуализации")

    # График пассажиропотока по дням
    daily_passengers = filtered_df.groupby('Date')['Passengers'].sum().reset_index()
    fig1 = px.line(daily_passengers, x='Date', y='Passengers', title='Пассажиропоток по дням')
    st.plotly_chart(fig1)

    # Тепловая карта по часам и дням недели
    temp_df = filtered_df.copy()
    temp_df['Hour'] = pd.to_datetime(temp_df['Time'], format='%H:%M:%S').dt.hour
    temp_df['Weekday'] = temp_df['Date'].dt.day_name()
    heatmap_data = temp_df.pivot_table(values='Passengers', index='Weekday', columns='Hour', aggfunc='sum')
    fig2 = go.Figure(data=go.Heatmap(z=heatmap_data.values, x=heatmap_data.columns, y=heatmap_data.index, colorscale='Viridis'))
    fig2.update_layout(title='Тепловая карта пассажиропотока по часам и дням недели')
    st.plotly_chart(fig2)

    # Гистограмма по авиакомпаниям
    airline_passengers = filtered_df.groupby('Airline')['Passengers'].sum().reset_index()
    fig3 = px.bar(airline_passengers, x='Airline', y='Passengers', title='Пассажиры по авиакомпаниям')
    st.plotly_chart(fig3)

# Экспорт в Excel
if st.button("Экспорт отфильтрованных данных в Excel"):
    filtered_df.to_excel('filtered_passenger_data.xlsx', index=False)
    st.success("Данные экспортированы в filtered_passenger_data.xlsx")