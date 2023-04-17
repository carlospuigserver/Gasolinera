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


        tiempo_llenar=random.randint(5*100,10*100)
        time.sleep(tiempo_llenar/100)


        with self.caja:
         tiempo_pagar=3*100
         time.sleep(tiempo_pagar/100)

        self.surtidores[surtidor].release()





class Coche(threading.Thread):
    def __init__(self,gasolinera):
        super().__init__()
        self.gasolinera=gasolinera



    def run(self):
        tiempo_llegada=random.randint(0,15*100)
        time.sleep=tiempo_llegada/100
        print(f"Coche {self.name} llega a la gasolinera en el tiempo{time.time()} segundos.")
        self.gasolinera.atender_coche()
        print(f"Coche {self.name} sale de la gasolinera en el tiempo{time.time()} segundos.")

if __name__ == "__main__":
        gasolinera=Gasolinera(num_surtidores=1)
        coches=[Coche(gasolinera)for i in range(50)]
        for coche in coches:
            coche.start()
        for coche in coches:
            coche.join()



