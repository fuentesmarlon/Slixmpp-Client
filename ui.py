from bots import *

def starting_menu():
    print("""
    Welcome to the CLient!

    Please choose one of the following options:

        1. Log-in existing account

        2. Register New User

        3. Unregister a User

        4. Quit   
    """)

    answer =input("Choose: ")
    return answer

def user_menu():
    print("""
    Good to have you back!

    Choose one of the following options:
        1. Show Available Users
        
        2.  Contacts   

        3. Show status

        4. Start Talking!

        5. Group Chat!

        6. Check Notifications

        7. Log Out
    """)

    answer=input("Choose: ")

    return answer
def register_user(username,password):
    xmpp = UserCreate(username,password)
    xmpp.register_plugin('xep_0030') 
    xmpp.register_plugin('xep_0004') 
    xmpp.register_plugin('xep_0066') 
    xmpp.register_plugin('xep_0077') 
    xmpp.connect()
    xmpp.process(forever=False)

def delete_user(username,password):
    xmpp = UserDelete(username,password)
    xmpp.register_plugin('xep_0030') 
    xmpp.register_plugin('xep_0004') 
    xmpp.register_plugin('xep_0066') 
    xmpp.register_plugin('xep_0077') 
    xmpp.connect()
    xmpp.process(forever=False)

def login(username,password):
    xmpp = ClientHandler(username,password)
    xmpp.register_plugin('xep_0030') 
    xmpp.register_plugin('xep_0199') 
    xmpp.connect()
    xmpp.process(forever=False)
    result= xmpp.success_login

    return result

def show_available(username,password):
    xmpp = AvailableUsers(username,password)
    xmpp.connect()
    xmpp.process(forever=False)

def add_friend(username,password,friend):
    xmpp = AvailableUsers(username,password)
    xmpp.connect()
    xmpp.send_request(friend)
    xmpp.process(forever=False)
