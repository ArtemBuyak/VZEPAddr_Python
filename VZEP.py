import serial
from Serialization import Serialiaz
from COM_work import COM_worker

class Vzep():
    def __init__(self):
        self.__buff = []
        self.__answer = b''
        self.__copy1 = 0
        self.__copy2 = 0

    @property
    def buff(self):
        return self.__buff

    @buff.setter
    def buff(self, mass):
        self.__buff = mass

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        self.__answer = answer

    @property
    def copy1(self):
        return self.__copy1

    @copy1.setter
    def copy1(self, copy1):
        self.__copy1 = copy1

    @property
    def copy2(self):
        return self.__copy2

    @copy2.setter
    def copy2(self, copy2):
        self.__copy2 = copy2


    #Метод расчета CRC
    def calculation_crc(self, mass, begin, count):
        CS = 0x00
        end = begin
        while begin < end + count:
            CS += mass[begin]
            begin+=1
        CS = CS & 0xFF
        return CS

    #метод формирования посылки на концентратор
    def create_request(self, lAddr, hAddr):
        # 0-3 заводской номер концентратора, 4 - КС первых трех
        self.buff.append(0x01)
        self.buff.append(0x00)
        self.buff.append(0x00)
        self.buff.append(self.calculation_crc(self.buff, 0, 3))
        # 4-6 старый пароль в формате BCD, 7 - КС байт 4-6
        self.buff.append(0x01)
        self.buff.append(0x00)
        self.buff.append(0x00)
        self.buff.append(self.calculation_crc(self.buff, 4, 3))
        # 8-10 новый пароль в формате BCD, 11 - КС байт 8-10
        self.buff.append(0x01)
        self.buff.append(0x00)
        self.buff.append(0x00)
        self.buff.append(self.calculation_crc(self.buff, 8, 3))
        self.buff.append(0x00) # код ошибки
        self.buff.append(0x33) # код функции
        # 14-15 байты адреса в памяти контроллера
        self.buff.append(lAddr)
        self.buff.append(hAddr)
        self.buff.append(0x00) # кол-во байт, значение - 0
        self.buff.append(self.calculation_crc(self.buff, 0, 17)) # КС байт 0-16
        return self.buff

    def read_answer(self, serial_object):
        self.answer = serial_object.read_answer(4)
        self.copy1 = self.answer[self.answer.__len__() - 4]
        self.copy2 = self.answer[self.answer.__len__() - 3]
        return self.answer
