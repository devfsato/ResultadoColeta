from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ResultadoColeta',
      version='1.0.0',
      description='Relatório do resultado de Inicio e Fim da Coleta',
      url='https://github.com/devfsato/ResultadoColeta.git',
      author='Fabiano Sato',
      author_email='fsato@ecourbis.com.br',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      zip_safe=False)