import pyautogui
from pywinauto.application import Application
import time

app = Application(backend='uia').start('notepad.exe') #start application

app.UntitledNotepad.type_keys("Hei! tämä on testi. Tulen tallentamaan tämän tiedoston työpöydälle",with_spaces = True) #type into .txt file

app.UntitledNotepad.child_window(title="File", control_type="MenuItem").click_input() #open menu
#app.UntitledNotepad.print_control_identifiers()
app.UntitledNotepad.child_window(title="Save as", control_type="MenuItem").double_click_input() #click save as

app.UntitledNotepad.child_window(title="Save as", control_type="Window").click_input() #click so the window will be active
#app.UntitledNotepad.print_control_identifiers()

app.UntitledNotepad.child_window(title="All locations", control_type="SplitButton").click_input() #click on path so desktop can be written

time.sleep(1)
pyautogui.write("Desktop") # type desktop
time.sleep(0.5)

app.UntitledNotepad.child_window(title="File name:", auto_id="1001", control_type="Edit").type_keys("OskariKurtti.txt") #name the file

app.UntitledNotepad.child_window(title="Save", auto_id="1", control_type="Button").click_input() #save the file

time.sleep(1)

confirmSave = app.UntitledNotepad.child_window(title="Yes", auto_id="CommandButton_6", control_type="Button") #find the optional overwrite button

if app.UntitledNotepad.child_window(title="Yes", auto_id="CommandButton_6", control_type="Button").exists():
    confirmSave.click_input() #if overwrite is possible/ needed. Overwrite
else:
    print("File save -- Succesful") #if this is the first time running program no need for overwriting

#app.OskariKurttiTxtNotepad.print_control_identifiers()

app.OskariKurttiTxtNotepad.child_window(title="Close", control_type="Button").click_input() #close notepad

app = Application(backend='uia').start('mspaint.exe') #start paint

time.sleep(2) #wait for paint to start
pyautogui.getWindowsWithTitle("Paint")[0].maximize() #maximize paint for accuracy

canvas = pyautogui.locateCenterOnScreen('canvas.png') #locate a big white area

kyna = pyautogui.locateCenterOnScreen('kyna.png') #locate pencil tool
pyautogui.click(kyna) #select pencil tool

pyautogui.moveTo(canvas) #move to a confirmed area for drawing

pyautogui.dragRel(-100, 0, duration=0.5)
pyautogui.dragRel(0, 200, duration=0.5)
pyautogui.dragRel(200, 0, duration=0.5)
pyautogui.dragRel(0, -200, duration=0.5)
pyautogui.dragRel(-100, 0, duration=0.5) #make a square

ampari = pyautogui.locateCenterOnScreen('ampari.png')
pyautogui.click(ampari) #locate and click on the bucket fill

pyautogui.moveTo(canvas)
pyautogui.moveRel(0, 50, duration=0.25)
pyautogui.click() #fill the square with whatever colour happens to be

punainen = pyautogui.locateCenterOnScreen('punainen.png')
pyautogui.click(punainen) #locate and select the colour red

pyautogui.moveTo(canvas)
pyautogui.moveRel(0, -25, duration=0.5)
pyautogui.click() #first move to the edge of the square then move out of it to fill the rest of the canvas with red

sulku = pyautogui.locateCenterOnScreen('sulku.png')
pyautogui.click(sulku) #locate and close paint

dontSave = pyautogui.locateCenterOnScreen('dontSave.png')
pyautogui.click(dontSave) #no need to save this masterpiece

