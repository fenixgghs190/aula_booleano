'''
Construindo a lógica do NOT
'''
print('Construindo a lógica do NOT')

var_1 = True
var_2 = False

print('{} quando negada fica {}'.format(var_1, not var_1))
print()

'''
Construindo a lógica do AND
'''
print('Construindo a lógica do AND')

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

print('Quando var_1_t {} e var_2_t {} o resultado é {}'.format(var_1_t, var_2_t, var_1_t and var_2_t))
print('Quando var_1_t {} e var_2_f {} o resultado é {}'.format(var_1_t, var_2_f, var_1_t and var_2_f))
print('Quando var_1_f {} e var_2_t {} o resultado é {}'.format(var_1_f, var_2_t, var_1_f and var_2_t))
print('Quando var_1_f {} e var_2_f {} o resultado é {}'.format(var_1_f, var_2_f, var_1_f and var_2_f))
print()

'''
Construindo a lógica de OR
'''
print('Construindo a lógica de OR')

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False
print('Quando var_1_t {} e var_2_t {} o resultado é {}'.format(var_1_t, var_2_t, var_1_t or var_2_t))
print('Quando var_1_t {} e var_2_f {} o resultado é {}'.format(var_1_t, var_2_f, var_1_t or var_2_f))
print('Quando var_1_f {} e var_2_t {} o resultado é {}'.format(var_1_f, var_2_t, var_1_f or var_2_t))
print('Quando var_1_f {} e var_2_f {} o resultado é {}'.format(var_1_f, var_2_f, var_1_f or var_2_f))
print()

'''
Múltiplas regras de lógica
'''
print('Múltiplas regras de lógica')

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

var_resultado = ((var_1_t and var_2_f) or ((var_1_f or var_2_t) and (not var_2_f)))
print('O resultado da lógica é {}'.format(var_resultado))
print()


'''
Exercício
'''

print('Exercício 1:')
print()

a_f = False
a_t = True
b_f = False
b_t = True

resultado_tt = ((not a_t and b_t) or (not b_t and a_t))
resultado_tf = ((not a_t and b_f) or (not b_f and a_t))
resultado_ft = ((not a_f and b_t) or (not b_t and a_f))
resultado_ff = ((not a_f and b_f) or (not b_f and a_f))

print('Quando A é true e B é true, o resultado é {}'.format(resultado_tt))
print('Quando A é true e B é false, o resultado é {}'.format(resultado_tf))
print('Quando A é false e B é true, o resultado é {}'.format(resultado_ft))
print('Quando A é false e B é false, o resultado é {}'.format(resultado_ff))

'''
Exercício 2
'''

print('Exercício 2:')
print()

a_t = True
b_t = True
c_t = True
d_t = True
a_f = False
b_f = False
c_f = False
d_f = False

resultado_ffff = (not (a_f and not c_f) or (b_f or d_f)) and (not d_f and c_f)
resultado_ffft = (not (a_f and not c_f) or (b_f or d_t)) and (not d_t and c_f)
resultado_fftf = (not (a_f and not c_t) or (b_f or d_f)) and (not d_f and c_t)
resultado_ftff = (not (a_f and not c_f) or (b_t or d_f)) and (not d_f and c_f)
resultado_fftt = (not (a_f and not c_t) or (b_f or d_t)) and (not d_t and c_t)
resultado_ftft = (not (a_f and not c_f) or (b_t or d_t)) and (not d_t and c_f)
resultado_fttf = (not (a_f and not c_t) or (b_t or d_f)) and (not d_f and c_t)
resultado_fttt = (not (a_f and not c_t) or (b_t or d_t)) and (not d_t and c_t)
resultado_tfff = (not (a_t and not c_f) or (b_f or d_f)) and (not d_f and c_f)
resultado_tfft = (not (a_t and not c_f) or (b_f or d_t)) and (not d_t and c_f)
resultado_tftf = (not (a_t and not c_t) or (b_f or d_f)) and (not d_f and c_t)
resultado_tftt = (not (a_t and not c_t) or (b_f or d_t)) and (not d_t and c_t)
resultado_ttff = (not (a_t and not c_f) or (b_t or d_f)) and (not d_f and c_f)
resultado_ttft = (not (a_t and not c_f) or (b_t or d_t)) and (not d_t and c_f)
resultado_tttf = (not (a_t and not c_t) or (b_t or d_f)) and (not d_f and c_t)
resultado_tttt = (not (a_t and not c_t) or (b_t or d_t)) and (not d_t and c_t)

print()
'''
Correção
'''

A = True
B = True
C = True
D = True

regra = (not(A and (not C)) or (B or D)) and ((not D) and C)
print (A, B, C, D, regra)
valores = [True, False]
for A in valores:
    for B in valores:
        for C in valores:
            for D in valores:
                regra_d_c = ((not D) and C)
                regra_a_c = not (A and (not C))
                regra_b_d = B or D
                regra = (regra_a_c or regra_b_d) and regra_d_c
                print(A, B, C, D, regra)

