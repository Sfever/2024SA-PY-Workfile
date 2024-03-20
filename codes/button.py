#typehints
'''
It's Button!
'''
class button_ins:
    def __init__(self,posx,posy,width,height):
        self.x=posx
        self.y=posy
        self.width=width
        self.height=height
    def onclick(self,action,mousepos):
        if mousepos[0] > self.x:
            if mousepos[1] > self.y:
                if mousepos[0] < self.x+self.width:
                    if mousepos[1] < self.y+self.height:
                        return action()
        return None
class button:
    def __init__(self):
        self.buttonlist=[]
    def new_button(self,posx,posy,width,height):
        new_button=button_ins(posx,posy,width,height)
        self.buttonlist.append(new_button)
        return len(self.buttonlist)-1
    def del_button(self,target):
        del self.buttonlist[target]
