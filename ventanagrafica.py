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

    def run(self):
        tiempo_llegada=random.randint(0,15*100)
        time.sleep=tiempo_llegada/100
        print(f"Coche {self.name} llega a la gasolinera en el tiempo{time.time()} segundos.")
        self.gasolinera.atender_coche()
        print(f"Coche {self.name} sale de la gasolinera en el tiempo{time.time()} segundos.")
        self.ventana.actualizar_surtidores()

class Ventana:
    def __init__(self,gasolinera):
        self.gasolinera=gasolinera
        self.root=tk.Tk()
        self.root.title("Gasolinera")
        self.surtidores_label=tk.Label(self.root,text=f"Surtidores libres: {gasolinera.num_surtidores}")
        self.surtidores_label.pack()
        self.llegada=tk.Button(self.root,text="Llegada de coche", command=self.llegada_coche)
        self.llegada.pack()

    def actualizar_surtidores(self):
        self.surtidores_label.configure(text=f"Surtidores libres: {self.gasolinera.num_surtidores}")

    
    def llegada_coche(self):
        coche=Coche(self.gasolinera,self)
        coche.start()

    def iniciar(self):
        for i in range (50):
            coche=Coche(self.gasolinera,self)
            coche.start()
        self.root.mainloop()

if __name__ == "__main__":
      gasolinera=Gasolinera(num_surtidores=1)
      ventana=Ventana(gasolinera)
      ventana.iniciar()
  