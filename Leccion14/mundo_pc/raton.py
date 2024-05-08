from mundo_pc.dispositvo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones= 0

    def __init__(self, marca, tipoEntrada):
        Raton.contador_ratones +=1
        self._id_raton= Raton.contador_ratones
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo de entrada: {self._tipoEntrada}'

#Hacemos pruebas
if __name__=='__main__':
    raton1 = Raton('HP','USB')
    print(raton1)
    raton2 = Raton('Arcer','Bluetooth')