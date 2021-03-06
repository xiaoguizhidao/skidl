from skidl import SKIDL, TEMPLATE, Part, Pin, SchLib

SKIDL_lib_version = '0.0.1'

analog_switches = SchLib(tool=SKIDL).add_parts(*[
        Part(name='ADG729',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='CPC1017N',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH OPTO',description='opto mos',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='ANOD',do_erc=True),
            Pin(num='2',name='CATH',do_erc=True),
            Pin(num='3',name='INOUT2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='INOUT1',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='DG308',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Quad Analog Switches',ref_prefix='U',num_units=4,do_erc=True,aliases=['DG441'],pins=[
            Pin(num='4',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='ON',do_erc=True),
            Pin(num='2',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='ON',do_erc=True),
            Pin(num='9',name='ON',do_erc=True),
            Pin(num='10',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='11',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='15',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='16',name='ON',do_erc=True)]),
        Part(name='DG309',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Quad Analog Switches',ref_prefix='U',num_units=4,do_erc=True,aliases=['DG442'],pins=[
            Pin(num='4',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='OFF',do_erc=True),
            Pin(num='2',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='OFF',do_erc=True),
            Pin(num='9',name='OFF',do_erc=True),
            Pin(num='10',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='11',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='15',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='16',name='OFF',do_erc=True)]),
        Part(name='DG417',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Analog Switch ( 8pins)',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VCC',do_erc=True),
            Pin(num='6',name='OFF',do_erc=True),
            Pin(num='8',name='O/I',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='DG418',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Analog Switch ( 8pins)',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VCC',do_erc=True),
            Pin(num='6',name='ON',do_erc=True),
            Pin(num='8',name='O/I',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='DG419',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Analog Switch ( 8pins)',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='COM',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='B',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VCC',do_erc=True),
            Pin(num='6',name='A/B',do_erc=True),
            Pin(num='8',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='DG9421',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH',description='Analog Switch ( 6pins TSOP)',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='I/O',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='O/I',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='ON',do_erc=True)]),
        Part(name='LAA110',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH OPTO',description='opto mos 2 controls, 2 switches, norm OFF',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='1',name='ANOD',do_erc=True),
            Pin(num='2',name='CATH',do_erc=True),
            Pin(num='7',name='INOUTB1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='INOUTA1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='ANOD',do_erc=True),
            Pin(num='4',name='CATH',do_erc=True),
            Pin(num='5',name='INOUTB1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='INOUTA1',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LBB110',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH OPTO',description='opto mos 2 controls, 2 switches',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='1',name='ANOD',do_erc=True),
            Pin(num='2',name='CATH',do_erc=True),
            Pin(num='7',name='INOUTB1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='INOUTA1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='ANOD',do_erc=True),
            Pin(num='4',name='CATH',do_erc=True),
            Pin(num='5',name='INOUTB1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='INOUTA1',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LCC110',dest=TEMPLATE,tool=SKIDL,keywords='SWITCH OPTO',description='opto mos 1 control, 2 switches A/B',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='2',name='ANOD',do_erc=True),
            Pin(num='3',name='CATH',do_erc=True),
            Pin(num='5',name='INOUTB2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='INOUTA2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='INOUTB1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='INOUTA1',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='DG884',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='HI524',dest=TEMPLATE,tool=SKIDL,do_erc=True)])
