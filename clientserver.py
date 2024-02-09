import msgpack
import zmq


class DuplicationClient:
    def __init__(self, server_address: str = "tcp://localhost:5545"):
        self.__context = zmq.Context.instance()
        self.__socket = self.__context.socket(zmq.REQ)
        self.__socket.setsockopt(zmq.LINGER, 0)
        self.__socket.setsockopt(zmq.AFFINITY, 1)
        self.__socket.connect(server_address)

    def check_if_duplicate_and_add(self, filename: str) -> bool:
        self.__socket.send(msgpack.dumps(filename))
        print(f"FLAG 22: From duplication client with file name {filename}")
        return bool(self.__socket.recv())
