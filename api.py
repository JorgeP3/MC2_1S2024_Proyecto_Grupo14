import networkx as nx 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
G = nx.Graph()
root = tk.Tk()
root.title("Algoritmo de busqueda en Anchura")
vertex_entry = tk.Entry(root)
vertex_entry.pack()

def agregarVertice():
    G.add_node(vertex_entry.get())
    draw_graph()

add_vertex_button=tk.Button(root, text="Agregar vertice", command=agregarVertice)
add_vertex_button.pack()

edge_entry_1=tk.Entry(root)
edge_entry_1.pack()
edge_entry_2=tk.Entry(root)
edge_entry_2.pack()

def agregarArista():
    G.add_edge(edge_entry_1.get(),edge_entry_2.get())
    draw_graph()

add_edge_button = tk.Button(root, text="Agregar arista", command=agregarArista)
add_edge_button.pack()



print_info_button=tk.Button(root, text="Info de datos agregados (consola)", command=lambda:print("Numero de nodos:",G.number_of_nodes(),"\nNumero de bordes:",G.number_of_edges()))
print_info_button.pack()

figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111)
canvas=FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

def draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='r', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
        canvas.draw()

draw_button = tk.Button(root, text="Dibujar grafo", command=draw_graph)
draw_button.pack()

def show_bfs():
    bfs_edges=list(nx.bfs_edges(G,source=vertex_entry.get()))
    draw_graph(bfs_edges)
    canvas.draw()
    
bfs_button = tk.Button(root, text="Busqueda en anchura", command=show_bfs)
bfs_button.pack()

def hola_mundo():
    print("hola mundo")

bfs_button2 = tk.Button(root, text="ejemplo", command=hola_mundo)
bfs_button2.pack()


root.mainloop()