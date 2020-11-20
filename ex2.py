import time
def countdown(func):
    def seconds():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func()
    return seconds

@countdown
def time_now():
    print(time.strftime("%H:%M", time.localtime()))
print("What time is now?")
time_now()