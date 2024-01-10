import tkinter as tk 

root = tk.Tk()
space_x = 5

def convert_temp():
    try:
        temp = float(entry.get())
        celcius = (temp - 32)*5/9

        lbl_conv["text"] = str(f'{round(celcius,3)} °C')

        print("Calculo correcto")

    except:
        lbl_conv["text"] = 'Temp. Incorrect'
        print('Intrese numero correcto')


root.title("Temperature converter")
root.resizable(width=False, height=False)   # La ventana mantiene un tamaño constante

root.columnconfigure([0,1,2,3], minsize=10)
root.columnconfigure(0, minsize=50)

entry = tk.Entry(root, width= 10)
entry.grid(row=0, column= 0, ipadx= space_x, ipady= 5)

lbl_f = tk.Label(root, text= '°F')
lbl_f.grid(row=0, column= 1, ipadx= space_x)

btn_convert = tk.Button(root, text = "->",command=convert_temp)
btn_convert.grid(row=0, column= 2,ipadx= space_x )

lbl_conv = tk.Label(root,text="Temperatura Celsius")
lbl_conv.grid(row=0, column= 3, ipadx= space_x)



root.mainloop()