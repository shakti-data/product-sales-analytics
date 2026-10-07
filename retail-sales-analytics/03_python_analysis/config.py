# Database connection settings used by every notebook in this folder.
# Edit SERVER (and DRIVER if needed) to match your own SQL Server instance.

from urllib.parse import quote_plus


def get_conn_url():
    """Return a SQLAlchemy connection URL for the DataWarehouse database."""
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=.\\SQLEXPRESS;"  # local SQL Server Express instance
        "DATABASE=DataWarehouse;"
        "Trusted_Connection=yes;"  # Windows authentication, no password stored
    )
    return "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string)
