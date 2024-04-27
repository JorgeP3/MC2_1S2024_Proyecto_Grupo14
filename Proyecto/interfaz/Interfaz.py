#clases
from clases.Grafo import Grafo

#librerias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from graphviz import Source
from PIL import Image
import io
import networkx as nx 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")
        self.grafo=Grafo()
        self.grafoG=nx.Graph()

        self.cargarWidgets()

    def cargarWidgets(self):
        
        #FRAME GRAFO
        self.frmGrafo=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        self.frmGrafo.place(x=20,y=20)

        
        #FRAME arbol
        self.frmArbol=tk.Frame(self.root,width=325, height=325,borderwidth=2, relief="ridge", bg="lightgrey")
        self.frmArbol.place(x=400,y=20)


        #FRAME con los botones
        frmControl=tk.Frame(self.root,width=600, height=200,borderwidth=2, relief="ridge", bg="lightgrey")
        frmControl.place(x=100,y=360)

        btnAgregarVertice=tk.Button(frmControl,text="Agregar Vértice",command=self.agregarVertice)
        btnAgregarVertice.place(x=10,y=20)

        btnAgregarArista=tk.Button(frmControl,text="Agregar Arista",command=self.agregarArista)
        btnAgregarArista.place(x=10,y=60)

        btnBusquedaAnchura=tk.Button(frmControl,text="Busqueda Anchura",command=self.busquedaAnchura)
        btnBusquedaAnchura.place(x=10,y=120)

        btnBusquedaProdundidad=tk.Button(frmControl,text="Busqueda Produndidad",command=self.busquedaProdundidad)
        btnBusquedaProdundidad.place(x=10,y=150)

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

        #figura del grafo
        figure = Figure(figsize=(3,3))
        self.ax = figure.add_subplot(111)
        self.canvas=FigureCanvasTkAgg(figure, self.frmGrafo)
        self.canvas.get_tk_widget().pack()

        #figura busqueda Anchura

        figureAnchura = Figure(figsize=(3,3))
        self.axAnchura = figureAnchura.add_subplot(111)
        self.canvasAnchura=FigureCanvasTkAgg(figureAnchura, self.frmArbol)
        self.canvasAnchura.get_tk_widget().pack()


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
            self.dibujargrafo()
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
            self.dibujargrafo()
        else:
            messagebox.showerror("Error", "vertice1 o vertice2 estan vacios")

    def generarGrafo(self):
        lista_vertices=self.grafo.obtener_vertices()
        lista_aristas=self.grafo.obtener_aristas()

        for vertice in lista_vertices:
            self.grafoG.add_node(vertice)
        
        for arista in lista_aristas:
            self.grafoG.add_edge(arista[0],arista[1])

    def dibujargrafo(self):
        self.ax.clear()
        nx.draw(self.grafoG, ax=self.ax, with_labels=True)
        self.canvas.draw()

    def busquedaAnchura(self):
        lista_vertices=self.grafo.obtener_vertices()
        lista_vertices_ordenada=sorted(lista_vertices)
        #inicia siempre en orden ascendente por el vertice que esta primero en la lista
        vertice_inicial=lista_vertices_ordenada[0]

        self.axAnchura.clear()
        bfs_edges=list(nx.bfs_edges(self.grafoG,source=vertice_inicial))
        pos = nx.spring_layout(self.grafoG)
        nx.draw(self.grafoG, pos=pos, ax=self.axAnchura, with_labels=True)
        nx.draw_networkx_edges(self.grafoG, pos=pos, edgelist=bfs_edges, edge_color='#FFF05F', ax=self.axAnchura)
        nx.draw_networkx_nodes(self.grafoG, pos=pos, nodelist=[vertice_inicial]+[v for u, v in bfs_edges], node_color='#FFF05F', ax=self.axAnchura)
        self.canvasAnchura.draw()

    def busquedaProdundidad(self):
        lista_vertices=self.grafo.obtener_vertices()
        lista_vertices_ordenada=sorted(lista_vertices)
        #inicia siempre en orden ascendente por el vertice que esta primero en la lista
        vertice_inicial=lista_vertices_ordenada[0]

        self.axAnchura.clear()
        dfs_edges=list(nx.dfs_edges(self.grafoG,source=vertice_inicial))
        pos = nx.spring_layout(self.grafoG)
        nx.draw(self.grafoG, pos=pos, ax=self.axAnchura, with_labels=True)
        nx.draw_networkx_edges(self.grafoG, pos=pos, edgelist=dfs_edges, edge_color='#4CE27F', ax=self.axAnchura)
        nx.draw_networkx_nodes(self.grafoG, pos=pos, nodelist=[vertice_inicial]+[v for u, v in dfs_edges], node_color='#4CE27F', ax=self.axAnchura)
        self.canvasAnchura.draw()

    '''
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
    '''

    

        

      
