from queue import *
#will use python's implementation for queues
# q = Queue()
#add to queue -> q.put(n)
#pop from queue -> q.get()
#test if queue is empty -> q.empty()

class Graph:
    def __init__(self):
        self.ADJ = {}
    def add(self, n, neighbors):
        self.ADJ[n] = neighbors
    def remove(self, n):
        del self.ADJ[n]
        for k in self.ADJ.keys():
            temp = []
            for i in self.ADJ[k]:
                if i != n:
                    temp.append(i)
            self.ADJ[k] = temp
    def BFS(self, n):
        q = Queue()
        seen = {}
        distance = {}
        pred = {}
        for k in self.ADJ.keys():
            seen[k] = False
            distance[k] = 99999
            pred[k] = -1
        q.put(n)
        seen[n] = True
        distance[n] = 0
        while(not q.empty()):
            current = q.get()
            print(current , distance[current], pred[current])
            for i in self.ADJ[current]:
                if seen[i] == False:
                    q.put(i)
                    seen[i] = True
                    distance[i] = distance[current]+1
                    pred[i] = current

                    
G = Graph()
G.add(1,[2,3])
G.add(2,[1,5,7])
G.add(3,[1,4,5])
G.add(4,[3,5])
G.add(5,[2,3,4,6])
G.add(6,[5,8])
G.add(7,[2,9])
G.add(8,[6,9])
G.add(9,[7,8])
G.add(10,[11,12])
G.add(11,[10,12,13])
G.add(12,[10,11,13])
G.add(13,[11,12])

G.BFS(1)
