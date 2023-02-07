import tkinter


ventana = tkinter.Tk()
ventana.geometry("800x600")

recuadroInput = tkinter.Frame(ventana, bg="lightblue")

textboxLink = tkinter.Entry(recuadroInput, width="50")
textboxLink.pack(side=tkinter.LEFT, padx=20, pady=20)
btnAgregar = tkinter.Button(recuadroInput, text="Agregar")
btnAgregar.pack(side=tkinter.LEFT, padx=20, pady=20)
btnDescargar = tkinter.Button(recuadroInput, text="Descargar")
btnDescargar.pack(side=tkinter.LEFT, padx=20, pady=20)

recuadroInput.pack()


ventana.mainloop()