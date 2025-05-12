import sqlite3
from faker import Faker
from datetime import datetime, timedelta
import random

def init_db():
    fake = Faker('ru_RU')  # Русская локализация для ФИО и текста
    topics = ['ЖКХ', 'Благоустройство', 'Образование']
    content_templates = {
        'ЖКХ': ['Проблема с отоплением в квартире', 'Протечка труб в подъезде', 'Отсутствие горячей воды', 'Поломка лифта'],
        'Благоустройство': ['Необходим ремонт дороги', 'Установка детской площадки', 'Обрезка деревьев', 'Уборка мусора'],
        'Образование': ['Вопрос о школьном питании', 'Нехватка учебников', 'Ремонт класса', 'Организация кружков']
    }

    with sqlite3.connect('appeals.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appeals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                topic TEXT NOT NULL,
                content TEXT NOT NULL,
                registration_date DATE NOT NULL
            )
        ''')

        # Проверяем, пуста ли таблица
        if cursor.execute('SELECT COUNT(*) FROM appeals').fetchone()[0] == 0:
            test_data = []
            for topic in topics:
                # Генерируем 10–15 обращений для каждой темы
                for _ in range(random.randint(10, 15)):
                    full_name = fake.name()
                    content = random.choice(content_templates[topic])
                    # Случайная дата в 2024–2025 годах
                    start_date = datetime(2024, 1, 1)
                    random_days = random.randint(0, 365 * 2)  # До конца 2025
                    registration_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
                    test_data.append((full_name, topic, content, registration_date))
            
            cursor.executemany('INSERT INTO appeals (full_name, topic, content, registration_date) VALUES (?, ?, ?, ?)', test_data)
        conn.commit()

if __name__ == '__main__':
    init_db()