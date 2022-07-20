from tkinter import *
from tkinter import ttk




class Res_cch:
    def __init__(self, root):
        self.root = root
        self.WIDTH = 100
        self.HEIGHT = 200
        
        self.canvas = Canvas(self.root, width = self.WIDTH, height = self.HEIGHT, bg='black') #, bd=5, relief=RAISED
        self.canvas.pack(side='left')
        #self.canvas.create_rectangle(1,1,self.WIDTH, self.HEIGHT, outline='red', width=5)
        self.canvas.create_oval(self.WIDTH // 2 - 15, 20, self.WIDTH // 2 + 15, 50, outline='green', width=2    )
        self.canvas.create_line(self.WIDTH // 2 -5, 25, self.WIDTH // 2, 35, self.WIDTH // 2 + 15,15 , fill='green', width=2    )
    def rsq_pass(self, )
        
        pass
    





class CCheck_win:
    # class for creating main contact check windows
    def __init__(self, root):
        self.root = root
        self.ENTRY_WIDTH = 10
        #add to root setup form
        self.create_frm_setup()
        #add to root result form
        self.create_frm_result()
        
    def create_frm_setup(self):
        #create root setup form with widgets and put it to root
        self.frm_setup = Frame(self.root, bg='red', width=100, height=100)
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
        
        
        pass
    
    def create_frm_result(self):
         #create root result form with widgets and put it to root
        self.frm_result = Frame(self.root, bg='green', width=100, height=100)
        self.frm_result.pack()
        self.res_1_2 = Res_cch(self.frm_result)
        pass






if __name__ == '__main__':
    root = Tk()
    root.title('Contackt check (Van der Pauw)')
    #root.geometry('640x480')
    
    cch = CCheck_win(root)

    root.mainloop()
