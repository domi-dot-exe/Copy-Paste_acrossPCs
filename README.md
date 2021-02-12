# Copy-Paste_acrossPCs
A (hopefully) small Python program that allow you to share a common clipboard between computers on the same LAN

### Requirements:
In order to use it, make sure to have both `Pynput` (for keyboard handling) and `Pyperclip` (for os clipboard). 
- `pip install pynput`
- `pip install pyperclip`

## Usage:
0. Open `Client-copy_paste.py` with a text editor and change the IP address on line 26 with your server's IP (or localhost if trying it on local);
1. Run `Server-copy_paste` on Server PC
2. Run `Client-copy_paste.py` on Client PC
3. From Client copy some text with `cmd+c`;
4. On Server PC press `cmd+v` to get the copied text. 
5. Enjoy. 

> If using windows just press `ctrl+c` and `ctrl+v`.
