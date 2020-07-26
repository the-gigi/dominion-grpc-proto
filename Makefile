*.py: *.proto
	poetry run python \
               -m grpc_tools.protoc \
               --python_out=dominion_grpc_proto  \
               --grpc_python_out=dominion_grpc_proto \
               -I. dominion.proto
