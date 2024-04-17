from tkinter import messagebox

class Grafo:
    def __init__(self):
        self.vertices = {}
    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:#si el vertice no existe, lo grega si no marca error
            self.vertices[vertice] = []
            print("sea gregó el vertice",vertice)
        else:
            messagebox.showerror("Error", "El vertice ya existe" )

    def agregar_arista(self, origen, destino):
        #si encuentra el vertice oriegn y destino agrega la arista si no marca error
        if origen in self.vertices and destino in self.vertices: 
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)
        else:
            messagebox.showerror("Error", "No se encontró el vertice origen o destino")


    def obtener_vertices(self):
        return list(self.vertices.keys())
    
    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.vertices.items():
            for adyacente in adyacentes:
                aristas.append((vertice, adyacente))
        return aristas