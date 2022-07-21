from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import json

from lakeshore import FastHall

with open('cch_res_all.txt','r') as f:
    res_json = f.read()
    
data = json.loads(res_json) # json -> dictionary


class Res_cch():
    """ class for show the resalts of contact pairs check in rectangular form"""
    def __init__(self, root, num):
        self.root = root
        self.num = num #number of contacr pair 0 to 3
        #size of result windows
        self.WIDTH = 100
        self.HEIGHT = 200
        #number of contact
        self.point1 = None
        self.point2 = None
        
        self.offset = StringVar()
        self.offset.set('offset = ?')
        self.slope = StringVar()
        self.slope.set('slope = ?')
        self.r_squared = StringVar()
        self.r_squared.set('Rsq = ?')
        
        self.r_squared_pass = None
        self.in_compliance = None
        self.voltage_overload = None
        self.current_overload = None
         
        self.current = []
        self.voltage = []
        self.resistance = []
        self.power = []
        
        self.draw_window()
        self.update_window(data)#<-----change
        
    def update_window(self, data):
        """ take data type of dict, parse it and show in form"""
        # data["ContactPairIVResults"][i]["ContactPair"]['Point1']
        #clear contact color
        for contact in self.contacts:
            contact.config(bg='SystemButtonFace')
        #set measurable contact
        self.point1 = data["ContactPairIVResults"][self.num]["ContactPair"]['Point1']-1
        self.contacts[self.point1].config(bg='green')
        self.point2 = data["ContactPairIVResults"][self.num]["ContactPair"]['Point2']-1
        self.contacts[self.point2].config(bg='green')
        
        self.r_squared.set('Rsq = {:.8f}'.format(data["ContactPairIVResults"][self.num]["RSquared"]))
        self.slope.set('slope = {:.2f} Ohm'.format( data["ContactPairIVResults"][self.num]["Slope"]))
        self.f_slope = data["ContactPairIVResults"][self.num]["Slope"]
        self.offset.set('offset = {:.6f} V'.format( data["ContactPairIVResults"][self.num]["Offset"]))
        self.f_offset = data["ContactPairIVResults"][self.num]["Offset"]
    
        self.r_squared_pass = data["ContactPairIVResults"][self.num]["RSquaredPass"]
        self.lbl_r_squared_pass['bg'] = 'green' if self.r_squared_pass else 'red'
        
        self.in_compliance = data["ContactPairIVResults"][self.num]["InCompliance"]
        self.lbl_in_compliance['bg'] = 'red' if self.in_compliance else 'green'
        
        self.voltage_overload = data["ContactPairIVResults"][self.num]["VoltageOverload"]
        self.lbl_voltage_overload['bg'] = 'red' if self.voltage_overload else 'green'
        
        self.current_overload = data["ContactPairIVResults"][self.num]["CurrentOverload"]
        self.lbl_current_overload['bg'] = 'red' if self.current_overload else 'green'
        #take points from json for different measurement
        self.current = []
        self.voltage = []
        self.resistance = []
        self.power = []
        
        for i_v in data["ContactPairIVResults"][self.num]["IvCurvePoints"]:
            self.current.append(i_v["CurrentInAmps"])
            self.voltage.append(i_v["VoltageInVolts"])
            self.resistance.append(i_v["ResistanceInOhms"])
            self.power.append(i_v["CurrentInAmps"] * i_v["VoltageInVolts"])
    
    def draw_window(self):

        self.frm_root = Frame(self.root, width=self.WIDTH, height=self.HEIGHT, relief=GROOVE, borderwidth=3)#, bg='blue'
        self.frm_root.pack(side=LEFT, padx=5, pady=5, ipadx=2, ipady=2)
        
        self.lbl_r_squared_pass = Label(self.frm_root, text='Rsq Pass', bg='red')
        self.lbl_r_squared_pass.grid(row=1, column=0, columnspan=2)
        self.lbl_in_compliance = Label(self.frm_root, text='In Compliance', bg='red')
        self.lbl_in_compliance.grid(row=2, column=0, columnspan=2)
        self.lbl_voltage_overload = Label(self.frm_root, text='Voltage Overload', bg='red')
        self.lbl_voltage_overload.grid(row=3, column=0, columnspan=2)
        self.lbl_current_overload = Label(self.frm_root, text='Current Overload', bg='red')
        self.lbl_current_overload.grid(row=4, column=0, columnspan=2)
        
        self.contacts = []
        self.contacts.append(Label(self.frm_root, text='1'))
        self.contacts[0].grid(row=5, column=0, columnspan=2)
        self.contacts.append(Label(self.frm_root, text='2'))
        self.contacts[1].grid(row=6, column=0, sticky=E, padx=10)
        self.contacts.append(Label(self.frm_root, text='3'))
        self.contacts[2].grid(row=7, column=0, columnspan=2)
        self.contacts.append(Label(self.frm_root, text='4'))
        self.contacts[3].grid(row=6, column=1, sticky=W, padx=10)
        
        
        Label(self.frm_root, textvariable=self.r_squared).grid(row=8, column=0, columnspan=2)
        Label(self.frm_root, textvariable=self.slope).grid(row=9, column=0, columnspan=2)
        Label(self.frm_root, textvariable=self.offset).grid(row=10, column=0, columnspan=2)
        self.btn_show_graph = Button(self.frm_root, text='Show Graph', command=self.show_graph).grid(row=11, column=0, columnspan=2, pady=5)
        
    def show_graph(self):
        fig, axs = plt.subplots(3,1)
        # voltage vs current
        points, = axs[0].plot(self.current, self.voltage, 'o')
        points.set_label('V(I)')
        points, = axs[0].plot(self.current, [self.f_slope*x+self.f_offset for x in self.current], '-')
        points.set_label('{:.2f}*x+{:.6f}'.format(self.f_slope, self.f_offset))
        axs[0].legend()
        axs[0].set_ylabel('voltage')
        axs[0].set_title('contacts {} - {}'.format(self.point1 + 1, self.point2 + 1))
        # resistance vs current
        points, = axs[1].plot(self.current, self.resistance, 'o')
        points.set_label('R(I)')
        points, = axs[1].plot(self.current, [self.f_slope for i in range(len(self.resistance)) ], '-')
        points.set_label('R = {:.2f} Ohm'.format(self.f_slope))
        axs[1].legend()
        axs[1].set_ylabel('resistance')
        # power vs current
        points, = axs[2].plot(self.current, self.power, 'o')
        points.set_label('P(I)')
        axs[2].legend()
        axs[2].set_xlabel('current')
        axs[2].set_ylabel('power')
        plt.show()
        pass
        
  
