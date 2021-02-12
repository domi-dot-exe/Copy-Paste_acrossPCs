import pyperclip


def main():
    from pynput import keyboard
    import socket             
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
    print ("Socket successfully created") 
      
    port = 12345                
      
    bool = True
    while bool: 
        try:
            s.bind(('', port))
            bool = False
        except OSError:
            print(port)
            port = port+1      
    print ("socket binded to %s" %(port))  
      
    s.listen(5)   
    print ("socket is listening")            
    c, addr = s.accept()      
    print ('Got connection from', addr )   
    
    while True:    
    # send a thank you message to the client.  
        c.send(b'Thank you for connecting')  
        copiedText = c.recv(1024).decode()
        pyperclip.copy(copiedText)

        recvText = pyperclip.paste()
        print(recvText)
        '''
        def function_1():
            print('Function 1 activated')
            str = pyperclip.paste()
            print(str)
            #pyperclip.copy(str)
            # send str to server

        def function_2():
            print('Function 2 activated')
            # get str to server
            str = "copied text from server"
            pyperclip.copy(str)

        with keyboard.GlobalHotKeys({
            '<cmd>+c': function_1,
            '<cmd>+v': function_2}) as h:
            h.join()
        '''
    # Close the connection with the client  
    c.close() 


if __name__ == "__main__":
    main()