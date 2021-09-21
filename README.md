# Automated-Attendance
This a web scraping bot written in python using the selenium library. The robot logs into the website with some credentials, locates the attendance widget, scrolls through the list to find the current date's attendance and marks it present, daily. 

The bot was custom made for my [college's website](http://psd.bits-pilani.ac.in/Login.aspx).
You can see it in action [here]()

The bot is tailored for a specific task. It can:
* Open Chrome through a webdriver
* Sign in to a google account
* Repeatedly try marking attendance for every date until it succesfully marks it of the active date
* Repeat the process for multiple accounts
* Run every day at a specific time with Windows Task Scheduler

The bot cannot:
* Log in without credentials
* Intelligently locate widgets as a human would (primarily xpath is used)
* Run on a completely different platform/website

There is little scope for further improvements since the bot reliably does what it is tasked to. Image processing may be employed to locate the active date to improve speed.

This project is GPL-3.0 Liscenced to Aditya Nair under GogiPuttar
