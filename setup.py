from setuptools import find_packages, setup

setup(
    name='proceso',
    packages=find_packages(include=['proceso']),
    version='0.0.1',
    description='Proyecto 4 de IE0405 - Modelos Probabilísticos de Señales y Sistemas',
    author='Sofía Mairena Herrera, Laisa , Estudiante C',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'requests',
        'pandas',
        'json',
        'datetime',
        'matplotlib',
        'fitter',
        'scipy.stats',
    ],
)
