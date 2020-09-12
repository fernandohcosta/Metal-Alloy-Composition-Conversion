# AUTHOR: Fernando Henrique da Costa <fernando.henriquecosta@yahoo.com.br>
# DATE CREATED: 11/09/2020

import re

#Dictionary with the elements and their atomic masses
atomic_mass = {'H':1.00797, 'He':4.0026, 'Li':6.941, 'Be':9.01218, 'B':10.81,
    'C':12.011, 'N':14.0067, 'O':15.9994, 'F':18.998403, 'Ne':20.179, 'Na':22.98977,
    'Mg':24.305, 'Al':26.98154, 'Si':28.0855, 'P':30.97376, 'S':32.06, 'Cl':35.453,
    'K':39.0983, 'Ar':39.948, 'Ca':40.08, 'Sc':44.9559, 'Ti':47.9, 'V':50.9415,
    'Cr':51.996, 'Mn':54.938, 'Fe':55.847, 'Ni':58.7, 'Co':58.9332, 'Cu':63.546,
    'Zn':65.38, 'Ga':69.72, 'Ge':72.59, 'As':74.9216, 'Se':78.96,
    'Br':79.904, 'Kr':83.8, 'Rb':85.4678, 'Sr':87.62, 'Y':88.9059,
    'Zr':91.22, 'Nb':92.9064, 'Mo':95.94, 'Tc':98, 'Ru':101.07,
    'Rh':102.9055, 'Pd':106.4, 'Ag':107.868, 'Cd':112.41, 'In':114.82,
    'Sn':118.69, 'Sb':121.75, 'I':126.9045, 'Te':127.6, 'Xe':131.3,
    'Cs':132.9054, 'Ba':137.33, 'La':138.9055, 'Ce':140.12, 'Pr':140.9077,
    'Nd':144.24, 'Pm':145, 'Sm':150.4, 'Eu':151.96, 'Gd':157.25, 'Tb':158.9254,
    'Dy':162.5, 'Ho':164.9304, 'Er':167.26, 'Tm':168.9342, 'Yb':173.04,
    'Lu':174.967, 'Hf':178.49, 'Ta':180.9479, 'W':183.85, 'Re':186.207,
    'Os':190.2, 'Ir':192.22, 'Pt':195.09, 'Au':196.9665, 'Hg':200.59,
    'Tl':204.37, 'Pb':207.2, 'Bi':208.9804, 'Po':209, 'At':210,
    'Rn':222, 'Fr':223, 'Ra':226.0254, 'Ac':227.0278, 'Pa':231.0359,
    'Th':232.0381, 'Np':237.0482, 'U':238.029, 'Pu':242, 'Am':243,
    'Bk':247, 'Cm':247, 'No':250, 'Cf':251, 'Es':252, 'Hs':255,
    'Mt':256, 'Fm':257, 'Md':258, 'Lr':260, 'Rf':261, 'Bh':262,
    'Db':262, 'Sg':263, 'Uun':269, 'Uuu':272, 'Uub':277 }


#Function to divide the composition, inserted as a string, into a list using regular expressions
#lcc: list with the complete composition 
def lcc (composition):
    return re.findall('[A-Z][a-z]?|[0-9]+\.?[0-9]+|\.[0-9]+|[0-9]+', composition)


#The comp_dict function transform the list created by lcc into a dictionary
#{Element: composition}
#comp_dict: composition dictionary
def comp_dict(composition):
    #use lcc to parse the composition and transform it into a list
    completelist = lcc(composition)
    #od (organized dictionary) is the dictionary with the composition
    od = {}  
    k = 0
    for i, j in enumerate(completelist):
        if k == 0:
            if not re.findall('[0-9]+\.?[0-9]+|\.[0-9]+|[0-9]+', j):
                element = j
                if (element not in atomic_mass):
                    print('Element {} not present in Periodic table'.format(element))
                k = 1
                if i == (len(completelist)-1):
                    od[element] = 1
        elif k == 1:
            if re.findall('[0-9]+\.?[0-9]+|\.[0-9]+|[0-9]+', j):
                k = 0
                od[element] = float(j)
            else:
                od[element] = 1
                element = j
                k = 1
                if i == (len(completelist)-1):
                    od[element] = 1
    return od


