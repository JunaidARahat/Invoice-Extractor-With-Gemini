from setuptools import find_packages, setup

setup(
    name = "Invoice Extractor",
    version="0.0.1",
    author="JunaidARahat",
    author_email="mjunaidrahat1990@gmail.com",
    packages=find_packages(),
    # this function will look for the constructor file (__init__.py)
    # in every folder and install those local packages in my enviorment
    install_requires = []
)