from turtle import *
from random import randrange

graph = dict()

def draw(g):
	penup()
	visted = []
	position = {}

	#sets position for nodes and writes it
	for i in g.keys():
		a = True
		while a:
			a = False
			x = randrange(-400, 400)
			y = randrange(-200, 200)
			for j in position.keys():
				if 10000 > (position[j][0]-x)**2 + (position[j][1]-y)**2:
					a = True
					break 
		setposition(x, y)
		position[i] = [x, y]
		write(i)

	#draw edges
	for i in g.keys():
		visted.append(i)
		for j in g[i]:
			if j not in visted:
				penup()
				setposition(position[i][0], position[i][1])
				pendown()
				setposition(position[j][0], position[j][1])
	mainloop()
	exit()


def add_node(node):
	if node not in graph.keys():
		graph[node] = []
	else:
		print("node lready exists")

def add_vertex(node1, node2):
	if node1 not in graph.keys() and node2 not in graph.keys():
		print("Node 1 and 2 not exists")
	elif node1 not in graph.keys():
		print("Node 1 not exists")
	elif node2 not in graph.keys():
		print("Node 2 not exists")
	elif node1 in graph[node2]:
		print("edge already exists")
	else:
		graph[node1].append(node2)
		graph[node2].append(node1)

def print_vertex():
	visited = []
	going_to_visit = graph.keys()
	for i in going_to_visit:
		visited.append(i)
		for j in graph[i]:
			#if j not in visited: #for not printing double time
			print(i,'-->',j)

def matrix_to_graph(list1):
	g = dict()
	for i in range(len(list1)):
		g[i] = []
	for index in range(len(list1)):
		for i in range(len(list1)):
			if list1[index][i] == 1 and index != i:
				g[index].append(i)
	return g


print("press 1 to enter nodes and edges")
print("Press 2 to enter adjacency matrix")
opt = int(input())

if opt == 2:
	number_of_nodes = int(input("Enter number of nodes"))
	g = []
	print("Enter the matrix seperated by spaces")
	for i in range(number_of_nodes):
		temp = [int(x) for x in input().split()]
		g.append(list(temp))
	graph = matrix_to_graph(g)
while True:
	print("\n\npress 1 to add node")
	print("press 2 to add edges")
	print("press 3 to print")
	print("Press 4 to draw and exit")
	print("press 5 to exit")
	a = int(input())
	if a == 1:
		node = input('Enter node:')
		add_node(node)
	elif a == 2:
		node1 = input("Enter node 1:")
		node2 = input("Enter node 2:")
		add_vertex(node1, node2)
	elif a == 3:
		print_vertex()
	elif a == 4:
		draw(graph)
	else:
		break