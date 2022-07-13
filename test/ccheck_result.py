{'SampleType': 0,
 'ContactPairIVResults': [
    {'ContactPair': {'Point1': 1, 'Point2': 2},
     'Offset': -0.0007002966546996527,
     'Slope': 677.655206498274,
     'RSquared': 0.9999967453199577,
     'RSquaredPass': True,
     'InCompliance': False,
     'VoltageOverload': False,
     'CurrentOverload': False},
    {'ContactPair': {'Point1': 2, 'Point2': 3},
     'Offset': -0.00021208247809857957,
     'Slope': 691.3397736632312,
     'RSquared': 0.9999994052827728,
     'RSquaredPass': True,
     'InCompliance': False,
     'VoltageOverload': False,
     'CurrentOverload': False},
    {'ContactPair': {'Point1': 3, 'Point2': 4},
     'Offset': -0.00010671980256721605,
     'Slope': 689.8607603934051,
     'RSquared': 0.9999996475462598,
     'RSquaredPass': True,
     'InCompliance': False,
     'VoltageOverload': False,
     'CurrentOverload': False},
    {'ContactPair': {'Point1': 4, 'Point2': 1},
     'Offset': -7.198124957054109e-05,
     'Slope': 681.7803465268462,
     'RSquared': 0.999999701549316,
     'RSquaredPass': True,
     'InCompliance': False,
     'VoltageOverload': False,
     'CurrentOverload': False}],
 'InCompliance': False,
 'VoltageOverload': False,
 'CurrentOverload': False,
 'StartTime': '2022-07-06T03:57:52.276437+00:00',
 'EndTime': '2022-07-06T03:58:14.095057+00:00',
 'DurationInSeconds': 21.818}



ccheck_results['ContactPairIVResults'][0]
{'ContactPair': {'Point1': 1, 'Point2': 2},
 'Offset': -0.0007002966546996527,
 'Slope': 677.655206498274,
 'RSquared': 0.9999967453199577,
 'RSquaredPass': True,
 'InCompliance': False,
 'VoltageOverload': False,
 'CurrentOverload': False}

>>> ccheck_results['ContactPairIVResults'][1]
{'ContactPair': {'Point1': 2, 'Point2': 3}, 'Offset': -0.00021208247809857957, 'Slope': 691.3397736632312, 'RSquared': 0.9999994052827728, 'RSquaredPass': True, 'InCompliance': False, 'VoltageOverload': False, 'CurrentOverload': False}
>>> ccheck_results['ContactPairIVResults'][2]
{'ContactPair': {'Point1': 3, 'Point2': 4}, 'Offset': -0.00010671980256721605, 'Slope': 689.8607603934051, 'RSquared': 0.9999996475462598, 'RSquaredPass': True, 'InCompliance': False, 'VoltageOverload': False, 'CurrentOverload': False}
>>> ccheck_results['ContactPairIVResults'][3]
{'ContactPair': {'Point1': 4, 'Point2': 1}, 'Offset': -7.198124957054109e-05, 'Slope': 681.7803465268462, 'RSquared': 0.999999701549316, 'RSquaredPass': True, 'InCompliance': False, 'VoltageOverload': False, 'CurrentOverload': False}
>>> ccheck_results['ContactPairIVResults'][4]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
IndexError: list index out of range
>>> 
