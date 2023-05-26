import requests

#result = requests.post(http://10.10.103.233:8088/ari/channels?endpoint=sip%2F101&extension=102&context=my&priority=1&label=101&callerId=101&timeout=30&api_key=ariuser:123456)

base_url = 'http://10.10.103.233:8088/ari/channels'
CALLERID = '102'
EXTEN = '101'

pay_load ={
    'endpoint':'sip/{}'.format(CALLERID),
    'extension':'{}'.format(EXTEN),
    'context':'my',
    'priority':'1',
    'timeout':'30',
    'api_key':'ariuser:123456'
    }

result = requests.post(url=base_url,data=pay_load)

print(result.json())
data_from_ast = result.json()

print(data_from_ast['caller']['name'])

