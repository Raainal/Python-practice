class tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

    def __str__(self,level=0):
        ret = "\t"*level+str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
rootnode=tree("Drinks")
hot=tree("Hot")
cold=tree("Cold")
tea=tree("Tea")
coffee=tree("Coffee")
nonalcoholic=tree("Non-Alcoholic")
alcoholic=tree("Alcoholic")

rootnode.add_child(hot)
rootnode.add_child(cold)
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(nonalcoholic)
cold.add_child(alcoholic)
print(rootnode)