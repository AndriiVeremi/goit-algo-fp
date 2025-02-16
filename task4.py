import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heapify(arr):
    n = len(arr)
    
    def heapify_recursive(i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify_recursive(largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify_recursive(i)
    return arr


def build_heap_tree(arr):
    heap = heapify(arr)
    root = Node(heap[0])

    def insert(node, arr, i=0):
        if i < len(arr):
            new_node = Node(arr[i])
            if 2 * i + 1 < len(arr):
                node.left = new_node
                insert(node.left, arr, 2 * i + 1)
            if 2 * i + 2 < len(arr):
                node.right = new_node
                insert(node.right, arr, 2 * i + 2)

    insert(root, heap)
    return root


arr = [10, 5, 3, 7, 1, 2]
root = build_heap_tree(arr)
draw_tree(root)

