import os
import sys
script_dir = os.path.dirname( os.path.realpath( __file__ ) ) + "/../modules"
sys.path.append( script_dir )
from cmd import Cmd


class PromptHandle( Cmd ):
    def do_exit( self ):
        return True

    def do_list( self ):
        # Display all the read valid commands from a database here.
        # This function should be called in this class' constructor, so that the list of commands are automatically shown once the prompt session is loaded.
        pass


if __name__ == "__main__":
    #PromptHandle().cmdloop()
    