**Instagram Message Bot
Author: Yuvraj**

This Python script automates sending messages on Instagram using Selenium WebDriver. It logs into Instagram, navigates to the Direct Message (DM) section, selects a user, and sends multiple messages to that user. The code uses Selenium to interact with Instagram's web interface and requires chromedriver for operation.

**Features**
Automated Login: Logs into Instagram using provided credentials.
DM Navigation: Opens the Direct Message section and selects a user to chat with.
Message Sending: Sends a series of automated messages in a loop.
Session Management: Closes the browser after completing the task.
Prerequisites
Python 3.x: Ensure Python is installed on your machine.
Selenium: Install the Selenium package by running:
pip install selenium

ChromeDriver: Download the appropriate version of chromedriver that matches your Chrome browser version. Update the PATH variable in the script with the location of your chromedriver.

Save it to a known location on your computer.


Set Up Instagram Credentials:
Update the user and password variables with your Instagram login details.
Specify the Recipient:
Enter the username of the recipient in the person variable.

Usage
Run the Script:
bash
Copy code
python instagram_msg_bot.py
What the Script Does:
Opens Instagram in Chrome.
Logs in using the provided username and password.
Navigates to the DM section and selects the specified user.
Sends a series of messages in a loop, each message prefixed with "meow" and an index number.
Code Walkthrough
Imports:
Imports Selenium WebDriver modules for Chrome interaction, waiting, and key inputs.
Initialize WebDriver:
Defines chrome_options to disable notifications and initializes the WebDriver.
Instagram Login:
Loads Instagram and enters credentials to log in.
Handle Pop-ups:
Clicks "Not Now" on any notifications pop-up that may appear.
Navigate to DM Section:
Finds and clicks on the Direct Messaging icon.
Select User and Send Messages:
Finds the specified recipient and sends a series of messages in a loop.
Close Session:
Waits for a few seconds to ensure all messages are sent, then closes the browser.
