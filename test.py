'pscode',
'OutputCode',
'PollutantCode',
'psname',
'OutputName',
'PollutantName',
'MonitorTime',
'RevisedStrength',
'RzsStrength',
'RevisedFlow',
'cou',
'S01',
'S03',
'S05',
'StandardValue',

'pscode', 'OutputCode', 'PollutantCode', 'psname', 'PollutantName', 'MonitorTime', 'RevisedStrength', 'RzsStrength', 'RevisedFlow', 'cou', 'S01', 'S03', 'S05', 'StandardValue',

df.rename(
    columns={
        'pollutant_code': 'PollutantCode',
        'outputname': 'OutputName',
        'data_time': 'MonitorTime'
    })

df.rename(
    columns={
        'RevisedzsStrength': 'RzsStrength',
        'flow': 'cou',
        'VALUES01': 'S01',
        'VALUES02': 'S02',
        'VALUES03': 'S03'
    })
