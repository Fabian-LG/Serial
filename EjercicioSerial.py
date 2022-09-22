import serial,time
from tkinter import *

#Ventana gráfica
root=Tk()

#msg1 = Label(root, text=estado, )
#msg1 = Label(root, text=" - ", relief=RAISED, width=25)
msg1 = Label(root, text=" - ", width=25)

Red = serial.Serial("/dev/cu.usbmodem1101", 9600, timeout=.1)#comunicación con el puerto, 9600 velocidad de transimisión

time.sleep(2) #tiempo de espera

estado=b'' #binaro

def led_on():
    global estado
    Red.write(b'P')
    time.sleep(.5)
    estado = Red.readline().decode('ascii')
    msg1['text']= estado
    #msg1.config(text="Led ON")

def led_off():
    global estado
    Red.write(b'A')
    time.sleep(.5)
    estado = Red.readline().decode('ascii')
    msg1['text'] = estado
    #msg1.config(text="Led OFF")

def salir():
    global estado
    Red.write(b'A')
    time.sleep(.5)
    estado=Red.readline().decode('ascii')
    Red.close()
    root.destroy()



root.title("Control de LED del Arduino")
root.geometry("500x500")

boton1 = Button(root, text="Led ON", width = 25, command=led_on)
boton2 = Button(root, text="Led OFF", width = 25, command=led_off)
boton3 = Button(root, text="Salir", width = 25, command=salir)

boton1.pack()
boton2.pack()
boton3.pack()
msg1.pack()

root.mainloop()