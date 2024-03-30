#typehints
class _ButtonInstance:
    def __init__(self,posx,posy,width,height):
        self.x=posx
        self.y=posy
        self.width=width
        self.height=height
    def OnClick(self,action,mousepos):
        if mousepos[0] > self.x:
            if mousepos[1] > self.y:
                if mousepos[0] < self.x+self.width:
                    if mousepos[1] < self.y+self.height:
                        return action()
        return None
class Button:
    def __init__(self):
        self.buttonList:list[_ButtonInstance]=[]
    def NewButton(self,posx,posy,width,height):
        new_button=_ButtonInstance(posx,posy,width,height)
        self.buttonList.append(new_button)
        return len(self.buttonList)-1
    def DeleteButton(self,target):
        del self.buttonList[target]
