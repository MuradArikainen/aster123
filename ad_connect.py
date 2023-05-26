# import ldap3
import ldap3
from ldap3 import Server, Connection, NTLM, ALL, DIGEST_MD5, SUBTREE

print(1234)

#AD_SERVER = '10.10.103.208'
#AD_USER = 'aster.local\Администратор'
#AD_PASSWORD = '123Qaz'
AD_SEARCH_TREE = 'dc=aster, dc=local'

# соединяюсь с сервером. всё ОК
server = Server(host='10.10.103.208', port=389, get_info=ALL)
conn = Connection(server, auto_bind=True, version=3, client_strategy='SYNC', authentication=NTLM,
                  user='aster.local\Kostya', password='123Qaz!')

print('test')
#print(server.info)
print(conn.bind())
print('test2')

user_dn = "dc=aster,dc=local"
base_dn = "dc=aster,dc=local"
filter = "uid=admin"
total_entries = 0

result = conn.search(search_base='cn=Users,dc=aster,dc=local', search_filter= '(objectClass=Person)', search_scope=SUBTREE, attributes=['telephonenumber','name'])

print(result)
#print(conn.response)

print('----------------------------------------------------------------------')
user_list = conn.entries
user_dict = {}

for user in user_list:
    #print(user)
    #print(type(user))
    print(user['name'], user['telephonenumber'])
    user_dict[str(user['name'])] = str(user['telephonenumber'])

print('----------------------------------------------------------------------')
print(user_dict)
conn.unbind()



