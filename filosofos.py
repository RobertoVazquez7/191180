import time
import random
import threading
#from threading import Thread, Lock
import queue #constructor en clase (limite de elementos insertados en cola)
#mutex = Lock()

queue = queue.Queue(maxsize=5); # numero de elementos en cola (limite)

#funcion
def tenedor(): 
    item = 0
    while True:
        if not queue.full(): # espera que le proceso termine
            #mutex.acquire()
            item += 1
            queue.put(item) # pone el item en cola
            print('Filosofo', item, 'esta comiendo') 

            time_sleep = random.randint(1,3) # 1,5 milisegundos
            time.sleep(time_sleep)
            if item == 5:
                break

#funcion
def filosofo(): 
    while True:
        if not queue.empty(): # verifica que no haya un proceso en cola
            #mutex.release()
            item = queue.get() # se extrae el recurso de queue
            queue.task_done() # indicar que la tarea esta completada
            print('Filosofo', item, 'ha terminado de comer')

            time_sleep = random.randint(1,3) # 1 - 5 milisegundos
            time.sleep(time_sleep)
            if item == 5:
                break

if __name__ == '__main__':
    tenedor_hilo = threading.Thread(target=tenedor)
    filosofo_hilo = threading.Thread(target=filosofo)

    tenedor_hilo.start()
    filosofo_hilo.start()