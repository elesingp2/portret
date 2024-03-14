-- Создание таблицы источников
CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    in_use_flag BOOLEAN -- предполагаем, что флаг показывает, используется источник или нет
);