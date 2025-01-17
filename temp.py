import mysql.connector
import random
import time

def insert_metric(metric_name, value):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="5289",
            database="monitoring"
        )
        cursor = conn.cursor()
        query = "INSERT INTO metrics (metric_name, value) VALUES (%s, %s)"
        cursor.execute(query, (metric_name, value))
        conn.commit()
        print(f"Добавлена метрика: {metric_name}, значение: {value}")
    except mysql.connector.Error as e:
        print(f"Ошибка подключения или выполнения запроса: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

# Генерация случайных данных
while True:
    metric = "temperature"
    value = random.uniform(20.0, 30.0)
    insert_metric(metric, value)
    time.sleep(5)  # Отправка данных каждые 5 секунд
