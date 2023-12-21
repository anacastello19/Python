from mundo_pc.dispositvo_entrada import DispositivoEntrada


class Monitor(DispositivoEntrada):
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._tamaño = tamaño
        super().__init__(marca)

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca},  Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitor1 = Monitor('HP', '18 pulgadas')
    print(monitor1)
    monitor2 = Monitor('Samsung', '24 pulgadas')
    print(monitor2)
