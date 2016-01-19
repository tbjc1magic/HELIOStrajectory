import sys
import Tkinter
import pylab
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from KINEMATICS import KINEMATICS
import AtomicMassTable
import copy
import math
import matplotlib.pyplot as plt
import HELIOS
from LINEMANAGER import LINEMANAGER
import functools

def _quit():
    global root
    root.quit()
    root.destroy()

Ne20 =  AtomicMassTable.GetElement(10,20)
H1 =  AtomicMassTable.GetElement(1,1)
Ne21 =  AtomicMassTable.GetElement(10,21)
H2 =  AtomicMassTable.GetElement(1,2)
He4 =  AtomicMassTable.GetElement(2,4)
Na23 =  AtomicMassTable.GetElement(11,23)
Ti48 = AtomicMassTable.GetElement(22,48)
Au197 = AtomicMassTable.GetElement(79,197)

MagneticFieldB =2.
K0=90

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlim([-150,150])
ax.set_ylim([-5,40])
ax.axhline(0, color='black')
ax.axvline(0, color='black')

root  = Tkinter.Tk()
root.minsize(width=1000,height=600)
root.protocol("WM_DELETE_WINDOW",_quit)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().place(relwidth=0.6, relheight=0.9,relx=0.05,rely=0.05)

lm1 = LINEMANAGER( m=[Ne20[3],H2[3],Ne21[3],H1[3]], K0= 88,Eex2=0,Eex3=0, targetCharge2=Ne21[2], targetCharge3=H1[2], MagneticFieldB=MagneticFieldB, axes=ax, c='r')
lm2 = LINEMANAGER( m=[Ne20[3],H2[3],Ne21[3],H1[3]], K0= 40,Eex2=0,Eex3=0, targetCharge2=Ne21[2], targetCharge3=H1[2], MagneticFieldB=MagneticFieldB, axes=ax, c='b')
lm3 = LINEMANAGER( m=[Ne20[3],He4[3],Na23[3],H1[3]], K0= 30.8,Eex2=0,Eex3=0, targetCharge2=Ne21[2], targetCharge3=H1[2], MagneticFieldB=MagneticFieldB, axes=ax, c='purple')
lm4 = LINEMANAGER( m=[Ne20[3],H2[3],Ne21[3],H1[3]], K0= 40,Eex2=2.8,Eex3=0, targetCharge2=Ne21[2], targetCharge3=H1[2], MagneticFieldB=MagneticFieldB, axes=ax, c='black')

StartOfTube = 20
LengthOfTube = 40
WidthOfTube = 1

ax.plot([StartOfTube,StartOfTube+LengthOfTube,StartOfTube+LengthOfTube,StartOfTube,StartOfTube ],
        [-WidthOfTube/2.0,-WidthOfTube/2.0,WidthOfTube/2.0,WidthOfTube/2.0,
            -WidthOfTube/2.0  ] ,c="black" )

originOfbarX = 20
originOfbarY = 20.35
barW = 2.8
barH = 5.1

ax.plot([originOfbarX-barW/2, originOfbarX-barW/2,originOfbarX+barW/2,originOfbarX+barW/2,originOfbarX-barW/2,],
        [ originOfbarY-barH/2,originOfbarY+barH/2,originOfbarY+barH/2,originOfbarY-barH/2,originOfbarY-barH/2,] ,c="black" )

lm = [lm1,lm2,lm3,lm4]

def ScaleChanged(index,*args):
    thetalab2 = float(args[0])
    lm[index].SetLineWithTheta(thetalab2)
    canvas.draw()

for i in xrange(4):
    stmp = Tkinter.Scale(root, from_=0.1, to=179.9, resolution = 0.1, command=functools.partial(ScaleChanged, i), orient = Tkinter.HORIZONTAL)
    stmp.set(60)
    stmp.place(relx = 0.7,rely = 0.1+i*0.1)

############# NavigationToolBar #####################
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
#canvas._tkcanvas.place(relx = 0, rely = 0.95)

Tkinter.mainloop()
