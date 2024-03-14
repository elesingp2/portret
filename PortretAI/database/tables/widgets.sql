-- Создание таблицы виджетов
CREATE TABLE widgets (
    user_id INT REFERENCES users(user_id),
    widget_id SERIAL PRIMARY KEY,
    widget_name VARCHAR(255) NOT NULL,
    key_words TEXT[], 
    sources_id TEXT[],
    schedule_hour INT 
);