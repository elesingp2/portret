-- Создание таблицы отчетов
CREATE TABLE reports (
    widget_id INT REFERENCES widgets(widget_id),
    reports_id SERIAL PRIMARY KEY,
    create_dttm TIMESTAMP NOT NULL,
    filepath JSON,
    period_flag BOOLEAN,
    report_text JSON
);
