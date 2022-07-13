from lakeshore import FastHall
from time import sleep
import json



class CheckContact:
    def __init__(self, fh):
        self.fh = fh
        
    def get_id(self):
        r = self.fh.query('*IDN?')
        print('id: ', r)
        
    def check_contact(self):
        #CCHeck[:VDP]:STARt[:OPTimize]
        self.fh.command('CCHeck:STARt')
        #check contacts
        print('check contacts: ', end='')
        count = 0
        while '1' == fh.query('CCHeck:RUNNing?'):
            sleep(1)
            print('x', end='')
            count += 1
        print(' ', count, 'sec', end='\n')
        
    def get_check_json_summary(self):
        #CCHeck:RESult:JSON[:SUMMary]?
        json_result = fh.query('CCHeck:RESult:JSON?')
        self.cch_res_sum = json.loads(json_result)
        with open('cch_res_sum.txt', 'w') as f:
            print('record ', f.write(json_result))
        #print(json.dumps(result, indent=2))
        
    def get_check_json_all(self):
        #CCHeck:RESult:JSON:ALL?
        json_result = fh.query('CCHeck:RESult:JSON:ALL?')
        self.cch_res_all = json.loads(json_result)
        with open('cch_res_all.txt', 'w') as f:
            print('record ', f.write(json_result))
        #print(json.dumps(result, indent=2))

if __name__ == '__main__':
    fh = FastHall()
    cch = CheckContact(fh)
    cch.get_id()
    
    cch.check_contact()
    cch.get_check_json_summary()
    
    #print(json.dumps(cch.cch_res_all, indent=2))
    pass








# #mesuare resestivity
# print('mesuare resestivity', end='\n')
# #fh.command('RES:START:LINK')
# while '1' == fh.query('RESistivity:RUNNing?'):
#     sleep(1)
#     print('wait2', end=' ')

#measure hall
# print('measure hall', end='\n')
# #fh.command('FAST:START:LINK 1')
# while '1' == fh.query('FAST:RUNN?'):
#     sleep(1)
#     print('wait3', end=' ')
    
    
#print(r1)
#print(fh.query('CCH:RES:STAN?')) 
#print(fh.query('RESistivity:RESult:STANdard?'))
#print(fh.query('RESistivity:RESult:STANdard:SUMMary?'))



'''
fh.query('RESistivity:RESult:STANdard?')
All Results: Returns all measurement data stored.
RESistivity:RESult:JSON:ALL? 1
RESistivity:RESult:STANdard?

fh.query('RESistivity:RESult:STANdard:SUMMary?')
Summary Level Results: Returns the measurement results.
RESistivity:RESult:JSON:SUMMary? 1
RESistivity:RESult:STANdard:SUMMary?
D Data Level Results: Returns calculations taken for a given sample point.
RESistivity:RESult:JSON:DATA? <sample index>, 1
RESistivity:RESult:STANdard:DATA? <sample index>
D Raw Results: Returns the measured voltage, current, and calculated resistance
using current reversal for a given contact configuration and sample point.
RESistivity:RESult:STANdard:RAW? <sample index>, <contact
configuration>

'''
