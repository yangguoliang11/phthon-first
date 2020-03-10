#coding=utf-8
import time;
import tkinter
from   tkinter import *

G_UIElementArray={'Label_2':None,'Entry_3':None,'Label_4':None,'Entry_5':None,'Button_6':None,'Button_7':None,'Button_8':None,'Button_9':None,'Label_10':None}
#convert
def Button_6():
  G_UIElementArray.get("Entry_5").delete(0, tkinter.END)
  G_UIElementArray.get("Entry_5").insert(0,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(G_UIElementArray.get("Entry_3").get()))))
#today
def Button_7():
  G_UIElementArray.get("Entry_5").delete(0, tkinter.END)
  G_UIElementArray.get("Entry_5").insert(0,time.strftime("%Y-%m-%d 00:00:00", time.localtime()))
  Button_9()
#now
def Button_8():
  G_UIElementArray.get("Entry_5").delete(0, tkinter.END)
  G_UIElementArray.get("Entry_5").insert(0,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
  Button_9()
#unconvert
def Button_9():
  G_UIElementArray.get("Entry_3").delete(0, tkinter.END)
  G_UIElementArray.get("Entry_3").insert(0,int(time.mktime(time.strptime(G_UIElementArray.get("Entry_5").get(),"%Y-%m-%d %H:%M:%S"))))
