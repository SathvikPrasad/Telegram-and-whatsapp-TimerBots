
import pyautogui
import time
import datetime


def auto_2(name, msg, count):
    pyautogui.click(0, 1073)
    time.sleep(2)
    pyautogui.typewrite('telegram')
    pyautogui.typewrite(['enter'])
    time.sleep(3)
    pyautogui.typewrite(name)
    pyautogui.typewrite(['enter'])
    time.sleep(1)
    for mesage in range(count):
        pyautogui.typewrite(msg)
        pyautogui.typewrite(['enter'])
        time.sleep(1)


def Timer_bot(timer, name, msg, count):

    tt = 2

    while tt == 2:
        time_1 = datetime.datetime.now()
        local_hour = time_1.hour
        if local_hour == timer:
            auto_2(name, msg, count)
            tt += 1
        else:
            pass


# Timer_bot(24 hour format, name of the contact, message, count)

Timer_bot(12, 'pc', 'happy birthday', 5)
