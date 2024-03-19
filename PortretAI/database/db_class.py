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
                sql.SQL(columns) if isinstance(columns, str) else sql.SQL(", ").join(map(sql.Identifier, columns.split(","))),
                sql.Identifier(table_name),
            )

            # Append conditions if they exist, ensuring they are properly formatted
            if conditions:
                query = query + sql.SQL(" ") + sql.SQL(conditions)

            # Execute the complete query
            cur.execute(query)
            return cur.fetchall()



    def update(self, table_name, data_dict, conditions, condition_values=None):
        self.connect()
        with self.conn.cursor() as cur:
            # Dynamically building the part of the SET clause based on data_dict keys and values
            update_data = sql.SQL(", ").join(
                sql.Identifier(k) + sql.SQL(" = ") + sql.Placeholder()
                for k in data_dict.keys()
            )
            # Constructing the full UPDATE statement with safe placeholders for table name and conditions
            update_query = sql.SQL("UPDATE {} SET {} {}").format(
                sql.Identifier(table_name),
                update_data,
                sql.SQL(conditions)
            )
            # Concatenating all values that will be substituted into the placeholders
            all_values = list(data_dict.values()) + list(condition_values if condition_values else [])
            cur.execute(update_query, all_values)
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

    def run_table(self, method, table_name, data_dict=None, conditions=None, return_columns="*"):
        self.connect()
        primary_key = self.primary_keys.get(table_name)
        if not primary_key:
            raise ValueError(f"No primary key is defined for table {table_name}.")
            
        if method.lower() == 'insert':
            inserted_id = self.insert(table_name, data_dict)
            print(f"Inserted row ID in {table_name}: {inserted_id}")
            returned_row = inserted_id
        
        elif method.lower() == 'select':
            return self.select(table_name, return_columns, conditions)
        
        elif method.lower() == 'update':
            if data_dict is None or conditions is None:
                raise ValueError("Data dictionary and conditions must be provided for update operations.")
            self.update(table_name, data_dict, conditions)

        elif method.lower() == 'delete':
            if conditions is None:
                raise ValueError("Conditions must be provided for delete operations.")
            self.delete(table_name, conditions)

        else:
            raise ValueError(f"Unknown method '{method}'.")
        
        # Correctly construct the WHERE condition using psycopg2.sql.SQL
        #condition = sql.SQL("WHERE {} = {}").format(sql.Identifier(primary_key), sql.Literal(inserted_id))
        
        returned_row = self.select(table_name, "*", conditions)
        #print(f"Retrieved row from {table_name}: {returned_row}")

        #self.view_all(table_name)
        self.close()
        return returned_row


