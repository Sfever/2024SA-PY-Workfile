'''
This file is used to display and operate any type of text in the game
All texts should use this file
Please do not use your own implentation
'''
#typehints
import pygame as pg #导入pygame储存为pg库方便后续调用
class textobj:  #类textobj方便后续调用
    text=""     #定义文本类
    surface=""  #定义文本类
    color=[]    #定义文本类
    font=""     #定义文本类
    title=""    #定义文本类    （选择变量类型）
    def __init__(self):#初始化
        self.text=""
        self.surface=""
        self.color=[255,255,255] #设置初始颜色？
        self.size=30             #设置初始大小？
        self.font="arial"        #设置初始字体？
        self.title="Fuck this world" #设置标题
    def set_color(self,color:list):  #设置颜色清单？  （这一块在创建变量？）
        self.color=color
    def set_font(self, font:str):    
        self.font=font
    def set_size(self,size:int):
        self.size=size
    def set_content(self,content:str):
        self.title=content
    def set_text(self):
        self.text=pg.font.SysFont(self.font,self.size)  #这一块才是设置变量的值？
    def render_surface(self):
        self.surface=self.text.render(self.title,True,tuple(self.color))
    def get_text(self):
        return self.text#returns the object of font
    def get_surface(self):
        return self.surface#returns rendered surface
    def get_dimensions(self):
        return self.text.size(self.title)
    def delete_text(self):
        self.surface.set_alpha(0)#make surface invisible
        pg.display.update()
        print("Successed to remove text") #设置完了print出来？

class textview:
    def __init__(self): #初始化
        self.textlist=[]
    def new_text(self):  #新建文本对象？（什么ppt操作）
        newtext=textobj()
        self.textlist.append(newtext)
        return len(self.textlist)-1
    def del_text(self,tgt):    #删除文本对象？
        self.textlist[tgt].delete_text()
        del self.textlist[tgt]#remove it and make become not accessible anymore
        #print("Successed to remove text")
    '''
    self.textlist will not be provided outside the class in order to prevent losting access to textobj object accidentally
    '''
    #returns the instance of textobj for devs to work on
    '''
    def get_object(self,index):
        return self.textlist[index]
    Just for idiots, i think don't give 'em text object either
    '''