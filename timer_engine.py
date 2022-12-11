import time


def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        end = " "
        timer = '{:02d}:{:02d}'.format(mins, secs, end)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print('Прокидайся!!!')


t = input("Введіть час в секундах: ")
countdown(int(t))


