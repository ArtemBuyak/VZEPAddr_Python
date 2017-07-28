from COM_work import COM_worker
from VZEP import Vzep
from Serialization import Serialiaz
from GSM_Connection import GSM
from Parse_XLS import Parsing_xls

from_serialization = 0
kol = 0
flag = 1
vz = Vzep()
s = Serialiaz(vz.answer, vz)
com = COM_worker("COM12", 9600)
gsm = GSM(com)
par = Parsing_xls()
se = par.parse()
breaking = 0

for i in se:
    s.counter = 0
    while flag:
        check = gsm.gsm_connection(i)
        if check:
            if kol == 3:
                kol = 0
                flag = 0
                breaking = 1
                continue
            else:
                kol += 1
        else:
            flag = 0
            kol = 0
    flag = 1
    if breaking:
        breaking = 0
        continue
    while flag:
        if kol == 0:
            com.write(bytes(vz.create_request(0x00, 0x00)))
        elif from_serialization == 2:
            gsm.gsm_connection(i)
            com.write(bytes(vz.create_request(vz.copy1, vz.copy2)))
        else:
            com.write(bytes(vz.create_request(vz.answer[vz.answer.__len__() - 4], vz.answer[vz.answer.__len__() - 3])))
        vz.read_answer(com)
        from_serialization = s.to_file_from_answer(vz.answer, i)
        if from_serialization:
            flag = 0
        vz.buff = []
        kol += 1
    flag = 1
    gsm.gsm_disconnection()
