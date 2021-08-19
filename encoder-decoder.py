import tkinter as tk
import tkinter.messagebox as tmsg

root = tk.Tk()
root.geometry("600x500")
root.title("Encoder-Decoder")
root.config(bg = 'seashell3')
#definfe functions

def encoder(key, message):
    cipher_text = ''
    for i in range(len(message)):
        x = (ord(key[i])+ord(message[i]))%26 
        x+=ord('A')
        cipher_text+=chr(x)
    result.insert(0, cipher_text)
 
def decoder(key, message):
    decipher_text = ''
    for i in range(len(message)):
        x = (ord(message[i]) - ord(key[i]) + 26)%26 
        x+=ord('A')
        decipher_text+=chr(x)
    result.insert(0, decipher_text)
 
def cipher():
    keyword = key.get().upper()
    message = text.get().upper()
    result.delete(0, tk.END)
    if len(keyword) == len(message):
        new_key = keyword
    elif len(keyword)<len(message):
        new_key = keyword
        for i in range(len(message) - len(keyword)):
            new_key+=keyword[i%len(keyword)]
    else:
        new_key = keyword[0:len(message)]
    #print(new_key)
    ans = encode.get()
    if ans == 'e':
        encoder(new_key, message)
    elif ans == 'd':
        decoder(new_key, message)
    else:
        result.delete(0,tk.END)
        result.insert(0, 'Invalid mode. Try again')
        encode.delete(0, tk.END)
    

def reset():
    text.delete(0,tk.END)
    key.delete(0,tk.END)
    encode.delete(0,tk.END)
    result.delete(0,tk.END)

def leave():
    ans = tmsg.askquestion("Exit", "Are you sure you want to exit?")
    if ans == 'yes':
        root.destroy()
    else:
        reset()

#Frame and head label
f1 = tk.Frame(root, bg = 'red', borderwidth = 4)
f1.place(relx = 0.25, rely = 0.08, relwidth = 0.5, relheight = 0.15)

tk.Label(f1, text = "Encode/Decode", bg = 'black', fg = 'white', font = 'georgia 30').place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

# frame for labels and entries
f2 = tk.Frame(root, bg = 'black')
f2.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.5)

tk.Label(f2, text = 'Text :',bg = 'black', fg = 'white', font = 'gerogia 15').place(relx = 0.02, rely = 0.08, relheight = 0.08)
text = tk.Entry(f2, font=  'gerogia 15')
text.place(relx = 0.2, rely = 0.08, relwidth = 0.75, relheight = 0.1)

tk.Label(f2, text = 'Key :',bg = 'black', fg = 'white', font = 'gerogia 15').place(relx = 0.02, rely = 0.3, relheight = 0.08)
key = tk.Entry(f2, font=  'gerogia 15')
key.place(relx = 0.2, rely = 0.3, relwidth = 0.75, relheight = 0.1)

tk.Label(f2, text = 'e/d :',bg = 'black', fg = 'white', font = 'gerogia 15').place(relx = 0.02, rely = 0.52, relheight = 0.08)
encode = tk.Entry(f2, font=  'gerogia 15')
encode.place(relx = 0.2, rely = 0.52, relwidth = 0.75, relheight = 0.1)

tk.Label(f2, text = 'Result :',bg = 'black', fg = 'white', font = 'gerogia 15').place(relx = 0.02, rely = 0.74, relheight = 0.08)
result = tk.Entry(f2, font=  'gerogia 15')
result.place(relx = 0.2, rely = 0.74, relwidth = 0.75, relheight = 0.1)

tk.Button(f2, text = 'Cipher', font = 'georgia 15', command = cipher).place(relx = 0.42, rely = 0.86, relwidth = 0.15, relheight = 0.12)

# reset and exti buttons
tk.Button(root, text = 'Reset', font = 'georgia 15', command = reset, bg = 'green', borderwidth = 0).place(relx = 0.1, rely = 0.85, relwidth = 0.15, relheight = 0.08)
tk.Button(root, text = 'Exit', font = 'georgia 15', command = leave, bg = 'red', borderwidth = 0).place(relx = 0.75, rely = 0.85, relwidth = 0.15, relheight = 0.08)

root.mainloop()