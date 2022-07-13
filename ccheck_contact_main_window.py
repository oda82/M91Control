import tkinter as tk

class CheckContactWindow:
    def __init__(self, root):
        self.root = root #parant window
        self.draw_param() #contact check parameter frame
        self.draw_result() # result check frame
        pass
    
    def draw_param(self):
        frm_param = tk.Frame(self.root)
        frm_param.pack(side=tk.LEFT)
        #row 0
        tk.Label(frm_param, text='Max current').grid(row=0, column=0)
        self.ent_max_current = tk.Entry(frm_param, width=10)
        self.ent_max_current.grid(row=0, column=1)
        #row 1
        tk.Label(frm_param, text='Max voltage').grid(row=1, column=0)
        self.ent_max_voltage = tk.Entry(frm_param, width=10)
        self.ent_max_voltage.grid(row=1, column=1)
        #row 2
        tk.Label(frm_param, text='Min r squared').grid(row=2, column=0)
        self.ent_min_r_squared = tk.Entry(frm_param, width=10)
        self.ent_min_r_squared.grid(row=2, column=1)
        #row 3
        tk.Label(frm_param, text='Number_of_points').grid(row=3, column=0)
        self.ent_number_of_points = tk.Entry(frm_param, width=10)
        self.ent_number_of_points.grid(row=3, column=1)
        #row 4
        self.btn_check_contact = tk.Button(frm_param, text='Check contact')
        self.btn_check_contact.grid(row=4, column=0)
        self.pb_check_contact = tk.ttk.Progressbar(frm_param)
        self.pb_check_contact.grid(row=4, column=1)
        pass
    
    def draw_result(self):
        frm_result = tk.Frame(self.root)
        frm_result.pack(fill=tk.BOTH, side=tk.LEFT)
        
        self.lbl_contact_pair_1 = tk.Label(frm_result, text='contact_pair_1', justify='left')
        self.lbl_contact_pair_1.pack(anchor=tk.NW, side=tk.LEFT)
        self.lbl_contact_pair_2 = tk.Label(frm_result, text='contact_pair_2', justify='left')
        self.lbl_contact_pair_2.pack(anchor=tk.NW, side=tk.LEFT)
        self.lbl_contact_pair_3 = tk.Label(frm_result, text='contact_pair_3', justify='left')
        self.lbl_contact_pair_3.pack(anchor=tk.NW, side=tk.LEFT)
        self.lbl_contact_pair_4 = tk.Label(frm_result, text='contact_pair_4', justify='left')
        self.lbl_contact_pair_4.pack(anchor=tk.NW, side=tk.LEFT)
        
        
        pass





if __name__ == '__main__':
    root = tk.Tk()
    root.title('Check Contact M91 FastHall')
    
    CheckContactWindow(root)
    
    root.mainloop()