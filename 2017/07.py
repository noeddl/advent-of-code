
class Node():

    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.parent = None
        self.children = []
        self.total_weight = int(weight)
        self.visited = False

    def __str__(self):
        return '{} ({})'.format(self.name, self.total_weight)

    def __repr__(self):
        return self.__str__()


class Tree():

    def __init__(self, path):
        self.nodes = {}
        self.root = None
        self.terminals = []

        parent = {}

        # Parse file and create nodes.
        with open(path) as f:
            for line in f:
                line = line.strip()
                sides = line.split(' -> ')
                elems = sides[0].split()
                n = Node(elems[0], elems[1][1:-1])
                self.nodes[n.name] = n

                if len(sides) > 1:
                    children = sides[1].split(', ')
                    for c in children:
                        parent[c] = n.name

        # Add parent and children attributes to nodes.
        for n_name, p_name in parent.items():
            n = self.nodes[n_name]
            p = self.nodes[p_name]
            n.parent = p
            p.children.append(n)

        # Collect terminals.
        for n in self.nodes.values():
            if not n.parent:
                self.root = n
            if not n.children:
                self.terminals.append(n)

    def collect_total_weights(self):
        queue = []
        for t in self.terminals:
            queue.append(t)

        while queue:
            n = queue.pop(0)
            if n.visited:
                continue
            n.visited = True

            if n.parent:
                queue.append(n.parent)
                n.parent.total_weight += n.total_weight

    def find_unbalance(self):
        queue = []
        for t in self.terminals:
            queue.append(t)

        while queue:
            n = queue.pop(0)
            if n.parent:
                queue.append(n.parent)

            weights = {}

            for c in n.children:
                weights.setdefault(c.total_weight, []).append(c)
            
            if len(weights) > 1:
                sorted_weights = sorted(weights, reverse=True)
                wrong_weight = sorted_weights[0]
                right_weight = sorted_weights[1]
                diff = right_weight - wrong_weight
                wrong_child = weights[wrong_weight][0]
                #print(weights, wrong_weight, wrong_child, right_weight, diff)
                #print(wrong_child.children)
                return wrong_child.weight + diff


#path = 'inputs/07_small.txt'
path = 'inputs/07.txt'

t = Tree(path)

# a
print(t.root)

# b
t.collect_total_weights()
corrected_weight = t.find_unbalance()
print(corrected_weight)

