from computer_components import PowerSupply, Motherboard, CPU, RAM, SSD, GraphicsCard

class ComputerCase:
    def __init__(self, power_supply_obj, motherboard_obj, cpu_obj, ram_obj, ssd_obj, graphics_card_obj):
        self.power_supply = power_supply_obj
        self.motherboard = motherboard_obj
        self.cpu = cpu_obj
        self.ram = ram_obj
        self.ssd = ssd_obj
        self.graphics_card = graphics_card_obj

    def start_computer(self):
        return (f'{self.power_supply.supply_voltage()}\n{self.motherboard.redistribute_voltage()}'
                f'\n{self.graphics_card.display_image()}')


if __name__ == '__main__':
    print(f'\nФайл - {__file__.split('\\')[-1]}\n')
    power_supply = PowerSupply(750)
    motherboard = Motherboard('AMD B650')
    cpu = CPU(8, 3.5)
    ram = RAM(32, 5000)
    ssd = SSD(1000)
    graphics_card = GraphicsCard('GeForce RTX 4090', 24)

    computer = ComputerCase(power_supply, motherboard, cpu, ram, ssd, graphics_card)
    print(computer.start_computer())
    print()

    print(f'Производительность компьютера {computer.cpu.get_cores()}')
    print(computer.cpu.activate_turbo_mode())
    print()

    print(computer.ram.load_data(2.5))
    print(computer.ram.load_data(2.5))
    print(computer.ram.unload_data(4))
    print()

    print(computer.ssd.save_data(100))
    print(computer.ssd.save_data(200))
    print(computer.ssd.delete_data(150))