#creear funcion para el calculo de descuento

def calcular_descuento(valor_total,porcentaje_descuento=10):
    descuento = valor_total * porcentaje_descuento /100
    return descuento
monto_total1= 1000
descuento1 = calcular_descuento(monto_total1)
print(f'el valor del descuesto es : ',monto_total1)
print(f'el valor del descuento es : ', descuento1)

## monto total y porcentaje
monto_total2= 2000
porcentaje_descontar=20
descuento2 = calcular_descuento(monto_total2,porcentaje_descontar)
print(f'El monto total es:', monto_total2)
print(f'el valor del descuesto es del ejemplo 2 : ',descuento2)
