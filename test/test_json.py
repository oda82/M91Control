import json
import matplotlib.pyplot as plt

with open('cch_res_all.txt','r') as f:
    res_json = f.read()
    
data = json.loads(res_json) # json -> dictionary

def pprint(data):
    if type(data) == dict: print(json.dumps(data, indent=2))
    else: print(data)
    pass

#pprint(data)
pprint(data['Setup'])# вывести данные настройки
for i in range(4):    #для каждой контактной пары
    pprint( data["ContactPairIVResults"][i]["ContactPair"])
    pprint( data["ContactPairIVResults"][i][ "RSquared"])
    pprint( data["ContactPairIVResults"][i][ "Slope"])
    pprint( data["ContactPairIVResults"][i][ "Offset"])
    
    
    contacts = data["ContactPairIVResults"][i]["ContactPair"]
    slope = data["ContactPairIVResults"][i][ "Slope"]
    offset = data["ContactPairIVResults"][i][ "Offset"]
    current = []
    voltage = []
    resistance = []
    power = []
    for i_v in data["ContactPairIVResults"][i]["IvCurvePoints"]:
        current.append(i_v["CurrentInAmps"])
        voltage.append(i_v["VoltageInVolts"])
        resistance.append(i_v["ResistanceInOhms"])
        power.append(i_v["CurrentInAmps"] * i_v["VoltageInVolts"])
        
    # voltage vs current
    plt.plot(current, voltage, 'o')
    plt.plot(current, [slope*x+offset for x in current], '-')
    plt.title('voltage vs current contacts {}-{}'.format(contacts["Point1"], contacts["Point2"]))
    plt.xlabel('current')
    plt.ylabel('voltage')
    plt.show()
    # resistance vs current
    plt.plot(current, resistance, 'o')
    plt.plot(current, [sum(resistance)/len(resistance) for i in range(len(resistance)) ], '-')
    plt.title('resistance vs current contacts {}-{}'.format(contacts["Point1"], contacts["Point2"]))
    plt.xlabel('current')
    plt.ylabel('resistance')
    plt.show()
    # power vs current
    plt.plot(current, power, 'o')
#     plt.plot(current, [0.001 for i in range(len(power))], '-')
#     plt.plot(current, [0.005 for i in range(len(power))], '-')
    plt.title('power vs current contacts {}-{}'.format(contacts["Point1"], contacts["Point2"]))
    plt.xlabel('current')
    plt.ylabel('power')
    plt.show()

