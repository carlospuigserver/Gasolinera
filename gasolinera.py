import threading
import time 
import random

class Gasolinera:
    def __init__(self, num_surtidores):
        self.num_surtidores=num_surtidores
        self.surtidores=[threading.Lock () for _ in range (num_surtidores)]
        self.caja=threading.Lock()
        self.abierta=True

