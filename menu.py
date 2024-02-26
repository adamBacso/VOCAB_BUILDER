class MenuItem:
    def __init__(self,name,parent:MenuItem=None,action=None): # TODO: implement forward declaration of MenuItem
        self.name = name
        self.parent = parent
        self.action = action
        
        self.children = []

        if self.parent is not None:
            self.parent.add_child(self)
            self.layer = self.parent.layer + 1
        else:
            self.layer = 0

    def add_child(self,child):
        self.children.append(child)
    
    def display_children(self):
        print(self.name)
        for i in range(len(self.children)):
            print("\t{}. {}".format(i+1, self.children[i]))
        print(len(self.children)+1 + ". Back")
    
    def ascend_layer(self):
        pass

class Menu:
    def __init__(self):
        self.root = MenuItem("root")
        self.translate = MenuItem("translate",root)
        self.settings = MenuItem("settings",root)
        self.quit = MenuItem("quit",root)
    
    def show_menu(self):
        self.root.display_children()

Menu.show_menu()