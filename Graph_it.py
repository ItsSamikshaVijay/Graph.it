from tkinter import Tk
from tkinter.ttk import Label
from tkinter import*
import tkinter.font as tkFont
import tkinter as tk
import matplotlib as plt
#matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np  
import matplotlib.pyplot as plt  
import sys
import pandas as pd 
from tkinter import filedialog 
from tkinter.filedialog import askopenfile 

# Creating App class which will contain
# Label Widgets
class App:
    def __init__(self, master) -> None:
  
        # Instantiating master i.e toplevel Widget
        self.master = master
  
        # Creating first Label i.e with default font-

if __name__ == "__main__":

    # Instantiating top level
    root = Tk()
    fontStyle = tkFont.Font(family = 'courier', size =25)
    root_lab = Label(root, text='Graph.it', font ='Times 25 bold italic', bg = 'lightblue')
    root_lab.pack()
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def  continuous():
    # Toplevel object which will
    # be treated as a new window
      newWindow = Toplevel(root)
      
    # sets the title of the
    # Toplevel widget
      newWindow.title("Continuous graph.exe")
    # sets the geometry of toplevel
      newWindow.geometry("800x300")
      newWindow.configure( background = "lightblue")
    # A Label widget to show in toplevel
      label =  Label(newWindow, text ="Continuous graph settings", font = 'Times 25  bold italic ', bg = 'lightblue')
      label.pack()
      label.grid(row = 0, column = 6)
      e1 =tk.StringVar()
      e2 =tk.StringVar()
      e3 = tk.StringVar()
      f = Figure(figsize=(5, 4), dpi=100)
      a = f.add_subplot(111)
      t = arange(0.0, 3.0, 0.01)
      s = sin(2*pi*t)

      a.plot(t, s)
  
      def submit():
 
        formula =e1.get()
        range_graph =e2.get()
        end = e3.get()
        print("The formula is : " + formula)
        print("The y is : " + range_graph)
        def graph(formula,x,y):  
          ran = int(x)
          run = int(y)
          r = range(ran, run)
          x = np.array(r)  
          y = eval(formula)
          plt.plot(x, y)  
          plt.show()
        graph(formula,range_graph, end)
        e1.set("")
        e2.set("")
        e3.set("")
      # creating a label for
# name using widget Label
      e1_label = tk.Label(newWindow, text = 'formula:', font=('calibre',10, 'bold'), bg= 'lightblue')
  
# creating a entry for input
# name using widget Entry
      e1_entry = tk.Entry(newWindow,textvariable = e1, font=('calibre',10,'normal'))
  
# creating a label for password
      e2_label = tk.Label(newWindow, text = 'range:', font = ('calibre',10,'bold'), bg='lightblue')
  
# creating a entry for password
      e2_entry=tk.Entry(newWindow, textvariable = e2, font = ('calibre',10,'normal'))
      e3_label = tk.Label(newWindow, text = 'end:', font=('calibre',10, 'bold'), bg= 'lightblue')
      e3_entry = tk.Entry(newWindow,textvariable = e3, font=('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
      sub_btn=tk.Button(newWindow,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
      e1_label.grid(row= 2,column=5)
      e1_entry.grid(row=3,column=5)
      e2_label.grid(row=4,column=5)
      e2_entry.grid(row=5,column=5)
      e3_label.grid(row=6,column=5)
      e3_entry.grid(row=7,column=5)
      sub_btn.grid(row=8,column=5)
      
      canvas = FigureCanvasTkAgg(f, master=newWindow)
      canvas.draw()
      canvas.get_tk_widget().pack( fill=Tk.BOTH, expand=1)

      toolbar = NavigationToolbar2Tk(canvas, newWindow)
      toolbar.update()
      canvas._tkcanvas.pack( fill=Tk.BOTH, expand=1)
    
      def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)

      canvas.mpl_connect('key_press_event', on_key_event)


      def _quit():
       root.quit()     # stops mainloop
       root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

      button = Tk.Button(master=root, text='Quit', command=_quit)
      button.pack(side=Tk.BOTTOM)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
    def   discrete():
    # Toplevel object which will
    # be treated as a new window
      ws = Tk()
      ws.title('PythonGuides')
      ws.geometry('400x300') 
      ws.configure( background = "lightblue")
      label =  Label(ws, text ="Discrete Graph Settings", font = 'Times 25  bold italic ', bg = 'lightblue')
      label.pack()
      label.grid(row=0, column = 6)
    
      def open_file():
        
          file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
          data = pd.read_csv(file_path)
          x = data['x']
          y = data['y']
          
      def blue():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
        data = pd.read_csv(file_path)
        x = data['x']
        y = data['y']
        plt.scatter(x,y)
        plt.show()

      def  green():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
        data = pd.read_csv(file_path)
        x = data['x']
        y = data['y']
        plt.scatter(x,y, color = 'green')
        plt.show()

      def pink():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
        data = pd.read_csv(file_path)
        x = data['x']
        y = data['y']
        plt.scatter(x,y, color = 'hotpink')
        plt.show()

      def yellow():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
        data = pd.read_csv(file_path)
        x = data['x']
        y = data['y']
        plt.scatter(x,y, color = 'yellow')
        plt.show()


      def uploadFiles():
          pb1 = Progressbar(
              ws, 
              orient=HORIZONTAL, 
              length=300, 
              mode='determinate'
              )
          pb1.grid(row=4, columnspan=3, pady=20)
          for i in range(5):
              ws.update_idletasks()
              pb1['value'] += 20
              time.sleep(1)
          pb1.destroy()
          Label(ws, text='File Uploaded Successfully!', foreground='pink').grid(row=4, columnspan=3, pady=10)
              
          
          
      adhar = Label(
          ws, 
          text='Upload the .csv file here', bg='lightblue'
          )
      adhar.grid(row=5, column=1, padx=10)

      adharbtn = Button(
          ws, 
          text ='Choose File', 
          command = lambda:open_file(),
          bg= 'pink'
          ) 
      adharbtn.grid(row=5, column=2)

      switch_frame = tk.Frame(ws)
      switch_frame.grid(row = 11, column=1)
      Color_switch = Label(
          ws, 
          text='  Choose color for your data', bg='lightblue'
          )
      Color_switch.grid(row=11, column=2, padx=10)
      switch_variable = tk.StringVar(value="off")
      blue_button = tk.Radiobutton(switch_frame, text="blue", variable=switch_variable,
                            indicatoron=False, value="blue", width=8, command= blue)
      green_button = tk.Radiobutton(switch_frame, text="Green", variable=switch_variable,
                            indicatoron=False, value="Green", width=8, command= green)
      pink_button = tk.Radiobutton(switch_frame, text="Pink", variable=switch_variable,
                            indicatoron=False, value="pink", width=8, command=pink)
      yellow_button = tk.Radiobutton(switch_frame, text="yellow", variable=switch_variable,
                             indicatoron=False, value="yellow", width=8, command=yellow)
      blue_button.grid(row= 11, column = 3)
      green_button.grid(row= 11, column =4)
      pink_button.grid(row = 11, column = 5)
      yellow_button.grid(row= 11, column = 6)
     
  
  
    # creating a button for the graphing options:
    root.configure( background = "lightblue")
    button_cont =  Button( root , text ="continuous graph", bd = "10" , bg = 'pink',command = continuous)
    button_cont.pack(side = LEFT , padx = 100, pady = 20)
    button_disc = Button( root , text ="discrete  graph", bd = "10" , bg = 'pink' ,command =  discrete)
    button_disc.pack(side = RIGHT , padx = 100, pady = 20)
    app = App(root)
    root.mainloop()
