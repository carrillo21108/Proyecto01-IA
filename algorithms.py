from implementations import Fifo,Lifo,PriorityQueue
import time

def reconstruct_path(predecessors, start, end, pygameMaze):
    current = end
    path = []
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()  # Invertir el camino, ya que lo reconstruimos de atrás hacia adelante
    
    pygameMaze.draw_maze()
    for node in path:
        pygameMaze.draw_pathcell(node,5)

def bfs(graph,startNode,endNode,pygameMaze):
    start_time = time.perf_counter()
    toBeVisited = []
    visited = []
    queue = Fifo()
    predecessors = {startNode: None}
    
    toBeVisited.append(startNode)
    queue.insert(startNode)
    
    count = 0
    while not queue.empty():
        count+=1
        s = queue.remove_first()
        pygameMaze.draw_pathcell(s,4)
        visited.append(s)
        
        if s==endNode:
            print("Iteraciones BFS: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return visited
        
        for n in graph[s]:
            if n not in toBeVisited:
                toBeVisited.append(n)
                queue.insert(n)
                predecessors[n] = s
    
    return None
                
def dfs(graph,startNode,endNode,pygameMaze):
    start_time = time.perf_counter()
    toBeVisited = []
    visited = []
    stack = Lifo()
    predecessors = {startNode: None}
    
    toBeVisited.append(startNode)
    stack.insert(startNode)
    
    count = 0
    
    while not stack.empty():
        count+=1
        s = stack.remove_first()
        pygameMaze.draw_pathcell(s,4)
        visited.append(s)
        
        if s==endNode:
            print("Iteraciones DFS: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return visited
        
        for n in reversed(graph[s]):
            if n not in toBeVisited:
                toBeVisited.append(n)
                stack.insert(n)
                predecessors[n] = s
                
    return None

def dls(graph,startNode,endNode,limit,pygameMaze):
    start_time = time.perf_counter()
    toBeVisited = []
    visited = []
    stack = Lifo()
    predecessors = {startNode: None}
    
    toBeVisited.append(startNode)
    stack.insert(startNode)
    
    count = 0
    
    while not stack.empty():
        count+=1
        s = stack.remove_first()
        pygameMaze.draw_pathcell(s,4)
        visited.append(s)
        
        if s==endNode:
            print("Iteraciones DLS: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return visited
        
        if limit>0:
            lastLen = len(toBeVisited)
            for n in reversed(graph[s]):
                if n not in toBeVisited:
                    toBeVisited.append(n)
                    stack.insert(n)
                    predecessors[n] = s
            
            if len(toBeVisited)!=lastLen:
                limit-=1
    
    return None
                
def ucs(graph,startNode,endNode,pygameMaze):
    start_time = time.perf_counter()
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),0)
    predecessors = {startNode: None}
    
    count=0
    while not queue.empty():
        count+=1
        actualCost, value = queue.remove_first()
        actualNode, actualPath = value
        
        pygameMaze.draw_pathcell(actualNode,4)
        
        if actualNode==endNode:
            print("Iteraciones UCS: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, cost in item.items():
                    if neighborNode not in visited:
                        newPath = actualPath+[neighborNode]
                        newCost = actualCost+cost
                        queue.insert((neighborNode,newPath),newCost)
                        predecessors[neighborNode] = actualNode
                    
    return None

def gbfs(graph,startNode,heuristic,endNode,pygameMaze):
    start_time = time.perf_counter()
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),heuristic)
    predecessors = {startNode: None}
    
    count=0
    while not queue.empty():
        count+=1
        actualNode, actualPath = queue.remove_first()[1]
        
        pygameMaze.draw_pathcell(actualNode,4)
        
        if actualNode==endNode:
            print("Iteraciones GBFS: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, heuristic in item.items():
                    if neighborNode not in visited:
                        newPath = actualPath+[neighborNode]
                        queue.insert((neighborNode,newPath),heuristic)
                        predecessors[neighborNode] = actualNode
                    
    return None

def astar_s(graph,startNode,heuristic,endNode,pygameMaze):
    start_time = time.perf_counter()
    visited = []
    queue = PriorityQueue()
    queue.insert((startNode,[startNode]),0+heuristic)
    accumulated = {startNode:0}
    predecessors = {startNode: None}
    
    count=0
    
    while not queue.empty():
        count+=1
        actualCost, value = queue.remove_first()
        actualNode, actualPath = value
        
        pygameMaze.draw_pathcell(actualNode,4)

        if actualNode==endNode:
            print("Iteraciones A*_S: "+str(count))
            end_time = time.perf_counter()
            duracion = end_time - start_time
            print(f"El algoritmo tomo {duracion} segundos en ejecutarse.")
            reconstruct_path(predecessors, startNode, endNode, pygameMaze)
            return actualPath
        
        if actualNode not in visited:
            visited.append(actualNode)
            
            for item in graph[actualNode]:
                for neighborNode, values in item.items():
                    newPath = actualPath+[neighborNode]
                    newAccumulated = accumulated[actualNode]+values[0]
            
                    if neighborNode not in visited or newAccumulated<accumulated[neighborNode]:
                        accumulated[neighborNode] = newAccumulated
                        newCost = newAccumulated+values[1]
                        queue.insert((neighborNode,newPath),newCost)
                        predecessors[neighborNode] = actualNode
                    
    return None