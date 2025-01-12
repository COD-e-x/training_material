class PowerSupply:
    def __init__(self, power):
        self.__power = power

    def get_power(self):
        return self.__power

    def supply_voltage(self):
        return f'Подаем напряжение мощностью {self.__power} Вт.'


class Motherboard:
    def __init__(self, chipset):
        self.__chipset = chipset

    def get_chipset(self):
        return self.__chipset

    def redistribute_voltage(self):
        return f'Перераспределяем напряжение через чипсет {self.__chipset}.'


class CPU:
    def __init__(self, clock_speed, cores):
        self.__clock_speed = clock_speed
        self.__cores = cores

    def get_clock_speed(self):
        return self.__clock_speed

    def get_cores(self):
        return self.__cores

    def activate_turbo_mode(self):
        return f'Активирован турбо-режим, производительность увеличилась до {self.__clock_speed * 0.6} ГГц.'


class RAM:
    def __init__(self, memory_size, frequency):
        self.__memory_size = memory_size
        self.__frequency = frequency
        self.__current_ram_size = memory_size

    def get_memory_size(self):
        return self.__memory_size

    def get_frequency(self):
        return self.__frequency

    def get__current_ram_size(self):
        return self.__current_ram_size

    def load_data(self, size):
        if size <= self.__current_ram_size:
            self.__current_ram_size -= size
            return f'Загружаем данные в оперативную память {size} ГБ, объем оперативной памяти {self.__current_ram_size} ГБ'
        else:
            return f'Используется файл подкачки!'

    def unload_data(self, size):
        if size <= (self.__memory_size - self.__current_ram_size):
            self.__current_ram_size += size
            return f'Выгружаем данные из оперативной памяти {size} ГБ, объем оперативной памяти {self.__current_ram_size} ГБ.'
        else:
            # По факту не знаю возможна вообще такая ошибка, но пусть будет как предупреждение
            return f'Ошибка: Попытка выгрузить больше дынных, чем загружено'


class SSD:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__current_ssd_size = capacity

    def get_capacity(self):
        return self.__capacity

    def get_current_ssd_size(self):
        return self.__current_ssd_size

    def save_data(self, size):
        if size <= self.__current_ssd_size:
            self.__current_ssd_size -= size
            return f'Сохраняем данные на SSD объемом {size} ГБ, объем SSD {self.__current_ssd_size}'
        else:
            return f'Ошибка: недостаточно памяти на SSD'

    def delete_data(self, size):
        if size <= (self.__capacity - self.__current_ssd_size):
            self.__current_ssd_size += size
            return f'Удаляем данные с SSD объемом {size} ГБ, объем SSD {self.__current_ssd_size}'
        else:
            return f'Попытка удалить больше записанного объема памяти!'


class GraphicsCard:
    def __init__(self, model, memory_size):
        self.__model = model
        self.__memory_size = memory_size

    def get_model(self):
        return self.__model

    def get_memory_size(self):
        return self.__memory_size

    def display_image(self):
        return f'Выводим изображение на экран с видеокартой {self.__model}.'