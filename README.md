# Stealth_Logger
The keylogger implemented by this Python script records keystrokes, screenshots using the webcam, and audio from the computer's default audio device.

# Keylogger that Reports to Email

The keylogger implemented by this Python script records keystrokes, screenshots using the webcam, and audio from the computer's default audio device. The obtained information is subsequently forwarded to the designated recipient via email.


## Requirements

- Python 3.x - The following Python packages are necessary: 'pynput', 'pyscreenshot', 'opencv-python','sounddevice', and'soundfile'
  'pip install pynput pyscreenshot opencv-python sounddevice soundfile' will install the necessary packages.

Configuration ##

You must modify the following settings in the code before executing the script:

'EMAIL_ADDRESS' refers to the email address used to deliver the logs.
'EMAIL_PASSWORD' is the email account's password.
The email address to which the logs will be delivered is 'RECIPIENT_EMAIL'.
- "SEND_EMAIL_INTERVAL": The time (in seconds) between sending emails containing logs that have been captured.

## Usage

Run the script by typing "python keylogger.py" into your computer's command line.
2. The keylogger will begin to operate and begin recording keystrokes.
3. It will occasionally record audio from the default audio device and snap screenshots using the webcam.
4. The gathered information will be emailed to the designated recipient.
5. Following the sending of each email, logs will be deleted.
6. Until the script is manually stopped (by pressing "Ctrl + C"), it will keep running and recording keystrokes.

Important Information

This script is only being made available for educational reasons. Before using this script, please make sure you have the required authorizations and are in compliance with all applicable laws and regulations. This script's unauthorised use can be against the law.

*** Disclaimer

Piyush Gayaki is the script's author. The use of this script may result in losses or legal repercussions for which the author is not responsible. You should only use it at your own risk.

# MOST IMPORTANT STEP FOR SENDING AND RECEIVING MAIL

First you need to enable 2-Step Verification.
1. Go to your Google Account .
2. Select Security.
3. Under "Signing in to Google," select App Passwords. You may need to sign in. If you don't
  have this option, it might be because:
  a. 2-Step Verification is not set up for your account.
  b. 2-Step Verification is only set up for security keys.
  c. Your account is through work, school, or other organization.
  d. You turned on Advanced Protection.
4. At the bottom, choose Select app and choose the app you using Select device and
  choose the device you're using > Generate.
5. Follow the instructions to enter the App Password. The App Password is the 16-character
  code in the yellow bar on your device.
6. Tap Done.
