import sys
from concurrent import futures
import grpc
import rpc_pb2
import rpc_pb2_grpc


class EchoService(rpc_pb2_grpc.EchoServicer):
    def EchoMessage(self, request, context):
        print(f"Received message from client: {request.message}")
        return rpc_pb2.EchoReply(message=f"Server received: {request.message}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_EchoServicer_to_server(EchoService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    sys.stdout.flush()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
