from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import BorderImage
from kivy.uix.popup import Popup
from scilab2py import scilab
from kivy.core.window import Window
from kivy.config import Config
import subprocess
from datetime import datetime
import threading
from kivy.clock import mainthread
import os
import numpy as np
import pygame
import time
import sys
import os.path
p=os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(p)
import main as m
sys.path.remove(p)
#Window.fullscreen = 'auto'
#Window.clearcolor = (0.1, 0.1, 0.1, 1)
#Window.size = (800,600)
class SimulatorApp(App):
    fnm = ''

    def showfc(self,mainimg,fcw,fchooser):
        if (fcw.height == 0):
            fchooser.height = fchooser.parent.height*7
            fcw.height = fcw.parent.height*7
            mainimg.source='no.gif'

    def focus (self,slider,textinput):
        try:
            if (int(textinput.text)>slider.max):
                slider.value = slider.max
                textinput.text = slider.max
            elif (int(textinput.text)<slider.min):
                slider.value = slider.min
                textinput.text = slider.min
            else:
                slider.value = int(textinput.text)
        except:
            print ""

    def SetMaxRGB(self,bandvalue,s1,s2,s3,rvalue,gvalue,bvalue):
        try:
            s1.max = int(bandvalue.text)
            s2.max = int(bandvalue.text)
            s3.max = int(bandvalue.text)
            s1.value = s1.min
            s2.value = s2.min
            s3.value = s3.min
            rvalue.hint_text = "1 - " + bandvalue.text
            gvalue.hint_text = "1 - " + bandvalue.text
            bvalue.hint_text = "1 - " + bandvalue.text
        except:
            print "dd"
    def ButtonImage (self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 1
        otherimg1.opacity = 0.3
        otherimg2.opacity = 0.3
        otherimg3.opacity = 0.3
        otherimg4.opacity = 0.3

    def EnableBand(self,bandvalue):
        if (self.fnm.find(".")==-1):
            print "band"
            bandvalue.disabled = False

    def showmainimg(self,mainimg,fcw,fchooser,s4,s5,s6,s7,rstart,rend,cstart,cend,submitbtn,imgname):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            imgname.text = mainimg.source
            img = pygame.image.load(self.fnm)
            wid=img.get_width()
            hei=img.get_height()
            print wid,hei
            s4.max = hei-100
            s4.min = 1
            s5.max = hei
            s6.max = wid-100
            s6.min = 1
            s7.max = wid
            rstart.readonly = False
            rend.readonly = False
            cstart.readonly = False
            cend.readonly = False
            rstart.hint_text = "1 - " + str(hei-100)
            rend.hint_text = "100 - " + str(hei)
            cstart.hint_text = "1 - " + str(wid-100)
            cend.hint_text = "100 - " + str(wid)
            submitbtn.disabled = False
            s4.disabled = False
            s5.disabled = False
            s6.disabled = False
            s7.disabled = False
        except:
            print fchooser.selection



    def submit(self,s1,s2,s3,s4,s5,s6,s7,mainimg,img1,img2,img3,img4,img5):
        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        subrow = np.matrix("'"+str(s4.value)+","+str(s5.value)+"'")
        subcol = np.matrix("'"+str(s6.value)+","+str(s7.value)+"'")

        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        self.outpath = os.getcwd()+"/"+folder+"/"

        def statPro():
            print("2")
            try:
                scilab.getd(os.getcwd()+"/")
                scilab.imgdisplay(self.fnm,rgb,subrow,subcol,'win4pix.txt',self.outpath)
                dl.dismiss()
                load()
            except Exception as e:
                dl.dismiss()
                print e
            print("3")
        mainimg=mainimg
        img1=img1
        img2=img2
        img3=img3
        img4=img4
        img5=img5
        dl=Popup(title="Process Running",content=Label(text="Please wait untill all calculations and process are done.....!!!") ,size_hint=(None, None), size=(500, 100),auto_dismiss=False)
        dl.open()
        print "before thread"
        t=threading.Thread(target=statPro, args=())
        t.start()
        #t.join()
        print("1")


        #self.load()
        @mainthread
        def load():
            dl.dismiss()
            folder=self.outpath
            img1.source = folder+'out_subset_img.jpg'
            img2.source = folder+'out_original_img.jpg'
            img3.source = folder+'out_hist_band 1.jpg'
            img4.source = folder+'out_hist_band 2.jpg'
            img5.source = folder+'out_hist_band 3.jpg'
            mainimg.source = img1.source
            img1.opacity = 1
            img1.reload()
            img2.reload()
            img3.reload()
            img4.reload()
            img5.reload()
            mainimg.reload()

    def ChangeVal(self,sl1,sl2,hint):
    	sl2.min=int(sl1.value)+100
        sl2.value = sl2.min
        hint.hint_text = str(sl1.value)+" - " + str(sl1.max+100)
    def mainMenu(self):
        App.get_running_app().stop()
        os.chdir("..")
        m.SiplabApp().run()

    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

SimulatorApp().run()
