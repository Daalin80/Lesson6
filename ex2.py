print("What time is now?")
def countdown(func):
    import time
    def seconds():
            time.sleep(1)
            print(3)
            time.sleep(2)
            print(2)
            time.sleep(3)
            print(1)
            func()
    return seconds

@countdown
def time_now():
    import time
    print(time.strftime("%H:%M", time.localtime()))
time_now()
