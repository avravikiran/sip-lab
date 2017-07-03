from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from scilab2py import scilab
from kivy.core.window import Window
from kivy.config import Config
#scilab.getd
import os
import numpy as np
import pygame
import os
from datetime import datetime
import math
#Window.fullscreen = 'auto'
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SimulatorApp(App):
    fnm = ''
    def showfc(self,mainimg,fcw,fchooser):
        fchooser.height = fchooser.parent.height*6.5
        fcw.height = fcw.parent.height*6.5
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
    def ButtonImage (self,mainimg,imgtodisp,otherimg1,otherimg2,otherimg3,otherimg4,otherimg5,otherimg6,otherimg7,otherimg8):
        mainimg.source = imgtodisp.source
        imgtodisp.opacity = 1
        otherimg1.opacity = 0.3
        otherimg2.opacity = 0.3
        otherimg3.opacity = 0.3
        otherimg4.opacity = 0.3
        otherimg5.opacity = 0.3
        otherimg6.opacity = 0.3
        otherimg7.opacity = 0.3
        otherimg8.opacity = 0.3

    def showmainimg(self,mainimg,fcw,fchooser,submitbtn):
        fchooser.height = fchooser.parent.height*0
        fcw.height = fcw.parent.height*0
        self.ftype=""
        self.ptype=""
        try:
            mainimg.source=fchooser.selection[0]
            self.fnm = fchooser.selection[0]
            submitbtn.disabled = False
        except:
            print fchooser.selection




    def submit(self,s1,s2,s3,mainimg,cutoff,order,img1,img2,img3,img4,img5,img6,img7,img8,img9,imgname):


        rgb = np.matrix("'"+str(s1.value)+","+str(s2.value)+","+str(s3.value)+"'")
        folder=""
        try:
            now =datetime.now()
            folder="out_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)
            os.mkdir(folder)
        except Exception as ex:
            print("error"+str(ex))
        outpath = os.getcwd()+"/"+folder+"/"

        dec=True
        try:
            print(self.fnm,rgb,self.ptype,cutoff,order,self.ftype,outpath)
            if(self.ftype==""):
                dec=False
            if(self.ptype==""):
                dec=False
            if(self.fnm==""):
                dec=False

        except:
            print("error in variable")
            dec=False

        if(dec):
	    scilab.getd(os.getcwd()+"/")
            scilab.fftfilter(self.fnm,rgb,self.ptype,cutoff,order,self.ftype,outpath)
            img1.source = outpath+'out_original_img.jpg'
            img2.source = outpath+self.ftype+self.ptype+' filteredimg.jpg'
            img3.source = outpath+'out_mag_spectrum_All.jpg'
            mainimg.source = img1.source
            img1.opacity = 1
            imgname.text = img1.source
            img1.reload()
            img2.reload()
            img3.reload()
            mainimg.reload()
            m=set()
            m.add(s1.value)
            m.add(s2.value)
            m.add(s3.value)
            l=[img4,img5,img6,img7,img8,img9]
            for i in range(0,(len(m)*2),2):
                l[i].source=outpath+self.ftype+self.ptype+' filteredimg '+str(int(list(m)[int(math.floor(i/2))]))+'.jpg'
                l[i+1].source=outpath+'out_magnitude_spectrum_'+str(int(list(m)[int(math.floor(i/2))]))+'.jpg'
                l[i].reload()
                l[i+1].reload()
        else:
            Popup(title="Error",content=Label(text="fill all fields properly") ,size_hint=(None, None), size=(600, 400)).open()
            print("fill all fields properly")


    def setFilter(self,s):
    	print(s)
    	self.ftype=s
    def setPass(self,s):
    	print(s)
    	self.ptype=s
    def simulator(self, label):
        try:
            label.text = (eval(label.text))
        except:
            label.text = 'syn error'

#SimulatorApp().run()