class CCheck_win():
    # class for creating main contact check windows
    def __init__(self, root):
        self.root = root
        self.ENTRY_WIDTH = 10
        #add to root setup form
        self.create_frm_setup()
        #add to root result form
        self.create_frm_result()
        #add to root coment form with open and save buttons
        self.create_frm_comment()
        
    def create_frm_setup(self):
        #create root setup form with widgets and put it to root
        self.frm_setup = Frame(self.root, width=100, height=100)#, bg='red'
        self.frm_setup.pack()
        #row0
        Label(self.frm_setup, text='Performs a contact check measurement on contact pairs \n1-2, 2-3, 3-4, and 4-1 for a van der Pauw sample.').grid(row=0, column=0, columnspan=3, padx=10, pady=3)
        #row1
        Label(self.frm_setup, text='Excitation Type:').grid(row=1, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=1, column=1)       
        Label(self.frm_setup, text='VOLTage, CURRent').grid(row=1, column=2, sticky='w', padx=10, pady=3)
        #row2
        Label(self.frm_setup, text='Excitation Start Value:').grid(row=2, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=2, column=1)
        Label(self.frm_setup, text='range from -0.1 to 0.1 A').grid(row=2, column=2, sticky='w', padx=10, pady=3)
        #row3
        Label(self.frm_setup, text='Excitation End Value:').grid(row=3, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=3, column=1)
        Label(self.frm_setup, text='range from -0.1 to 0.1 A').grid(row=3, column=2, sticky='w', padx=10, pady=3)
        #row4
        Label(self.frm_setup, text='Excitation Range:').grid(row=4, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=4, column=1)
        Label(self.frm_setup, text='range from 0 to 0.1 A or AUTO').grid(row=4, column=2, sticky='w', padx=10, pady=3)
        #row5
        Label(self.frm_setup, text='Measurement Range:').grid(row=5, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=5, column=1)
        Label(self.frm_setup, text='range from 0 to 10 V').grid(row=5, column=2, sticky='w', padx=10, pady=3)
        #row6
        Label(self.frm_setup, text='Compliance Limit:').grid(row=6, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=6, column=1)
        Label(self.frm_setup, text='range from 1 to 10 V').grid(row=6, column=2, sticky='w', padx=10, pady=3)
        #row7
        Label(self.frm_setup, text='Number Of Points:').grid(row=7, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=7, column=1)
        Label(self.frm_setup, text='range from 0 to 100').grid(row=7, column=2, sticky='w', padx=10, pady=3)
        #row8
        Label(self.frm_setup, text='Minimum R Squared:').grid(row=8, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=8, column=1)
        Label(self.frm_setup, text='DEFault = 0.9999').grid(row=8, column=2, sticky='w', padx=10, pady=3)
        #row9
        Label(self.frm_setup, text='Blanking Time:').grid(row=9, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=9, column=1)
        Label(self.frm_setup, text='DEFault=2ms min=0.5ms max=300s').grid(row=9, column=2, sticky='w', padx=10, pady=3)
        #row10
        Label(self.frm_setup, text='Sampling Time:').grid(row=10, column=0, sticky='e', padx=10, pady=3)
        Entry(self.frm_setup, width=self.ENTRY_WIDTH).grid(row=10, column=1)
        Label(self.frm_setup, text='DEFault=1/60s min=0.010ms max=1s').grid(row=10, column=2, sticky='w', padx=10, pady=3)
        #row11
        Button(self.frm_setup, text='Contact Check').grid(row=11, column=0, sticky='e', padx=10, pady=3)
        ttk.Progressbar(self.frm_setup).grid(row=11, column=1)
        Button(self.frm_setup, text='Stop/Reset').grid(row=11, column=2, sticky='w', padx=10, pady=3)
    
    def create_frm_result(self):
         #create root result form with widgets and put it to root
        self.frm_result = Frame(self.root)
        self.frm_result.pack()
        self.result = []
        for i in range(4):
            self.result.append(Res_cch(self.frm_result, i))
        
    def create_frm_comment(self):
        self.frm_comment = Frame(self.root, width=100, height=100)#, bg='green'
        self.frm_comment.pack(fill=BOTH)
        Label(self.frm_comment, text='Comment:').pack(anchor='w', padx=5)#, bg='red'
        Text(self.frm_comment, height=5, width=30).pack(fill=BOTH, expand=True, padx=5, pady=5)
        Button(self.frm_comment, text='Open').pack(side=LEFT, padx=5, pady=3)
        Button(self.frm_comment, text='Save').pack(side=LEFT, padx=5, pady=3)
#-------------------END OF MAIN WINDOW class CCheck_win()-----------------------
    
class CCheck_ctrl():
    def __init__(self, view):
        self.view = view
        pass
    
    pass


if __name__ == '__main__':
    root = Tk()
    root.title('Contackt check (Van der Pauw)')
    #root.geometry('640x480')

    cch_view = CCheck_win(root)
    cch_ctrl = CCheck_ctrl(cch_view)

    root.mainloop()
