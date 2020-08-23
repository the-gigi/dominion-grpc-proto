build: *.proto
	poetry run python \
               -m grpc_tools.protoc \
               --python_out=dominion_grpc_proto  \
               --grpc_python_out=dominion_grpc_proto \
               -I. dominion.proto
	sed -i '' 's/dominion_pb2/dominion_grpc_proto.dominion_pb2/' ./dominion_grpc_proto/dominion_pb2_grpc.py

build-dist: build
	poetry run python setup.py bdist_wheel

publish: build-dist
	poetry run twine upload -p "${PYPI_PASSWORD}" dist/*.whl
