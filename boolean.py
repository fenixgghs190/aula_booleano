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

print('Quando var_1_t{} e var_2_t {} o resultado é {}'.format(var_1_t, var_2_t, var_1_t and var_2_t))
print('Quando var_1_t{} e var_2_f {} o resultado é {}'.format(var_1_t, var_2_f, var_1_t and var_2_f))
print('Quando var_1_f{} e var_2_t {} o resultado é {}'.format(var_1_f, var_2_t, var_1_f and var_2_t))
print('Quando var_1_f{} e var_2_f {} o resultado é {}'.format(var_1_f, var_2_f, var_1_f and var_2_f))
print()

'''
Construindo a lógica de OR
'''
print('Construindo a lógica de OR')

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False
print('Quando var_1_t{} e var_2_t {} o resultado é {}'.format(var_1_t, var_2_t, var_1_t or var_2_t))
print('Quando var_1_t{} e var_2_f {} o resultado é {}'.format(var_1_t, var_2_f, var_1_t or var_2_f))
print('Quando var_1_f{} e var_2_t {} o resultado é {}'.format(var_1_f, var_2_t, var_1_f or var_2_t))
print('Quando var_1_f{} e var_2_f {} o resultado é {}'.format(var_1_f, var_2_f, var_1_f or var_2_f))
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

print('Exercício passado em aula:')

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
