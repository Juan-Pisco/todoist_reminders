# Todoist - Reminders feature in Python 🐍

Todoist application has the paid feature for getting reminders everytime the time is close to a scheduled task's time. This python solution makes this paying feature free for users that only want to have this characteristic.

**Note:** This is only working for Mac. Windows will be implemented in future versions

## Features 🍬

This integration has the ability to:
* Show a terminal notification every-time a task is due in 5 minutes
* Enable and disable showing up notifications by using the hotkey &rarr; `cmd + ctrl + l`

## How to install? 📝
1. Clone this repo via `git clone https://github.com/JuanDavidPiscoJaimes/todoist_reminders.git`
2. Install the necessary requirements with `pip install -r requirements.txt` in the terminal located in the project's folder
3. Create a `.env` file following the schema showed in the `example.env` file
4. After the `=` sign, introduce your Todoist API token (Go to the section _What's my Todoist API token_ if necessary)
5. You're ready to go! ✅

## How to run it? 🏃‍♂️
There are 2 alternatives for running the program:
1. Run it via terminal using `python main.py` located in the project's folder
2. Run it via your favourite IDE (Pycharm, Spyder, etc.), running the `main.py` script

## What's my Todoist API token? How do I get it?
Your Todoist API token is a unique id that makes your tasks and behavior trackable. This id is understandable by the Todoist python library which will be in charge of getting the necessary information to know when a task is due in 5 minutes or less.

For accessing your Todoist API, follow the next steps:
1. Open Todoist
2. Click on your avatar on the top right of your Todoist window
![](https://ibb.co/ngkwMG0)
3. Click on `Settings`
![](https://ibb.co/ngkwMG0)
4. Click on `Integrations`
![](https://ibb.co/ngkwMG0)
5. Scroll down and click on `Copy to clipboard` in the `API token` section
![](https://ibb.co/ngkwMG0)