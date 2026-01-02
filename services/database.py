import sqlite3;

class DatabaseClient:
    def __init__(self):
        self.conn = sqlite3.connect("cine_metrics.db")

    def init_db(self):
        cursor = self.conn.cursor()

        create_table_SQL = """
        CREATE TABLE IF NOT EXISTS SERIES(
            ID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            synopsis TEXT,
            vote_average REAL
        );
        """
        cursor.execute(create_table_SQL)
        self.conn.commit()
        print("Database initiated successfully")

    def add_series(self, series_data):
        cursor = self.conn.cursor()

        insert_sql = """
        INSERT OR IGNORE INTO SERIES (ID,name,synopsis,vote_average)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_sql, (
            series_data['id'],
            series_data['name'],
            series_data['overview'],
            series_data['vote_average']
        ))

        self.conn.commit()
        print(f"Series '{series_data['name']}' saved/updated in database")

    def get_all_series(self):
        """
        Busca todas as séries salvas no banco e retorna uma lista de tuplas.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, vote_average FROM SERIES")
        return cursor.fetchall()