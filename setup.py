from setuptools import setup

setup(name='dominion-grpc-proto',
      version='0.3.0',
      url='https://github.com/the-gigi/dominion-grpc-proto',
      license='MIT',
      author='Gigi Sayfan',
      author_email='the.gigi@gmail.com',
      description='gRPC protobuf definitions + generated Python code',
      packages=['dominion_grpc_proto'],
      python_requires='>=3.8',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      zip_safe=False)
