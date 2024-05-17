def d_v(rut):
    '''
    entrega el digito veriificador de un numero
    Se puede usar para colocar el dv
    df['dv']=list(map(lambda i:d_v(i), df['rut']))

    '''
    value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
    return {10: 'K', 11: '0'}.get(value, str(value))

