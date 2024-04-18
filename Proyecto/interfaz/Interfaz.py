#clases
from clases.Grafo import Grafo

#librerias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from graphviz import Source
from PIL import Image
import io




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
        self.frmFrameGrafo=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        self.frmFrameGrafo.place(x=20,y=20)

        
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

        self.txtListaVertices = tk.Listbox(frmControl,)
        self.txtListaVertices.place(x=250,y=20)
        self.txtListaAristas = tk.Listbox(frmControl,)
        self.txtListaAristas.place(x=400,y=20)

        lblEntrada=tk.Label(frmControl,text="--",bg="lightgrey")
        lblEntrada.place(x=147,y=60)


    #agrega un vertice al grafo
    def agregarVertice(self):
        arista=self.txtVertice.get()

        if arista:
            self.grafo.agregar_vertice(arista)
            self.txtVertice.delete(0, "end")

            self.txtListaVertices.delete(0,tk.END)

            #llena el listbox con los vertices
            lista_vertices=self.grafo.obtener_vertices()
            for vertice in lista_vertices:
                self.txtListaVertices.insert("end",vertice)

            self.generarGrafo()
            self.actualizarGrafo()
        else:
            messagebox.showerror("Error", "No se ingresó ningun vertice")

    #agrega aristas al grafo
    def agregarArista(self):
        vertice1=self.txtVertice1.get()
        vertice2=self.txtVertice2.get()
        
        if vertice1 and vertice2:
            self.grafo.agregar_arista(vertice1,vertice2)
            self.txtVertice1.delete(0, "end")
            self.txtVertice2.delete(0, "end")
            self.txtListaAristas.delete(0,tk.END)

            lista_aristas=self.grafo.obtener_aristas()

            for arista in lista_aristas:
                self.txtListaAristas.insert("end",arista[0]+"--"+arista[1])

            self.generarGrafo()
            self.actualizarGrafo()
        else:
            messagebox.showerror("Error", "vertice1 o vertice2 estan vacios")


    def generarGrafo(self):
        lista_vertices=self.grafo.obtener_vertices()
        lista_aristas=self.grafo.obtener_aristas()
        #codigo_dot = "graph [width=800, height=600];\n"
        codigo_dot="graph {\n node[shape=circle]\n"
        codigo_dot+="rankdir=\"LR\""
        for vertice in lista_vertices:
            codigo_dot+=vertice+"\n"

        for arista in lista_aristas:
            codigo_dot+=arista[0]+"--"+arista[1]+"\n"

        #codigo_dot += "size=\"800,600\";\n" 
        #codigo_dot+="graph [width=800, height=600];\n"
        codigo_dot+="}"

        with io.open('grafo.dot', 'w', encoding='utf-8') as archivo_dot:
            archivo_dot.write(codigo_dot)

        grafo=Source(codigo_dot)
        grafo.render(filename='grafo', format='png', cleanup=True, directory="imagenes")

        imagen_grafo = Image.open("imagenes/grafo.png")
        nueva_imagen = imagen_grafo.resize((325, 325), Image.BILINEAR)
        nueva_imagen.save("imagenes/grafo_resized.png")


    def actualizarGrafo(self):
        imgGrafo=tk.PhotoImage(file="imagenes/grafo_resized.png")
        lbl_imgGrafo=tk.Label(self.frmFrameGrafo,image=imgGrafo)
        lbl_imgGrafo.image=imgGrafo
        lbl_imgGrafo.pack()

        if hasattr(self, 'lbl_imgGrafo_anterior'):
            self.lbl_imgGrafo_anterior.destroy()

        self.lbl_imgGrafo_anterior = lbl_imgGrafo


    #actualizara el arbol
    def actualizarArbol(self):
        frmArbol=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        frmArbol.place(x=400,y=20)
        imgArbol=tk.PhotoImage(file="")
        lbl_imgArbol=tk.Label(frmArbol,image=imgArbol)
        lbl_imgArbol.image=imgArbol
        lbl_imgArbol.pack()

    

        

      
