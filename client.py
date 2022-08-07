'''
Клиент
подключение к серверу и трансляция видео
 '''

import cv2
import zmq
import numpy as np



def start_client():
    port = "5555"
    context = zmq.Context()
    footage_socket = context.socket(zmq.SUB)# создание сокета
    footage_socket.connect("tcp://localhost:%s" % port) # коннект к серверу
    footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))# установка параметров сокета через обьект юникода
    while True:
        try:
            frame = footage_socket.recv() #получение
            npimg = np.frombuffer(frame, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)
            cv2.imshow("Stream", source)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    start_client()