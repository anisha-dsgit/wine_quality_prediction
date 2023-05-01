#setup file need to make the module as package - to make it available for the public 
#find_packages calls all the packages where __init__ file is there 
from setuptools import setup, find_packages

setup(  name="wine_quality", 
        version="0.0.1",
        author="anisha",
        email="anisha1207@gmail.com",
        packages=find_packages(),
        install_requires=["pandas","numpy","flask"]
        )