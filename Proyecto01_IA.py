import algorithms
import data

import pygame
import numpy as np

from data import PyGameMaze

clock = pygame.time.Clock()

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Colores
colors = {1: (255, 255, 255),       # Negro para los muros
          0: (0, 0, 0), # Blanco para los caminos
          2: (0, 0, 255),     # Azul para la entrada
          3: (255, 0, 0),   # Rojo para la meta
          4: (0,255,0), #Verde para camino seguido
          5: (255,128,0)} #
            

#Lectura de laberinto y generacion de matriz numpy           
maze = data.get_maze('test_maze.txt')
npMaze = np.array(maze)

#Creacion documentos excel con funcion de costo y funcion heuristica
data.create_costFuctionDoc(npMaze)
data.create_euclideanHeuristicDoc(npMaze)
data.create_manhattanHeuristicDoc(npMaze)

#Creacion de grafos, grafos con peso, grafos con heuristica y grafos completos
graph = data.getGraph()
weighted_graph = data.getWeightedGraph()
euclideanHeuristic_graph = data.getEuclideanHeuristicGraph()
manhattanHeuristic_graph = data.getManhattanHeuristicGraph()
euclideanComplete_graph = data.getEuclideanCompleteGraph()
manhattanComplete_graph = data.getManhattanCompleteGraph()

#Inicio y fin del laberinto
start = data.get_mazeStart(npMaze)
end = data.get_mazeEnd(npMaze)

#Generacion de objeto Laberinto de Pygame
pygameMaze = PyGameMaze(colors,width,screen,npMaze)
#Dibujo inicial de laberinto
pygameMaze.draw_maze()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type==pygame.KEYDOWN:
            pygameMaze.draw_maze()
            if event.key==pygame.K_1: #[1] BFS
                print("Procesando con Breadth First Search...")
                algorithms.bfs(graph,start,end,pygameMaze)
            elif event.key==pygame.K_2: #[2] DFS
                print("Procesando con Depth First Search...")
                algorithms.dfs(graph,start,end,pygameMaze)
            elif event.key==pygame.K_3: #[3] DLS
                print("Procesando con Depth Delimited Search...")
                algorithms.dls(graph,start,end,2000,pygameMaze)
            elif event.key==pygame.K_4: #[4] USC
                print("Procesando con Uniform Cost Search...")
                algorithms.ucs(weighted_graph,start,end,pygameMaze)
            elif event.key==pygame.K_5: #[5] GBFS Distancia Euclidiana
                print("Procesando con Greedy Best First Search (Distancia Euclidiana)...")
                algorithms.gbfs(euclideanHeuristic_graph,start,data.getEuclideanHeuristicTable()[start],end,pygameMaze)
            elif event.key==pygame.K_6: #[6] A*S Distancia Euclidiana
                print("Procesando con A* Search (Distancia Euclidiana)...")
                algorithms.astar_s(euclideanComplete_graph,start,data.getEuclideanHeuristicTable()[start],end,pygameMaze)
            elif event.key==pygame.K_7: #[7] GBFS Distancia Manhattan
                print("Procesando con Greedy Best First Search (Distancia Manhattan)...")
                algorithms.gbfs(manhattanHeuristic_graph,start,data.getManhattanHeuristicTable()[start],end,pygameMaze)
            elif event.key==pygame.K_8: #[8] A*S Distancia Manhattan
                print("Procesando con A* Search (Distancia Manhattan)...")
                algorithms.astar_s(manhattanComplete_graph,start,data.getManhattanHeuristicTable()[start],end,pygameMaze)
                

    clock.tick(60)

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()