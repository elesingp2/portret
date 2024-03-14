import psycopg2


import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, user, host, password):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.conn = None
        # Define a mapping of tables to their primary key columns
        self.primary_keys = {
            'users': 'user_id',
            'widgets': 'widget_id',
            'reports': 'reports_id',
            'threads': 'thread_id',
            'sources': 'id'
        }

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password
            )

    def insert(self, table_name, data_dict):
        primary_key = self.primary_keys.get(table_name)
        if not primary_key:
            raise ValueError(f"Primary key for table {table_name} is not defined.")
            
        self.connect()
        with self.conn.cursor() as cur:
            columns = data_dict.keys()
            values = data_dict.values()
            placeholders = sql.SQL(', ').join(sql.Placeholder() for _ in values)
            insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING {};").format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(map(sql.Identifier, columns)),
                placeholders,
                sql.Identifier(primary_key) 
            )
            cur.execute(insert_query, tuple(values))
            self.conn.commit()
            return cur.fetchone()[0]  # Returns the primary key of the inserted row

    def select(self, table_name, columns="*", conditions=None):
        self.connect()
        with self.conn.cursor() as cur:
            # Build the base query
            query = sql.SQL("SELECT {} FROM {}").format(
                sql.SQL(columns) if isinstance(columns, str) else columns,
                sql.Identifier(table_name),
            )

            # Append conditions if they exist
            if conditions:
                query = query + sql.SQL(" ") + conditions

            # Execute the complete query
            cur.execute(query)
            return cur.fetchall()


    def update(self, table_name, data_dict, conditions):
        self.connect()
        with self.conn.cursor() as cur:
            update_data = sql.SQL(", ").join(
                sql.Identifier(k) + sql.SQL(" = ") + sql.Placeholder()
                for k in data_dict
            )
            update_query = sql.SQL("UPDATE {} SET {} WHERE {};").format(
                sql.Identifier(table_name),
                update_data,
                sql.SQL(conditions)
            )
            cur.execute(update_query, tuple(data_dict.values()))
            self.conn.commit()

    def view_all(self, table_name):
        """View all contents of a specified table."""
        self.connect()
        with self.conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            return rows

    def delete(self, table_name, conditions=None):
        """Delete records from a specified table based on conditions. Use with caution!"""
        self.connect()
        with self.conn.cursor() as cur:
            query = sql.SQL("DELETE FROM {} ").format(sql.Identifier(table_name))
            if conditions:
                query += sql.SQL("WHERE ") + conditions
            cur.execute(query)
            self.conn.commit()
            print(f"Records have been deleted from {table_name}.")


    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def run_table(self, table_name, data_dict, primary_condition=None):
        self.connect()
        primary_key = self.primary_keys.get(table_name)
        if not primary_key:
            raise ValueError(f"No primary key is defined for table {table_name}.")
            
        inserted_id = self.insert(table_name, data_dict)
        print(f"Inserted row ID in {table_name}: {inserted_id}")
        
        # Correctly construct the WHERE condition using psycopg2.sql.SQL
        condition = sql.SQL("WHERE {} = {}").format(sql.Identifier(primary_key), sql.Literal(inserted_id))
        
        row = self.select(table_name, "*", condition)
        print(f"Retrieved row from {table_name}: {row}")

        self.view_all(table_name)
        self.close()
        return row


