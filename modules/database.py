import sqlite3
import os
import pathlib


class DatabaseHandler():
    _connection = None
    _cursor = None

    def __init__( self, db: str ):
        if not os.path.exists( db ):
            raise Exception( f"Database '{db}' does not exist." )

        db_path = pathlib.Path( db )

        if db_path.suffix != '.db':
            raise Exception( f"Database '{db}' does not have the correct extension." )

        self._connection = sqlite3.connect( f'{db}' )
        self._cursor = self.connection.cursor()

    def __del__( self ):
        self._cursor.close()
        self._connection.close()

    def execute_query( self, query: str ) -> []:
        self._cursor.execute( query )
        data = self._cursor.fetchall()
        return data