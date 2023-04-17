import threading
import time
import random
import tkinter as tk

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

        tiempo_llenar=random.randint(5*100,10*100)
        time.sleep(tiempo_llenar/100)


        with self.caja:
         tiempo_pagar=3*100
         time.sleep(tiempo_pagar/100)

        self.surtidores[surtidor].release()


class Coche(threading.Thread):
    def __init__(self,gasolinera,ventana):
        super().__init__()
        self.gasolinera=gasolinera
        self.ventana=ventana