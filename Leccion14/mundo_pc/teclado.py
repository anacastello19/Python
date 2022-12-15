from mundo_pc.dispositvo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contador_teclados+=1
        self._id_teclado= Teclado.contador_teclados
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'Id:{self._id_teclado}, Marca: {self._marca}, Tipo de Entrada: {self._tipoEntrada}'

if __name__=='__main__':
    teclado1= Teclado('HP', 'USB')
    print(teclado1)
    teclado2= Teclado('Gamer','Bluetooth')
    print(teclado2)