import grpc
import rpc_pb2
import rpc_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = rpc_pb2_grpc.EchoStub(channel)
        request = rpc_pb2.EchoRequest(message="Hello, gRPC!")
        response = stub.EchoMessage(request)
    print("Server echoed: " + response.message)


if __name__ == "__main__":
    run()
    input("Press Enter to exit...")