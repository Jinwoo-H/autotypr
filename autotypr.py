import pytesseract
import PIL.Image
import cv2
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


myconfig = r"--psm 6 --oem 3"

time.sleep(3.0)

iml = pyautogui.screenshot(region=(350,460,1200,150))
iml.save(r"C:\Users\jinwo\Documents\PythonBot\textbox.png")

text = pytesseract.image_to_string(PIL.Image.open("textbox.png"), config=myconfig)
text = text.replace("\n", " ")

pyautogui.typewrite(text, interval=0.05)
