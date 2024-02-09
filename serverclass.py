import time

import msgpack
import zmq

import clossall


class dupserver:
    def server(self, address: str = "tcp://*:5545", save_state_every_sec: int = 5 * 60):
        clossall.close_all_ports()
        context = zmq.Context.instance()
        socket = context.socket(zmq.REP)
        socket.bind(address)
        print("Started")
        while True:
            print("Before")

            message = socket.recv()
            print("Recived")
            filename = msgpack.loads(message)
            print(f"FLAG 23: From duplication server with file name{filename},")
            time.sleep(1)
            socket.send(bytes(True))


