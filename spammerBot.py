import pyautogui, time
time.sleep(5)
f = open("caraAlSol", 'r')   #Open "fichero "

for word in f:
    pyautogui.typewrite(word)   #Write the word
    pyautogui.press("enter")    #Send