import os
from scilab2py import scilab
import numpy as np
from Tkinter import Tk
from tkFileDialog import askopenfilename,askdirectory
Tk().withdraw()
if(input("chose all file dir \n1.use current dirrector 2.other:")==1):
    scilab.getd(str(os.getcwd()))
else:
    scilab.getd(str(askdirectory()))
#out=scilab.test(5,6)
#print("this is in test "+ str(out))
#exec('~/usr/share/scilab/contrib/sivp/loader.sce')
#fnm=str(askopenfilename(filetypes = [("Image Files", ("*.jpg", "*.gif")),("JPEG",'*.jpg'),("GIF",'*.gif')]))
fnm=str(askopenfilename())
rgb=np.matrix("'"+str(int(input("Enter R value(1-3): ")))
                      +","+str(int(input("Enter G value: (1-3)")))+","+str(int(input("Enter B value(1-3): ")))+"'")
tp11=0
tp11=0
tp12=0
var1=0
var2=0
print("Enter Enhancement Type")
dec=str(input("1.Linear\n2.Standard Deviation\n3.Histogram\n4.Logarithmic\n5.Exponential\n5.Decorrelation \n:"))
if(dec=='1'):#for liner
    tp11=76
    tp12=110
elif(dec=='2'):#standard deviation stretch
    tp11=83
    var1=float(input("Enter Value1(>0): "))
elif(dec=='3'):#histogram equalization
    tp11=72
elif(dec=='4'):#logarithmic stretch
    tp11=76
    tp12=103
    var1=float(input("Enter Value1(0-255]): "))
elif(dec=='5'):
    tp11=69
    var1=float(input("Enter Value1(0-2): "))
    var2=float(input("Enter Value1(0-255): "))
elif(dec=='6'):
    tp11=68 
else:
    print("invalid input")
outpath=""
if(input("chose all file dir \n1.use current dirrector 2.other")==1):
    outpath=os.getcwd()
else:
    outpath=askdirectory()+'/'
print(fnm+"\n"+str(rgb)+"\n"+str(tp11)+"\n"+str(tp12)+"\n"+str(var1)+"\n"+str(var2)+"\n"+str(outpath))

scilab.enhancement(fnm,rgb,tp11,tp11,tp12,var1,var2,outpath)