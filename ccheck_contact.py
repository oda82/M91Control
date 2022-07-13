import tkinter as tk
from threading import Thread

from lakeshore import FastHall
from lakeshore import ContactCheckOptimizedParameters
from ccheck_contact_main_window import CheckContactWindow




class CheckContact:
    def __init__(self, view):
        self.view = view # pinter to view
        # Connect to the first available FastHall over USB
        self.fh_m91 = FastHall()
        # Create an optimized contact check settings object with default parameters
        self.ccheck_settings = ContactCheckOptimizedParameters()
        
        self.show_ccheck_settings() #показать параметры контактов по умолчанию
        self.bind_widget() # связать кнопку с обработчиком
        
    def show_ccheck_settings(self):
         self.view.ent_max_current.insert(0, self.ccheck_settings.max_current)
         self.view.ent_max_voltage.insert(0, self.ccheck_settings.max_voltage)
         self.view.ent_min_r_squared.insert(0, self.ccheck_settings.min_r_squared)
         self.view.ent_number_of_points.insert(0, self.ccheck_settings.number_of_points)

    def bind_widget(self):
        self.view.btn_check_contact.bind('<Button-1>', self.run_contackt_check)
        pass
    
    def show_ccheck_results(self):
        text = []
        for i in range(4):
            cpair = self.ccheck_results['ContactPairIVResults'][i]
            text.append('Point {}-{}\nR^2= {}\nR^2 Pass: {}\nIn Compliance: {}\nVoltage Overload: {}\nCurrent Overload: {}'.format(
                cpair['ContactPair']['Point1'],
                cpair['ContactPair']['Point2'],
                cpair['RSquared'],
                cpair['RSquaredPass'],
                cpair['InCompliance'],
                cpair['VoltageOverload'],
                cpair['CurrentOverload']))
            
        self.view.lbl_contact_pair_1['text'] = text[0]
        if cpair['RSquaredPass']: self.view.lbl_contact_pair_1.config(bg='green')
        else: self.view.lbl_contact_pair_1.config(bg='red')
        
        self.view.lbl_contact_pair_2['text'] = text[1]
        if cpair['RSquaredPass']: self.view.lbl_contact_pair_2.config(bg='green')
        else: self.view.lbl_contact_pair_2.config(bg='red')
        
        self.view.lbl_contact_pair_3['text'] = text[2]
        if cpair['RSquaredPass']: self.view.lbl_contact_pair_3.config(bg='green')
        else: self.view.lbl_contact_pair_3.config(bg='red')
        
        self.view.lbl_contact_pair_4['text'] = text[3]
        if cpair['RSquaredPass']: self.view.lbl_contact_pair_4.config(bg='green')
        else: self.view.lbl_contact_pair_4.config(bg='red')
        pass
    
    
    def run_contackt_check(self, event):
        #read check setting
        max_current = float(self.view.ent_max_current.get())
        max_voltage = float(self.view.ent_max_voltage.get()) 
        min_r_squared = float(self.view.ent_min_r_squared.get())
        number_of_points = int(self.view.ent_number_of_points.get())
        print(f'Max I = {max_current}, Max V = {max_voltage}, Min R^2 = {min_r_squared}, Points = {number_of_points}')
        # Create an optimized contact check settings object with user parameters
        self.ccheck_settings = ContactCheckOptimizedParameters(
            max_current = max_current,
            max_voltage = max_voltage,
            min_r_squared = min_r_squared,
            number_of_points = number_of_points)
        def run():
            #run progressbar
            self.view.pb_check_contact.start()
            #disabled button
            self.view.btn_check_contact['state'] ='disabled'
            # Run the optimized contact check to automatically determine the best parameters for the sample
            self.ccheck_results = self.fh_m91.run_complete_contact_check_optimized(self.ccheck_settings)
            #print(self.ccheck_results)
            self.show_ccheck_results()
            #stop progressbar
            self.view.pb_check_contact.stop()
            #enabled button
            self.view.btn_check_contact['state'] ='normal'
            
        thread = Thread(target=run)
        thread.start()

        pass
        

    



if __name__ == '__main__':
    root = tk.Tk()
    root.title('Check Contact M91 FastHall')
    
    view = CheckContactWindow(root)
    CheckContact(view)
    
    root.mainloop()