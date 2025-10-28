from psycopg2 import connect
from environs import Env

env = Env()
env.read_env()

def get_connect():
    return connect(
        user = env.str("DB_USER"),
        database = env.str("DATABASE"),
        host = env.str("HOST"),
        port = env.str("PORT"),
        password = env.str("PASSWORD")
    )

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        username VARCHAR(100),
        chat_id VARCHAR(150) UNIQUE
    );

    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id) ON DELETE CASCADE,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        start_date TIMESTAMP DEFAULT NOW(),
        end_date TIMESTAMP,
        holat VARCHAR(20) DEFAULT 'bajarilmagan'
    );
    """

    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute(sql)
            db.commit()

create_table()


