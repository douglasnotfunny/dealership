# Dealership System

Este é o código para um sistemas de concesionária, na qual pode ser cadastrado pessoas e carros. o código foi desenvolvido em Python3.10 com a bliblioteca Flask

- Para a execução do código siga os seguintes passo:
  
  cd development && docker-compose up --build

Com os passos é virtualizado o ambiente e instalada as bibliotecas necessárias

No arquivo Dearlership.postman_collection.json contém os endpoints criados para utilizá-los

- Neste projeto também foi desenvolvidos testes de cobertura que podem ser executados no comanda abaixo:
  
  coverage run -m pytest test/
  
- Para visualizar a cobertura dos testes basta utilizar o comando:
  
    coverage report
