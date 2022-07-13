import json

with open('cch_res_all.txt', 'r') as f:
    res_json = f.read()

data = json.loads(res_json)

# res_json_indent = json.dumps(data, indent=2)
# with open('cch_res_all_indent.txt', 'w') as f:
#     f.write(res_json_indent)

def p_indent(data):
    res_json_indent = json.dumps(data, indent=2)
    print(res_json_indent)

p_indent(data['OptimizationDiagnostics']['ContactPairOptimizationResults'][0]['ContactPair']  )
p_indent(data['OptimizationDiagnostics']['ContactPairOptimizationResults'][0]['LastIvCurve']  )

for point in data['OptimizationDiagnostics']['ContactPairOptimizationResults'][0]['LastIvCurve']:
    source = point['Source']
    Current = point['CurrentInAmps']
    Voltage = point['VoltageInVolts']
    Res_m91 = point['ResistanceInOhms']
    Res_V_source = Voltage / source
    Res_V_current = Voltage / Current
    
    print(f'{source}    {Current}    {Voltage}    {Res_V_source}    {Res_V_current}       {Res_m91}  ')
    