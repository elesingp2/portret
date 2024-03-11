CREATE TABLE reports (
    user_id SERIAL PRIMARY KEY,
    widget_id INT UNIQUE NOT NULL,
    widget_name VARCHAR(255) NOT NULL,
    first_report_created_at TIMESTAMP,
    reports_created_at_json JSONB,
    new_report_created_at TIMESTAMP,
    report_count INT
);