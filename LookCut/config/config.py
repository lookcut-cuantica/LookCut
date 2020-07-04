import os

class Config:

    def __init__(self):
        self.mysqldb_host = os.getenv("MYSQLDB_HOST")
        self.mysqldb_username = os.getenv("MYSQLDB_USERNAME")
        self.mysqldb_password = os.getenv("MYSQLDB_PASSWORD")
        self.mysqldb_name = os.getenv("MYSQLDB_NAME")
        self.mysqldb_port = os.getenv("MYSQLDB_PORT")