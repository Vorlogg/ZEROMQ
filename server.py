'''
Сервер стрима видеопотока
  в аргументах указывается видео,
  которое будет передаваться сервером,
если не будет аргументов запись будет с  веб-камеры

 '''
import cv2
import zmq
import sys


def run_stream(camera):
    context = zmq.Context()
    footage_socket = context.socket(zmq.PUB)# создание сокета
    footage_socket.bind("tcp://*:5555")# установка адресса сокета
    while True:
        try:
            grabbed, frame = camera.read() # захват кадра
            frame = cv2.resize(frame, (640, 480)) # размер кадра
            encoded, buffer = cv2.imencode('.jpg', frame)
            footage_socket.send(buffer)# передача
        except KeyboardInterrupt:
            camera.release()
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        camera = cv2.VideoCapture(sys.argv[1])
        run_stream(camera)
    else:
        camera = cv2.VideoCapture(0)
        run_stream(camera)
