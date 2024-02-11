from tkinter import *

def calcular_area():
    area_total = frame_interior1.winfo_width() * frame_interior1.winfo_height()
    area_armario = frame_interior.winfo_width() * frame_interior.winfo_height()
    area_habitacion = area_total - area_armario

    resultado_label.config(text=f"Área de la habitación: {area_habitacion} cm²")

root = Tk()
root.title("Roomba")



from tkinter import Tk, Frame

root = Tk()
root.title("Centrar Frames")

frame_exterior = Frame(root, width=690, height=560, bg="black", bd=2, relief="solid")
frame_exterior.pack()

frame_interior1 = Frame(frame_exterior, width=630, height=500, bg="white", bd=2, relief="solid")
frame_interior1.place(relx=0.5, rely=0.5, anchor="center")

frame_interior = Frame(frame_exterior, width=90, height=320, bg="brown", bd=2, relief="solid")
frame_interior.place(relx=0.26, rely=0.1)

calcular_button = Label(frame_exterior, text="Calcular Área", bg="gray", fg="white", padx=10, pady=5, cursor="hand2")
calcular_button.place(relx=0.5, rely=0.9, anchor="center")
calcular_button.bind("<Button-1>", lambda event: calcular_area())

resultado_label = Label(frame_exterior, text="", bg="white")
resultado_label.place(relx=0.5, rely=0.95, anchor="center")


root.mainloop()

