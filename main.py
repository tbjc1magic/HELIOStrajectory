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

def _quit():
    global root
    root.quit()
    root.destroy()


Ne20 =  AtomicMassTable.GetElement(10,20)
H1 =  AtomicMassTable.GetElement(1,1)
Ne21 =  AtomicMassTable.GetElement(10,21)
H2 =  AtomicMassTable.GetElement(1,2)

Ne20_mass = Ne20[3]
H1_mass = H1[3]
Ne21_mass = Ne21[3]
H2_mass = H2[3]


Kr = KINEMATICS()
Kr.m[0] = Ne20_mass 
Kr.m[1] = H2_mass 
Kr.m[2] = Ne21_mass 
Kr.m[3] = H1_mass 
Kr.K0 = 100
Kr.Eex2=0
Kr.Eex3=0

lab2 =[]
K2 = []





def ReturnLines(theta=30):
 
    degree = math.pi/180
    Kr.calculate(theta*degree, 0)
    MagneticFieldB=2
    tr2 =  HELIOS.trajectory(Kr.V2, Kr.thetalab2*degree, 10, Kr.m[2], MagneticFieldB)
    tr3 =  HELIOS.trajectory(Kr.V3, Kr.thetalab3*degree,  1, Kr.m[3], MagneticFieldB)
   
    return tr2,tr3


tr2, tr3 = ReturnLines(30)

#for i in xrange(5000):
#    Kr.randomgenerate()
#    lab2.append(Kr.thetalab2)
#    K2.append(Kr.K2)

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlim([-150,150])
ax.set_ylim([-10,50])
line2 = ax.plot(tr2[0],tr2[1])
line3 = ax.plot(tr3[0],tr3[1],c='r')
ax.axhline(0, color='black')
ax.axvline(0, color='black')

root  = Tkinter.Tk()
root.minsize(width=1000,height=600)
root.protocol("WM_DELETE_WINDOW",_quit)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().place(relwidth=0.6, relheight=0.5,relx=0.05,rely=0.05)



def s2changed(*args):
    thetalab2 = float(args[0])
    tr2,tr3 = ReturnLines(thetalab2)
    line2[0].set_data(tr2[0],tr2[1])
    line3[0].set_data(tr3[0],tr3[1])
    canvas.draw() 

s2 = Tkinter.Scale(root, from_=0.1, to=179, resolution = 0.1,command=s2changed)
s2.set(30)
s2.place(relx = 0.7,rely = 0.1)

#print Kr.m
#Kr.calculate(math.pi/2,1.2)

Tkinter.mainloop()