#Convert the composition from atomic fraction to atomic percent
def atf_to_atp(cpaf):
    Tmol = 0
    #cpap: composition atomic percent
    cpap = {}
    for i in cpaf:
        Tmol = Tmol + cpaf[i]
    for i in cpaf:
        cpap[i] = float("{:.2f}".format((cpaf[i])/Tmol*100))
    return cpap


#Convert the composition from atomic fraction to weight percent
def atf_to_wtp(cpaf):
    #cpap: composition atomic percent
    cpap = atf_to_atp(cpaf)
    total = 0
    for i in cpap:
        total += float(cpap[i])*atomic_mass[i]   
    
    cpwp = {}
    for i in cpap:
        CiAi = float(cpap[i])*atomic_mass[i]
        cpwp[i] = float("{:.2f}".format(CiAi/total*100))
    return cpwp


#Convert the composition from atomic percent to weight percent
def atp_to_wtp(cpap):
    total = 0
    for i in cpap:
        total += float(cpap[i])*atomic_mass[i]   
    
    #cpwp: composition weight percent
    cpwp = {}   
    for i in cpap:
        CiAi = float(cpap[i])*atomic_mass[i]
        cpwp[i] = float("{:.2f}".format(CiAi/total*100))
    return cpwp


#Convert the composition from weight percent to atomic percent
def wtp_to_atp(cpwp):   

    total = 0
    for i in cpwp:
        m = float(cpwp[i])/atomic_mass[i]
        total += m
        cpwp[i] = m
       
    for i in cpwp:
        cpwp[i] = float("{:.2f}".format(cpwp[i]/total*100))
        
    cpap = cpwp
    return cpap


#Format the composition to display the result
def format_comp(cp):
    formated = ''
    for i in cp:
        formated += i+str(cp[i])+' '
    return formated


def check_exit():
    e = input('Do you want to exit?(y/n): ')
    if e.lower() == 'y':
        return False
    else:
        return True

#Check if percentage is higher or lower than 100%
def check_percentage(cp):
    total = 0
    for i in cp:
        total += cp[i]
    if total>100:
        print('Warning! Input composition percentage is {}, higher than 100%'.format(total))
    elif total<100:
        print('Warning! Input composition percentage is {}, lower than 100%'.format(total))


#Main loop
i = True
while i == True:
    print('What do you need? Type h for examples')
    print('1 - Convert from atomic fraction to atomic percent')
    print('2 - Convert from atomic fraction to weight percent')
    print('3 - Convert from atomic percent to weight percent')
    print('4 - Convert from weight percent to atomic percent')
    print('h - help!')
    print('e - Exit')
    a = input('(1, 2, 3, 4, e): ')
    
    if a == '1':
        c = input('Insert composition in atomic fraction: ')
        conversion = atf_to_atp(comp_dict(c))
        conversion = format_comp(conversion)
        print(f'This composition in atomic percent is {conversion}')
        i = check_exit()
    elif a == '2':
        c = input('Insert composition in atomic fraction: ')
        conversion = atf_to_wtp(comp_dict(c))
        conversion = format_comp(conversion)
        print(f'This composition in weight percent is {conversion}')
        i = check_exit()
    elif a == '3':
        c = input('Insert composition in atomic percent: ')
        check_percentage(comp_dict(c))
        conversion = atp_to_wtp(comp_dict(c))
        conversion = format_comp(conversion)
        print(f'This composition in weight percent is {conversion}')
        i = check_exit()
    elif a == '4':       
        c = input('Insert composition in weight percent: ')
        check_percentage(comp_dict(c))
        conversion = wtp_to_atp(comp_dict(c))
        conversion = format_comp(conversion)
        print(f'This composition in atomic percent is {conversion}')
        i = check_exit()
    elif a == 'h' or a =='H':       
        print('Compositions must be written in the following manner:')
        print('Metal one followed by its amount, metal two followed by its amount and so on.')
        print('Do not use spaces or other characters.')
        print('Example 1: Ti1Nb2 for a atomic fraction composition.')
        print('Example 2: Mg30W70 for a atomic or weight percent composition.')
        print('Example 3: Mg10Nb10W10Ti10Fe10Mo10Mn10Al10Si10Ta10. There is no limit of elements.')
        i = check_exit()       
    elif a == 'e' or a == 'E':
        i = False