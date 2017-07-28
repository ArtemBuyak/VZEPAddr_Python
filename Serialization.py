class Serialiaz():
    def __init__(self, answer, vzep):
        self.__buff = answer
        self.__vzep = vzep
        self.__counter = 0

    @property
    def buff(self):
        return self.__buff

    @buff.setter
    def buff(self, buff):
        self.__buff = buff

    @property
    def vzep(self):
        return self.__vzep

    @vzep.setter
    def vzep(self, vzep):
        self.__vzep = vzep

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, counter):
        self.__counter = counter

    def to_file_from_answer(self,answer,  number):
        self.buff = answer
        try:
            if (str(hex(self.buff[0]))[2:] == "ff" and str(hex(self.buff[1]))[2:] == "ff"
                and str(hex(self.buff[2]))[2:] == "ff" and str(hex(self.buff[3]))[2:] == "ff"
                and str(hex(self.buff[4]))[2:] == "ff"):
                self.counter = 0
                return 1
        except IndexError:
            return 2
        except Exception:
            return 2
        else:
            my_file = open("test.txt", "a")
            if (str(hex(self.vzep.buff[14])))[2:] != '0' or (str(hex(self.vzep.buff[15])))[2:] != '0':
                my_file.write("\n")
            i = 0
            while i < 3:
                if str(hex(self.buff[2 - i])).__len__() < 4:
                    my_file.write("0" + (str(hex(self.buff[2 - i])))[2:])
                else:
                    my_file.write((str(hex(self.buff[2 - i])))[2:])
                i += 1
            i = 0
            while i < 2:
                if str(hex(self.vzep.buff[15 - i])).__len__() < 4:
                    if i == 0:
                        my_file.write(";$0" + (str(hex(self.vzep.buff[15 - i])))[2:])
                    else:
                        my_file.write("0" + (str(hex(self.vzep.buff[15 - i])))[2:])
                else:
                    if i == 0:
                        my_file.write(";$" + (str(hex(self.vzep.buff[15 - i])))[2:])
                    else:
                        my_file.write((str(hex(self.vzep.buff[15 - i])))[2:])
                i += 1
            my_file.write(";" + number)
            self.counter += 1
            print("Считано: " + str(self.counter) + " счетчиков. По телефону: " + number )
            return 0