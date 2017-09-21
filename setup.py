from distutils.core import setup

setup(
    name='rhgapi', version='0.1.0', description="Python client for RHG server",
    packages=['rhgapi'],
    install_requires=['requests']
)