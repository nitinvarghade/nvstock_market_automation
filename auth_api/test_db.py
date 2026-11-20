from auth_api.database import test_database_connection


if __name__ == "__main__":
    result = test_database_connection()

    print("PostgreSQL connection successful")
    print(f"Database: {result['database_name']}")
    print(f"User: {result['database_user']}")
    print(f"Server IP: {result['server_address']}")
    print(f"Version: {result['database_version']}")
