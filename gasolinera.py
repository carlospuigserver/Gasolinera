import threading
import time 
import random

class Gasolinera:
    def __init__(self, num_surtidores):
        self.num_surtidores=num_surtidores
        self.surtidores=[threading.Lock () for _ in range (num_surtidores)]
        self.caja=threading.Lock()
        self.abierta=True

def atender_coche(self):
    surtidor=None
    while surtidor is None:
        for i in range(self.num_surtidores):
            if self.surtidores[i].acquire(blocking=False):
                surtidor=i
                break
            else:
                time.sleep(0.1)

#Llenar el deposito
tiempo_llenar=random.randint(5*100,10*100)
time.sleep(tiempo_llenar/100)

