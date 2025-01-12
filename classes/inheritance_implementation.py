from computer_components import PowerSupply, Motherboard, CPU, RAM, SSD, GraphicsCard


class ComputerCase(PowerSupply, Motherboard, CPU, RAM, SSD, GraphicsCard):
    def __init__(
        self, power, chipset, clock_speed, cores, memory_size_ram, frequency, capacity, model, memory_size_graf
    ):
        PowerSupply.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, clock_speed, cores)
        RAM.__init__(self, memory_size_ram, frequency)
        SSD.__init__(self, capacity)
        GraphicsCard.__init__(self, model, memory_size_graf)

    def start_computer(self):
        return f'{self.supply_voltage()}\n{self.redistribute_voltage()}\n{self.display_image()}'


if __name__ == '__main__':
    print(f'\nФайл - {__file__.split('\\')[-1]}\n')
    computer = ComputerCase(
        750,
        'AMD B650',
        8,
        3.5,
        32,
        5000,
        1000,
        'GeForce RTX 4090',
        24
    )

    print(computer.start_computer())
    print()

    print(f'Производительность компьютера {computer.get_cores()}')
    print(computer.activate_turbo_mode())
    print()

    print(computer.load_data(2.5))
    print(computer.load_data(2.5))
    print(computer.unload_data(4))
    print()

    print(computer.save_data(100))
    print(computer.save_data(200))
    print(computer.delete_data(150))