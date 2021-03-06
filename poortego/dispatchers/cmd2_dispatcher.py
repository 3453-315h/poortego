
"""
TODO List
    - Possibly combine user, storage, and session commands into something simpler like "show"
"""


from cmd2 import make_option, options

#
# Imports for dispatcher supported command set
#
from ..commands.user import poortego_user
from ..commands.env import poortego_env
from ..commands.ls import poortego_ls
from ..commands.cd import poortego_cd
from ..commands.pwd import poortego_pwd
from ..commands.add import poortego_add
from ..commands.ln import poortego_ln
from ..commands.purge import poortego_purge
from ..commands.find import poortego_find
from ..commands.imports import poortego_import

class Cmd2Dispatcher:
    def __init__(self, interface_obj):
        self.my_interface = interface_obj

    #
    # Namespace: poortego
    # Command: user
    # 
    @options([
              make_option('-c', '--change', action="store_true", dest="change_user", help="Change the current user"),
              make_option('-l', '--list', action="store_true", dest="list_details", help="Show the current user details")
              ])
    def do_poortego_user(self, arg, opts):
        """Command to show and change user details"""
        poortego_user(self.my_interface, arg, opts)
        
    #
    # Namespace: poortego
    # Command: env
    #
    @options([
            make_option('-s', '--session', action="store_true", dest="session_details", help="Show the session details"),
            make_option('-d', '--storage', action="store_true", dest="storage_details", help="Show the storage details"),
            make_option('-u', '--user', action="store_true", dest="user_details", help="Show the user details")
        ])
    def do_poortego_env(self, arg, opts):
        """Command to show environment details"""
        poortego_env(self.my_interface, arg, opts)

    #
    # Namespace: poortego
    # Command: ls
    #        
    @options([
            make_option('-a', '--all', action="store_true", dest="all_nodes", help="List all nodes tied to root"),
            make_option('-b', '--bi', action="store_true", help="List nodes connected to/from current node"),
            make_option('-f', '--from', action="store_true", dest="from_nodes", help="List only nodes with link from current node"),
            make_option('-t', '--to', action="store_true", dest="to_nodes", help="List only nodes with link to current node"),    
        ])    
    def do_poortego_ls(self, arg, opts):
        """Command to show node adjacency"""
        poortego_ls(self.my_interface, arg, opts)

    #
    # Namespace: poortego
    # Command: cd
    #
    def do_poortego_cd(self, arg):
        """Command to change current node"""
        poortego_cd(self.my_interface, arg)
        
    #
    # Namespace: poortego
    # Command: pwd
    #    
    def do_poortego_pwd(self, arg):
        """Command to show data for current working node"""
        poortego_pwd(self.my_interface, arg)
    
    #
    # Namespace: poortego
    # Command: add
    #    
    @options([
            make_option('-p', '--prompt', action="store_true", default=True, help="Prompt user for node values"),
            make_option('-t', '--type', type="string", dest="node_type", help="Define the type of thing being added"),
            make_option('-v', '--value', type="string", dest="node_value", help="Define the value of the thing")
        ])
    def do_poortego_add(self, arg, opts=None):
        """Command to add node"""
        # Code moved to .command.add sub-module for easier reading/debugging    
        poortego_add(self.my_interface, arg, opts)

    #
    # Namespace: poortego
    # Command: ln
    #
    @options([
            make_option('-o', '--out', action="store_true", default=True, help="Create out-going link from current node"),
            make_option('-i', '--in', action="store_true", help="Create in-coming link to current node"),
            make_option('-b', '--bi', action="store_true", help="Create bi-directional link to/from current node"),
            make_option('-c', '--current', type="string", help="Specific a different node id to use than the current/working node"),
            make_option('-p', '--prompt', action="store_true", help="Prompt for link values")
        ])                         
    def do_poortego_ln(self, arg, opts):
        """Command to add link"""
        # TODO - also account for link properties
        poortego_ln(self.my_interface, arg, opts)    
    
    #
    # Namespace: poortego
    # Command: purge
    #
    def do_poortego_purge(self, arg):
        """Command to delete EVERYTHING from database"""
        poortego_purge(self.my_interface, arg)

    #
    # Namespace: poortego
    # Command: find
    #
    def do_poortego_find(self, arg):
        """Command to find nodes from database"""
        poortego_find(self.my_interface, arg)
        
    #
    # Namespace: poortego
    # Command: import
    #
    @options([
            make_option('-c', '--csv', action="store_true", help="Import data from CSV file"),
            make_option('-m', '--maltego', action="store_true", help="Import data from Maltego file"),
            make_option('-s', '--stix', action="store_true", help="Import data from STIX file"),
    ])
    def do_poortego_import(self, arg, opt):
        """Command to import data"""
        poortego_import(self.my_interface, arg, opt)
