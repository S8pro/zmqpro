import zmq


def close_all_ports():
    print("Closed All")
    context = zmq.Context.instance()
    sockets = []

    # Create a socket for each socket type (PUB, SUB, REQ, REP, etc.)
    for socket_type in [zmq.PUB, zmq.SUB, zmq.REQ, zmq.REP, zmq.DEALER, zmq.ROUTER, zmq.PAIR]:
        try:
            socket = context.socket(socket_type)
            sockets.append(socket)
        except zmq.ZMQError as e:
            print(f"Error creating socket for type {socket_type}: {e}")

    # Close all sockets
    for socket in sockets:
        try:
            last_endpoint = socket.getsockopt(zmq.LAST_ENDPOINT)
            print("Socket address:", last_endpoint)
            socket.close()

        except zmq.ZMQError as e:
            print(f"Error closing socket: {e}")


if __name__ == "__main__":
    close_all_ports()
