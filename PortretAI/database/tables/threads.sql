-- Создание таблицы тредов
CREATE TABLE threads (
    report_id INT REFERENCES reports(reports_id),
    thread_id SERIAL PRIMARY KEY,
    create_dttm TIMESTAMP NOT NULL,
    extension_text TEXT,
    thread_text JSON
);