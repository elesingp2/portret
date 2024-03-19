# Установка PostgreSQL
conda install -y -c conda-forge postgresql


# Инициализация и запуск сервера PostgreSQL(не забудь изменить конфиг - db_config!!)
initdb -D db
pg_ctl -D db -l logfile start
createdb db

#заход в бд
psql -U codespace -d db

# Создание таблиц(пример)
#\i /workspaces/portret/PortretAI/database/tables/reports.sql
# \q выйти из psql
