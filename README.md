# Dominon gRPC proto
[
![PyPI](https://img.shields.io/pypi/v/dominion-grpc-proto.svg)
![PyPI](https://img.shields.io/github/license/the-gigi/dominion-grpc-proto.svg)
](https://pypi.org/project/dominion-grpc-proto/)



The [gRPC](https://grpc.io/) protobuf definitions for the [Dominion](https://github.com/the-gigi/dominion) project

The **dominion.proto** file specifies the Dominion service definition. The Makefile creates two Python modules that can be used by the Dominion server and clients.
  
  
  
# Build and publish

This section is for the Dominion developers. 
If you just want to implement a player or a client library you can stop reading.


## Pre-requisites

- Install [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win)
- Install [poetry](https://python-poetry.org/docs/#installation)

Create a Python 3.8.2 environment

```
$ pyenv install 3.8.2
$ pyenv local
$ poetry init
$ poetry env use 3.8.2
$ poetry install
```

Save the following to ~/.pypirc

```
[distutils]
index-servers=
    pypi
    pypitest

[pypitest]
repository = https://test.pypi.org/legacy/
username = <your user name>

[pypi]
repository = https://pypi.org/legacy/
username = <your user name>
```

## Building the gRPC generated code

Just run `make`

## Building the package

Here is the command to build the package:

```
(🐙)/dominion-grpc-proto
$ poetry run python setup.py bdist_wheel
``` 

The result is tar-gzipped file in the dist subdirectory:

```
(🐙)/dominion-grpc-proto
$ ls dist
dominion_grpc_proto-0.2.0-py3-none-any.whl
```

## Publish the package

Next, we can upload the package using twine to PyPI.

```
(🐙)/dominion-grpc-proto
$ poetry run twine upload -p <redacted> dist/*.whl

Uploading distributions to https://upload.pypi.org/legacy/
Uploading dominion_grpc_proto-0.2.0-py3-none-any.whl
100%|███████████████████████████████████| 10.3k/10.3k [00:02<00:00, 3.54kB/s]

View at:
https://pypi.org/project/dominion-grpc-proto/0.2.0/
```

