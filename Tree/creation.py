class Treenode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret =" " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addchild(self, Treenode):
        self.children.append(Treenode)

tree=Treenode("Drinks",[])
cold=Treenode("Cold",[])
hot=Treenode("Hot",[])
tree.addchild(cold)
tree.addchild(hot)
cola=Treenode("Cola",[])
fanta=Treenode("Fanta",[])
tea=Treenode("Tea",[])
coffee=Treenode("Coffee",[])
cold.addchild(cola)
cold.addchild(fanta)
hot.addchild(tea)
hot.addchild(coffee)


print(tree)