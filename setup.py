from setuptools import setup, find_packages

setup(
    name="bancodigital_frf",  # Nome ÚNICO!
    version="3.0.1",          # Nova versão
    author="Fernando Rodrigues Fraga",
    author_email="fr.fraga@outlook.com",  # Campo obrigatório
    description="Sistema bancário orientado a objetos",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FRFraga/sistema_bancario3.0",  # URL válida
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'bancodigital = bancodigital.core:main'
        ]
    },
    python_requires='>=3.10',
)