import sys
import Tkinter
import pylab
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from KINEMATICS import KINEMATICS
import AtomicMassTable 
import copy
import math
import matplotlib.pyplot as plt


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

for i in xrange(5000):
    Kr.randomgenerate()
    lab2.append(Kr.thetalab2)
    K2.append(Kr.K2)

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)

line  = ax.plot(lab2,K2,'.')

root  = Tkinter.Tk()
root.protocol("WM_DELETE_WINDOW",_quit)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().place(relwidth=0.8, relheight=0.8,relx=0.1,rely=0.1)

#print Kr.m
#Kr.calculate(math.pi/2,1.2)

Tkinter.mainloop()
