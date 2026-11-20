import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

required_settings = [
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
    "DB_SSLROOTCERT",
]

missing = [
    name for name in required_settings
    if not os.getenv(name)
]

if missing:
    raise RuntimeError(
        f"Missing database configuration: {', '.join(missing)}"
    )

database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)

engine = create_engine(
    database_url,
    connect_args={
        "sslmode": os.getenv("DB_SSLMODE", "verify-full"),
        "sslrootcert": os.environ["DB_SSLROOTCERT"],
    },
    pool_pre_ping=True,
    pool_size=2,
    max_overflow=3,
    pool_timeout=10,
)


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text(
                """
                SELECT
                    current_database() AS database_name,
                    current_user AS database_user,
                    inet_server_addr() AS server_address,
                    version() AS database_version
                """
            )
        )

        return result.mappings().one()
