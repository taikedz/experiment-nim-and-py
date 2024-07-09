import os

def do_thing():
    message = os.getenv("MESSAGE", "no message")
    for x in range(5):
        print(f"{message} {x}")

