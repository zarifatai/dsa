class TreeNode:
    def __init__(self, city):
        self.city = city
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    

    def print_tree(self, l):
        spaces = ' ' * 3 * self.level
        prefix = spaces + "|-- " if self.parent else ""
        print(prefix + self.city)
        for child in self.children:
            if child.level <= l:
                child.print_tree(l)
                    
    
    @property
    def level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    ahmedabat = TreeNode("Ahmedabat")
    baroda = TreeNode("Baroda")
    karnataka = TreeNode("Karnataka")
    bangluru = TreeNode("Bangluru")
    mysore = TreeNode("Mysore")
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)
    gujarat.add_child(ahmedabat)
    gujarat.add_child(baroda)
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    california = TreeNode("California")
    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
    

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)
 