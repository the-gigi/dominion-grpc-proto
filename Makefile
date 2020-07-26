*.py: *.proto
	poetry run python \
               -m grpc_tools.protoc \
               --python_out=dominion_grpc_proto  \
               --grpc_python_out=dominion_grpc_proto \
               -I. dominion.proto
	sed -i '' 's/dominion_pb2/dominion_grpc_proto.dominion_pb2/' ./dominion_grpc_proto/dominion_pb2_grpc.py