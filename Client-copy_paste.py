import pyperclip
import time
from pynput import keyboard
import socket
import platform

def main():

    hotKeyCopy = '<cmd>+c'
    hotKeyPaste = '<cmd>+v'
    
    if(platform.system() == 'Windows'):
        hotKeyCopy = '<ctrl>+c'
        hotKeyPaste = '<ctrl>+v'
     

    # Create a socket object  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
      
    # Define the port on which you want to connect  
    startingPort = 12345                
    abool = True
    for port in range(startingPort,65535):   
    # connect to the server on local computer  
        try:
            s.connect(('192.168.1.174', port))
            break
        except Exception:
            print(port)
            #port = port+1  
      
    # receive data from the server  
    print (s.recv(1024) ) 

    while True:
    
        def function_1():
            print('Function 1 activated: copy text from pc clipB into server ')
            time.sleep(1)
            copiedText = pyperclip.paste()
            print(copiedText)
            s.send(copiedText.encode())
            #pyperclip.copy(str)
            # send str to server

        def function_2():
            print('Function 2 activated: get text from server')
            # get str to server
            str = "copied text from server"
            pyperclip.copy(str)

        with keyboard.GlobalHotKeys({
            hotKeyCopy: function_1,
            hotKeyPaste: function_2}) as h:
            h.join()
    # close the connection  
    s.close()   


if __name__ == "__main__":
    main()