class father:
    def __init__(self):
        print("Father class constructor")

class son(father):
    def __init__(self):
        print("Son class constructor")
       # super().__init__()
obj=son()