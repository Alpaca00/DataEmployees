from time import sleep
import keyword
from pyautogui import *
import pyautogui
import pyscreeze
from PIL import Image


pyautogui.PAUSE = 0.8
pyautogui.FAILSAFE = True

sleep(2)

pyautogui.moveTo(484, 745, duration=0.2)
pyautogui.click()

pyautogui.hotkey('ctrl', 'alt', 't')

sleep(6)
pyautogui.move(-330, -648, duration=0.2)
pyautogui.click()

pyautogui.typewrite('cd python', interval=0.1)
pyautogui.press('enter')


pyautogui.typewrite('cd Gui?Employees', interval=0.1)
pyautogui.press('enter')

pyautogui.typewrite('source venv/bin/activate', interval=0.1)
pyautogui.press('enter')


sleep(1)
pyautogui.typewrite('python3 main.py', interval=0.1)
pyautogui.press('enter')


sleep(2)
pyautogui.screenshot('/home/oleg/Pictures/example.png')
sleep(1)


img = Image.open("/home/oleg/Pictures/newBtn.png")
#img.show()
if img is not None:
    doc = pyscreeze.locateCenterOnScreen(img, grayscale=False)
    print(doc)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)

sleep(1)
pyautogui.move(-150, -330, duration=0.1)
pyautogui.click()
pyautogui.typewrite('Angelina', interval=0.1)


pyautogui.move(0, 30, duration=0.1)
pyautogui.click()
pyautogui.typewrite('Jolie', interval=0.1)


pyautogui.move(0, 33, duration=0.1)
pyautogui.click()
pyautogui.typewrite('911', interval=0.1)


pyautogui.move(0, 34.5, duration=0.1)
pyautogui.click()
pyautogui.typewrite('jolie@gamil.com', interval=0.1)


pyautogui.move(0, 35, duration=0.1)
pyautogui.click()
pyautogui.typewrite('Holliwood, Usa', interval=0.1)


addImg = Image.open("/home/oleg/Pictures/addBtn.png")
#addImg.show()
if img is not None:
    doc = pyscreeze.locateCenterOnScreen(addImg, grayscale=False)
    print(doc)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


okImg = Image.open("/home/oleg/Pictures/okBtn.png")
#okImg.show()
if okImg is not None:
    doc = pyscreeze.locateCenterOnScreen(okImg, grayscale=False)
    print(doc)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


pyautogui.moveTo(1366/2, 768/2, duration=0.2)
pyautogui.move(150, 150, duration=0.2)
pyautogui.click()
pyautogui.typewrite('Angelina Jolie', interval=0.2)


sleep(1)
searchImg = Image.open("/home/oleg/Pictures/searchBtn.png")
#searchImg.show()
if searchImg is not None:
    doc = pyscreeze.locateCenterOnScreen(searchImg, grayscale=False)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


pyautogui.move(-90, -330, duration=0.2)
pyautogui.click()


sleep(1)
deleteImg = Image.open("/home/oleg/Pictures/deleteBtn.png")
#deleteImg.show()
if deleteImg is not None:
    doc = pyscreeze.locateCenterOnScreen(deleteImg, grayscale=False)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


sleep(1)
yesImg = Image.open("/home/oleg/Pictures/yesBtn.png")
#yesImg.show()
if yesImg is not None:
    doc = pyscreeze.locateCenterOnScreen(yesImg, grayscale=False)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)

sleep(1)
okImg = Image.open("/home/oleg/Pictures/okBtn.png")
#okImg.show()
if okImg is not None:
    doc = pyscreeze.locateCenterOnScreen(okImg, grayscale=False)
    print(doc)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


pyautogui.moveTo(1366/2, 768/2, duration=0.2)
pyautogui.click()


pyautogui.moveTo(1366/2, 768/2, duration=0.2)
pyautogui.move(150, 150, duration=0.2)
pyautogui.click()
pyautogui.typewrite('Ansa Oliveira', interval=0.2)


sleep(1)
searchImgUpd = Image.open("/home/oleg/Pictures/searchBtn.png")
#searchImgUpd.show()


if searchImgUpd is not None:
    doc = pyscreeze.locateCenterOnScreen(searchImgUpd, grayscale=False)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


pyautogui.move(-90, -330, duration=0.2)
pyautogui.click()


pyautogui.moveTo(1366/2, 768/2, duration=0.2)
pyautogui.click()
pyautogui.move(170, 170, duration=0.2)
pyautogui.click()


pyautogui.move(-120, -330, duration=0.1)
print(pyautogui.position())
pyautogui.click()

pyautogui.PAUSE = 0.4
for i in range(13):
    pyautogui.press('backspace')
pyautogui.typewrite('Angelina', interval=0.1)

pyautogui.move(0, 30, duration=0.1)
pyautogui.click()
for i in range(13):
    pyautogui.press('backspace')
pyautogui.typewrite('Jolie', interval=0.1)


pyautogui.move(0, 33, duration=0.1)
pyautogui.click()
for i in range(15):
    pyautogui.press('backspace')
pyautogui.typewrite('911', interval=0.1)


pyautogui.move(0, 34.5, duration=0.1)
pyautogui.click()
for i in range(27):
    pyautogui.press('backspace')
pyautogui.typewrite('jolie@gmail.com', interval=0.1)


pyautogui.move(0, 35, duration=0.1)
pyautogui.click()
for i in range(26):
    pyautogui.press('backspace')
pyautogui.typewrite('Holliwood, Usa', interval=0.1)


pyautogui.move(-50, 58, duration=0.1)
pyautogui.click()


sleep(1)
okImg = Image.open("/home/oleg/Pictures/okBtn.png")
#okImg.show()
if okImg is not None:
    doc = pyscreeze.locateCenterOnScreen(okImg, grayscale=False)
    print(doc)
    if doc is None:
        print('Image not found on the screen!')
    else:
        pyautogui.click(doc)


