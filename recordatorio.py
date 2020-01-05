import time # libreria que ocuparemos
print ("¿que deseas que te recuerde?")
text = str(input())
print ("¿en cuantos minutos te lo recuerdo?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)
