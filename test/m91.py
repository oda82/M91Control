from lakeshore import FastHall
from time import sleep
import json




class CCheck:
    def __init__(self, fh=None, view=None):
        self.fh = fh
        self.view = view
        
    def get_id(self):
        r = self.fh.query('*IDN?')
        print('id: ', r)
        
    def check_contact_opt(self, maxCur=0.001, maxVolt=10, points=100, Rsq=0.9999, samp_t=0.1):
        #CCHeck[:VDP]:STARt[:OPTimize]
        #self.fh.command(f'CCHeck:STARt')
        self.fh.command(f'CCHeck:STARt {maxCur},{maxVolt},{points},{Rsq},{samp_t}')
        #check contacts
        print('check contacts: ', end='')
        count = 0
        while '1' == fh.query('CCHeck:RUNNing?'):
            sleep(1)
            print('x', end='')
            count += 1
        print(' ', count, 'sec', end='\n')
    
    def check_contact_man(self, excit='CURRent', start=-0.000001, end=0.000001, ex_range='AUTO',
                          m_range='AUTO', comp=10, points=100, Rsq=0.9999, blan_t=0.01, samp_t=0.1):
        #CCHeck:STARt:MANual CURRent,-10e-6,10e-6,10e-6,100e-3,1.5,20,0.9999,2.4e-3
        self.fh.command(f'CCHeck:STARt:MANual {excit},{start},{end},{ex_range},{m_range},{comp},{points},{Rsq},{blan_t},{samp_t}')        
        #self.fh.command('CCHeck:STARt:MANual CURRent,-10e-6,10e-6,AUTO,100e-3,1.5,20,0.9999,2.4e-3')
        #check contacts
        print('check contacts: ', end='')
        count = 0
        while '1' == fh.query('CCHeck:RUNNing?'):
            sleep(1)
            print('x', end='')
            count += 1
        print(' ', count, 'sec', end='\n')
       
    def get_check_json_all(self):
        #CCHeck:RESult:JSON:ALL?
        json_result = fh.query('CCHeck:RESult:JSON:ALL?')
        self.cch_res_all = json.loads(json_result)
        self.cch_res_all_dumps = json.dumps(self.cch_res_all, indent=2) 
        with open('cch_res_all.txt', 'w') as f:
            print('record ', f.write(self.cch_res_all_dumps))


if __name__ == '__main__':
    fh = FastHall()
    cch = CCheck(fh)
    cch.get_id()

    #cch.check_contact_opt()
    cch.check_contact_man(start=-0.0001, end=0.0001)
    cch.get_check_json_all()