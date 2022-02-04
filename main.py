from datetime import datetime, timedelta
from time import sleep

from dateutil import parser
from pynput import keyboard
from todoist.api import TodoistAPI
import pync
import threading

api = TodoistAPI('3ecd6c78d4e7a9548a4e4823807850906e8f6650')

notified = []

iterations = 0
global snooze
snooze = False


def silent_notifications():
    global snooze
    if snooze:
        snooze = False
    else:
        snooze = True


def check_shortcuts():
    COMBINATIONS = [
        {keyboard.Key.cmd, keyboard.Key.ctrl, keyboard.KeyCode(char='l')},
        {keyboard.Key.cmd, keyboard.Key.ctrl, keyboard.KeyCode(char='L')}
    ]

    current = set()

    def on_press(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                silent_notifications()

    def on_release(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


t1 = threading.Thread(target=check_shortcuts, name='t1')
t1.start()

# add_hotkey('ctrl+alt+f5', silent_notifications)

while 1:
    iterations += 1
    today = datetime.today()
    day = today.day
    hour = today.hour
    minute = today.minute

    api.sync()

    for item in api.state['items']:
        try:
            due_date = item['due']['date']
            due_date = parser.parse(due_date)

            if due_date.hour == 0:
                due_date = due_date.replace(hour=23, minute=59)

            if (due_date - timedelta(minutes=5)) <= today and not item['checked'] and {item['content'],
                                                                                       item['due'][
                                                                                           'date']} not in notified and not snooze:
                notified.append({item['content'], item['due']['date']})
                pync.notify(f"{item['content']} Task is next.", # Disable notifications with cmd+ctrl+l"
                            title='Todoist Reminders')
                # notification.show_toast(f"{item['content']} Task is next", "Disable notifications with
                # ctrl+alt+f5", duration=10,
                # icon_path=r"C:\Users\JuanD\Desktop\Instant\todosit_remiders\res\todoist_logo.ico")

        except Exception as e:
            pass

    if iterations >= 180:
        notified = []

    sleep(10)
