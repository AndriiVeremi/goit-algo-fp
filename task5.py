import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def get_color_for_step(step, total_steps):
    red = int((step / total_steps) * 255)  
    green = int((step / total_steps) * 255)
    blue = int((step / total_steps) * 255)

    color_hex = f"#{red:02X}{green:02X}{blue:02X}"
    return color_hex


def dfs(root):
    stack = [root]
    visited = []
    step = 0
    total_nodes = 0

    def count_nodes(node):
        nonlocal total_nodes
        if node:
            total_nodes += 1
            count_nodes(node.left)
            count_nodes(node.right)

    count_nodes(root)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node.color = get_color_for_step(step, total_nodes)  
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def bfs(root):
    queue = [root]
    visited = []
    step = 0
    total_nodes = 0

    def count_nodes(node):
        nonlocal total_nodes
        if node:
            total_nodes += 1
            count_nodes(node.left)
            count_nodes(node.right)

    count_nodes(root)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            node.color = get_color_for_step(step, total_nodes)  
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()



root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


dfs(root)
print("DFS обход:")
draw_tree(root)


root_bfs = Node(0)
root_bfs.left = Node(4)
root_bfs.left.left = Node(5)
root_bfs.left.right = Node(10)
root_bfs.right = Node(1)
root_bfs.right.left = Node(3)


bfs(root_bfs)
print("BFS обход:")
draw_tree(root_bfs)

