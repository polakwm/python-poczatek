import math
# s_dyst=0
# t_czas=0
# a=0
# b=0
# c=0
# k=0
# op=0
# ti=0
# suma = 0

def obl_v (s_dyst, t_czas):
    v_predk=s_dyst / t_czas
    return v_predk
def obl_c(a,b):
    c= math.sqrt(math.pow(a,2) + math.pow(b,2))
    return c
def obl_kapital(k,op,ti):
    suma=k*(1+op/100)**ti
    return suma