from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'LOLZTEAM api package'

# Setting up
setup(
    name="LZT_api",
    version=VERSION,
    author="fogiky",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'LOLZTEAM'],
)
