import tkinter as tk 

window = tk.Tk()
window.title("Address Entry Form")


def obtener_textos():
    for i in range(0,8):
        texto = entrys[i].get()
        print(f'{lbls[i]} {texto}')

def clear_textos():         # POR MEJORAR
    delet_text = entrys[i].delete(0,tk.END)
    delet_text = entrys[i].get() 
    print(f'{lbls[i]} {delet_text}')

def close_window():
    window.destroy()

lbls = ['Fist Name:',
        'Last Name:',
        'Address Line 1:',
        'Address Line 2:',
        'City:',
        'State/Province:',
        'Postal Code:',
        'Country:'          ]

entrys = []             # Guardamos todas las instancias entry para una posible posterior invocacion

frame_text = tk.Frame(window, relief=tk.SUNKEN,border=2)
frame_text.pack()

for i in range(0,8):
    lbl = tk.Label(frame_text, text = lbls[i])
    lbl.grid(row=i, column=0,sticky='e')

    entry = tk.Entry(frame_text, border=1, width=60)
    entry.grid(row=i, column=1)

    entrys.append(entry)

frame_buttons = tk.Frame(window)
frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

button_clear = tk.Button(frame_buttons,text="Clear")
button_submit = tk.Button(frame_buttons,text="Submit",command= obtener_textos)
button_close = tk.Button(frame_buttons,text="Exit",command= close_window)

button_submit.pack(side=tk.RIGHT)
button_clear.pack(side=tk.RIGHT)
button_close.pack(side=tk.RIGHT)



window.mainloop()