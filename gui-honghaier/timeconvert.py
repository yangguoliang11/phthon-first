#coding=utf-8

#import libs 
import timeconvert_cmd
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Global Varial 
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Global Function 
#Create the root of Kinter 
root = tkinter.Tk()
root.title("Form1")
Form_1= tkinter.Canvas(root,width = 10,height = 4)
Form_1.place(x = 0,y = 0,width = 500,height = 400)
Form_1.configure(bg = "#efefef")
root.geometry("500x400")
#Create the elements of root 
Label_2= tkinter.Label(root,text="时间戳格式",width = 10,height = 4)
Label_2.place(x = 35,y = 64,width = 100,height = 20)
Label_2.configure(bg = "#efefef")
timeconvert_cmd.G_UIElementArray['Label_2']=Label_2
Entry_3= tkinter.Entry(root)
Entry_3.place(x = 127,y = 64,width = 252,height = 113)
Entry_3.configure(relief = "sunken")
timeconvert_cmd.G_UIElementArray['Entry_3']=Entry_3
Label_4= tkinter.Label(root,text="时间格式",width = 10,height = 4)
Label_4.place(x = 24,y = 191,width = 100,height = 20)
timeconvert_cmd.G_UIElementArray['Label_4']=Label_4
Entry_5= tkinter.Entry(root)
Entry_5.place(x = 124,y = 192,width = 255,height = 120)
Entry_5.configure(relief = "sunken")
timeconvert_cmd.G_UIElementArray['Entry_5']=Entry_5
Button_6= tkinter.Button(root,text="转换为时间格式",width = 10,height = 4)
Button_6.place(x = 127,y = 333,width = 100,height = 28)
Button_6.configure(command =timeconvert_cmd.Button_6)
timeconvert_cmd.G_UIElementArray['Button_6']=Button_6
Button_7= tkinter.Button(root,text="今天",width = 10,height = 4)
Button_7.place(x = 241,y = 333,width = 100,height = 28)
Button_7.configure(command =timeconvert_cmd.Button_7)
timeconvert_cmd.G_UIElementArray['Button_7']=Button_7
Button_8= tkinter.Button(root,text="现在",width = 10,height = 4)
Button_8.place(x = 354,y = 331,width = 100,height = 28)
Button_8.configure(command =timeconvert_cmd.Button_8)
timeconvert_cmd.G_UIElementArray['Button_8']=Button_8
Button_9= tkinter.Button(root,text="转换为时间戳",width = 10,height = 4)
Button_9.place(x = 125,y = 368,width = 100,height = 28)
Button_9.configure(command =timeconvert_cmd.Button_9)
timeconvert_cmd.G_UIElementArray['Button_9']=Button_9
Label_10= tkinter.Label(root,text="时间转换工具 1.0 - powerby yangugoliang in 聚通达",width = 10,height = 4)
Label_10.place(x = 42,y = 15,width = 437,height = 20)
timeconvert_cmd.G_UIElementArray['Label_10']=Label_10
root.mainloop()
