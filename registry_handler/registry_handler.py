from cmd import Cmd
import sqlite3
import winreg


# START CLASS DECLARATIONS

class DatabaseHandle():
    connection = None
    cursor = None

    def __init__( self ):
        self.connection = sqlite3.connect( 'registry_data.db' )
        self.cursor = self.connection.cursor()

    def __del__( self ):
        self.cursor.close()
        self.connection.close()

    def read_from_db( self ) -> []:
        self.cursor.execute( 'SELECT * FROM registry_data' )
        data = self.cursor.fetchall()
        return data


class PromptHandle( Cmd ):
    def do_exit( self ):
        return True

    def do_list( self ):
        # Display all the read valid commands from a database here.
        # This function should be called in this class' constructor, so that the list of commands are automatically shown once the prompt session is loaded.
        pass

# END CLASS DECLARATIONS


# START FUNCTION DECLARATIONS



# END FUNCTION DECLARATIONS


if __name__ == "__main__":
    database_handle = DatabaseHandle()
    registry_data = database_handle.read_from_db()
    # Pass registry_data to a prompt handle instance, where it should be parsed.
    #PromptHandle().cmdloop()