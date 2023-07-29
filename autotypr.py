import pytesseract
import PIL.Image
from pyautogui import *
import pyautogui
import time

myconfig = r"--psm 6 --oem 3"

time.sleep(3.0)

iml = pyautogui.screenshot(region=(350,460,1200,150))
iml.save(r"./textbox.png")

text = pytesseract.image_to_string(PIL.Image.open("textbox.png"), config=myconfig)
text = text.replace("\n", " ")

pyautogui.typewrite(text, interval=0.05)
