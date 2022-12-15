from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 pulgadas')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
print(computadora1)

teclado2 = Teclado('HP', 'USB')
monitor2 = Monitor('HP', '15 pulgadas')
raton2 = Raton('HP', 'USB')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

computadora1=[computadora1, computadora2]
orden1= Orden(computadora1)
print(orden1)

teclado3 = Teclado('HP', 'USB')
monitor3 = Monitor('HP', '15 pulgadas')
raton3 = Raton('HP', 'USB')
computadora3 = Computadora('HP', monitor3, teclado3, raton3)
print(computadora3)

teclado4 = Teclado('Gamer', 'Bluetooth')
monitor4 = Monitor('Gamer', '27 pulgadas')
raton4 = Raton('Gamer', 'Bluetooth')
computadora4 = Computadora('Acer', monitor4, teclado4, raton4)

teclado5 = Teclado('HP', 'USB')
monitor5 = Monitor('HP', '15 pulgadas')
raton5 = Raton('HP', 'USB')
computadora5 = Computadora('HP', monitor5, teclado5, raton5)

computadora2=[computadora4, computadora3]
orden2= Orden(computadora2)
print(orden2)





