import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    from server.bundle import Application
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

'''
 Thanks to stackoverflow for the progress bar
 https://stackoverflow.com/questions/3160699/python-progress-bar
'''

user = input("Username: ")

while True:
    message = input("Message: ")
    Application.sendMessage(message, user)
    Application.readMessages()
