def countdown(func):
    import time
    def time_now():
            print("What time is now?")
            func()
            print(time.strftime("%H:%M", time.localtime()))
    return time_now

@countdown
def seconds():
    import time
    time.sleep(1)
    print(3)
    time.sleep(2)
    print(2)
    time.sleep(3)
    print(1)
seconds()
