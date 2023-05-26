from ldap3 import Server, Connection, NTLM, ALL, DIGEST_MD5, SUBTREE
import pymysql
import random

def get_data_from_ldap(host, port, user, password, search_base):

    #print(1234)

    #AD_SERVER = '10.10.103.208'
    #AD_USER = 'aster.local\Администратор'
    #AD_PASSWORD = '123Qaz'
    AD_SEARCH_TREE = 'dc=aster, dc=local'

    # соединяюсь с сервером. всё ОК
    server = Server(host=host, port=port, get_info=ALL)
    conn = Connection(server, auto_bind=True, version=3, client_strategy='SYNC', authentication=NTLM,
                      user=user, password=password)

    #print('test')
    #print(server.info)
    #print(conn.bind())
    #print('test2')

    user_dn = "dc=aster,dc=local"
    base_dn = "dc=aster,dc=local"
    filter = "uid=admin"
    total_entries = 0

    result = conn.search(search_base=search_base, search_filter= '(objectClass=Person)', search_scope=SUBTREE, attributes=['telephonenumber','name'])

    #print(result)
    #print(conn.response)

    #print('----------------------------------------------------------------------')
    user_list = conn.entries
    user_dict = {}

    for user in user_list:
        #print(user)
        #print(type(user))
        #print(user['name'], user['telephonenumber'])
        user_dict[str(user['name'])] = str(user['telephonenumber'])

    #print('----------------------------------------------------------------------')
    #print(user_dict)
    conn.unbind()
    return user_dict

if __name__ == '__main__':
    host = '10.10.103.208'
    port = 389
    user = 'aster.local\Kostya'
    password = '123Qaz!'
    search_base = 'cn=Users,dc=aster,dc=local'
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    user_dict = get_data_from_ldap(host, port, user, password, search_base)
    print('!!!!!!!!!!!!!!!!!!!!!!!!')
    print(user_dict)

    m_conn = pymysql.connect(host='10.10.103.233', port = 3306, user = 'ldap', password = '123456', database='testast')
    cursor = m_conn.cursor()
    for element in user_dict:
        print(element)
        print(user_dict[element])
        if user_dict[element] != '[]':
            select_line = f'select count(*) from sip where name = "{element}"'
            cursor.execute(select_line)
            result = int(cursor.fetchall()[0][0])
            print(result)
            if result == 0:
                for n in range(5):
                    passwd = ''
                    for i in range(6):
                        passwd += random.choice(chars)

                print(passwd)
                sql_line = f'insert into sip values ("{element}","{passwd}","{user_dict[element]}")'
                cursor.execute(sql_line)
    m_conn.commit()