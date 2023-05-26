from shared_func import get_config_data, connect_to_ast

def call_to(tc, CALLERID, EXTEN):
    CH_STR = bytes('Channel: SIP/{}\n'.format(CALLERID), 'utf-8')
    EXT_STR = bytes('Exten: {}\n'.format(EXTEN), 'utf-8')
    CID_STR = bytes('Callerid: {}\n'.format(CALLERID), 'utf-8')
    tc.write(b'\n')
    tc.write(b'Action: Originate\n')
    tc.write(CH_STR)
    tc.write(b'Context: my\n')
    tc.write(EXT_STR)
    tc.write(b'Priority: 1\n')
    tc.write(CID_STR)
    tc.write(b'\n')
    tc.write(b'\n')

if __name__ == '__main__':
    ast_ip, ast_port, ast_events = get_config_data()
    tc = connect_to_ast(ast_ip, ast_port)
    EXTEN = '102'
    CALLERID = '101'
    call_to(tc,CALLERID,EXTEN)
