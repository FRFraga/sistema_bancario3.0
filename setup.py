from setuptools import setup, find_packages

setup(
    name="bancodigital",
    version="3.0.0",
    author="Fernando Rodrigues Fraga",
    description="Sistema bancário orientado a objetos",
    packages=find_packages(include=['bancodigital*']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bancodigital = bancodigital.core:main'
        ]
    },
    python_requires='>=3.10'
)