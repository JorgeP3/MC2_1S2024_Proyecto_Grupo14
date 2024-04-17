#clases
from clases.Grafo import Grafo

#librerias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from graphviz import Source




class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")
        self.grafo=Grafo()

        self.cargarWidgets()

    def cargarWidgets(self):
        
        #FRAME GRAFO
        frmFrameGrafo=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        frmFrameGrafo.place(x=20,y=20)

        

        #FRAME arbol
        frmArbol=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        frmArbol.place(x=400,y=20)


        #FRAME con los botones
        frmControl=tk.Frame(self.root,width=600, height=200,borderwidth=2, relief="ridge", bg="lightgrey")
        frmControl.place(x=100,y=360)

        btnAgregarVertice=tk.Button(frmControl,text="Agregar Vértice",command=self.agregarVertice)
        btnAgregarVertice.place(x=10,y=20)

        btnAgregarArista=tk.Button(frmControl,text="Agregar Arista",command=self.agregarArista)
        btnAgregarArista.place(x=10,y=60)

        self.txtVertice=tk.Entry(frmControl,)
        self.txtVertice.place(x=105,y=20)

        self.txtVertice1=tk.Entry(frmControl,width=5)
        self.txtVertice1.place(x=105,y=60)
        self.txtVertice2=tk.Entry(frmControl,width=5)
        self.txtVertice2.place(x=170,y=60)

        self.txtListaAristas = tk.Listbox(frmControl,)
        self.txtListaAristas.place(x=250,y=20)

        lblEntrada=tk.Label(frmControl,text="--",bg="lightgrey")
        lblEntrada.place(x=147,y=60)


    #agrega un vertice al grafo
    def agregarVertice(self):
        arista=self.txtVertice.get()

        if arista:
            self.grafo.agregar_vertice(arista)
            self.txtVertice.delete(0, "end")

            self.txtListaAristas.delete(0,tk.END)

            #llena el listbox con los vertices
            lista_vertices=self.grafo.obtener_vertices()
            for vertice in lista_vertices:
                self.txtListaAristas.insert("end",vertice)

            self.generarGrafo()
            self.actualizarGrafo()
        else:
            messagebox.showerror("Error", "No se ingresó ningun vertice")

    def agregarArista(self):
        vertice1=self.txtVertice1.get()
        vertice2=self.txtVertice2.get()
        
        if vertice1 and vertice2:
            pass
        else:
            messagebox.showerror("Error", "vertice1 o vertice2 estan vacios")


    def generarGrafo(self):
        lista_vertices=self.grafo.obtener_vertices()
        
        codigo_dot="graph {\n node[shape=circle]\n"
        for vertice in lista_vertices:
            codigo_dot+=vertice+"\n"
        codigo_dot+="}"

        grafo=Source(codigo_dot)

        grafo.render(filename='grafo', format='png', cleanup=True, directory="imagenes")


    def actualizarGrafo(self):
        frmFrameGrafo=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        frmFrameGrafo.place(x=20,y=20)
        imgGrafo=tk.PhotoImage(file="imagenes\grafo.png")
        lbl_imgGrafo=tk.Label(frmFrameGrafo,image=imgGrafo)
        lbl_imgGrafo.image=imgGrafo
        lbl_imgGrafo.pack()

    def actualizarArbol(self):
        frmArbol=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        frmArbol.place(x=400,y=20)
        imgArbol=tk.PhotoImage(file="imagenes\grafo.png")
        lbl_imgArbol=tk.Label(frmArbol,image=imgArbol)
        lbl_imgArbol.image=imgArbol
        lbl_imgArbol.pack()

    

        

      
