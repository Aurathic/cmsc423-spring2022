from itertools import chain

debug = False

#Construct a class that represents a suffix tree
#One possible solution creates a class for a node, which contains the following information:
# - label of edge leading into node from parent (can be either a string or coordinates within the string provided in the input)
# - dictionary of children indexed by the first character on the edges leading into each child.
class Node:
    def __init__(self, parent=None, edge_to=None):
        self.parent = parent
        self.edge_to = edge_to
        self.children = dict()

    def add_child_edge(self, edge):
        if debug:
            print(f"add child {edge} to {self.edge_to}")
        self.children[edge[0]] = Node(self, edge)

    def add_child_node(self, node):
        self.children[node.edge_to[0]] = node

    def remove_child(self, edge):
        del self.children[edge[0]]

    def split(self, j, added_edge):
        parent_edge = self.edge_to[:j]
        new_edge = self.edge_to[j:]
        if debug:
            print(f"split {self.edge_to} into {parent_edge} with children {added_edge} and {new_edge}")
        #create new node N that splits the edge at location of mismatch
        new_parent = Node(self.parent, parent_edge)
        #adjust link from parent and link to child accordingly
        self.parent.remove_child(self.edge_to)
        self.parent.add_child_node(new_parent)
        self.parent = new_parent
        self.edge_to = new_edge
        new_parent.add_child_node(self)
        #create new leaf node as child of N, and label corresponding edge with remainder of suffix
        new_parent.add_child_edge(added_edge)
        return new_parent

    def __str__(self):
        return f"{self.edge_to}::[{', '.join([str(v) for v in self.children.values()])}]"
        #return f"({self.edge_to}::[{', '.join([e + ': ' + str(v) for (e,v) in self.children.items()])}])"


#Start by creating the root - an empty node
#Process the string suffix by suffix, starting from root
#For each suffix s
    #set current node to be the root
    #if current node has a child starting with the first character in s
        #check character by character if suffix matches the label of edge
        #if child reached before suffix is exhausted
            #continue with child as current node, and s as remaining portion of suffix
        #if mismatch found inside the edge
            #create new node N that splits the edge at slocation of mismatch
            #adjust link from parent and link to child accordingly
            #create new leaf node as child of N, and label corresponding edge with remainder of suffix
            #break;
        # Note, due to the $ character, it is not possible for suffix to end
        # in the middle of an edge
        #if current node does not have child starting with first character in s
        #create new leaf node as child of current node
        #label the edge towards the leaf with s.

def suffix_tree(text):
    n = len(text)
    #Start by creating the root - an empty node
    root = Node()
    #Process the string suffix by suffix, starting from root
    #For each suffix s
    for s in range(n):
        suffix = text[s:n]
        if debug:
            print(f"suffix: {suffix}")
        #set current node to be the root
        curr = root
        #if current node has a child starting with the first character in s
        if suffix[0] in curr.children:
            #check character by character if suffix matches the label of edge
            i = 0
            j = None
            continue_loop = True
            while i < n and continue_loop:
                j = 0
                if debug: 
                    print(f"i: {i}, curr: {curr}")
                #if child reached before suffix is exhausted
                if suffix[i] not in curr.children:
                    #continue with child as current node, and s as remaining portion of suffix
                    # TODO I have no idea if this works
                    curr.add_child_edge(suffix[i:])
                    break
                curr = curr.children[suffix[i]]
                while j < len(curr.edge_to):
                    #if mismatch found inside the edge
                    if suffix[i] != curr.edge_to[j]:        
                        #split node into two subnodes 
                        curr.split(j, suffix[i:])
                        # curr = curr.split(j, suffix[i:])
                        continue_loop = False
                        break
                    i += 1
                    j += 1
            # Note, due to the $ character, it is not possible for suffix to end
            # in the middle of an edge
        #if current node does not have child starting with first character in s
        else:            
            #create new leaf node as child of current node
            #label the edge towards the leaf with s.
            curr.add_child_edge(suffix)        
        print(f"{suffix} => {root}")
    return root 

def edges_of_suffix_tree(text):
    return edges_of_suffix_tree_aux(suffix_tree(text))[1:]

def edges_of_suffix_tree_aux(root):
    return [root.edge_to] + \
        list(chain(*[edges_of_suffix_tree_aux(child) for child in root.children.values()]))

## Driver code
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        text = fin.readline() 
        edges = edges_of_suffix_tree(text)
        fout.write("\n".join(edges))


def test(test):
    print(suffix_tree(test))
    print("------")
    print(edges_of_suffix_tree(test))
    #print(suffix_tree("AA$"))

main()


test1 = "ACACCAACA$"
test2 = "AA$"
#test(test1)

"""
None::[C::[CAACA$::[], A::[CCAACA$::[], ACA$::[]]], A::[C::[CAACA$::[], A::[CCAACA$::[], $::[]]], ACA$::[]]]
"""