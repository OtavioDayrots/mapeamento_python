import pyodbc

def conectar():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'
        'DATABASE=Geoprocessamento;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
