import os
import subprocess as sp

paths = {
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\Windows\System32\calc.exe",
    'vscode': "C:\\Users\\abhay\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.system("notepad.exe")

def open_discord():
    os.startfile(paths['discord'])

def open_vscode():
    sp.Popen(paths['vscode'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])