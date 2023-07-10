# README (Projeto de graduação)

Projeto desenvolvido para a disciplina de Sistemas Embarcados II da faculdade de Engenharia mecatrônica.
O objetivo da automação era:

- Movimentar diferentes tipos de caixas através de uma esteira;
- Fazer a distinção e separação de caixas em tamanhos: pequeno e grande;
- Fazer a distinção e separação de caixas de metal e madeira;
- Fazer o controle do sistema em modo manual e automático;
- Fazer uma interface com HTML e Flask.

Além disso, foi desenvolvido:
- Uma memória de quais caixas passaram por último, exibidas em sequência na interface;
- Um contador para exibir o número de caixas separadas.

Para isso, foram utilizados:
- Raspberry Pi 3b programado em Python;
- Uma placa eletrônica para amplificar o sinal do Raspberry para 12V, e receber sinal em 3,3V;
- 1 Sensor indutivo e 1 capacitivo, 4 Cilindros e 1 esteira.

Resultados:

O projeto foi iniciado e finalizado em 2018. Neste, foi possível realizar todas as funções requeridas de seleção de caixa, também a opção de escolher o modo manual ou automático funcionou adequadamente.

A interface web estava funcionando e exibindo dados adequadamente, porém o maior desafio encontrado foi a questão da obtenção de dados em tempo real corretamente.

Por isso, foi implementado uma atualização de página frequente como medida corretiva. Hoje, caso o código seja reorganizado, haveria a necessidade de eliminar este refresh, utilizar uma biblioteca que faça a leitura em tempo real. 

Além disso, haveira uma reestruturação do código eliminando as variáveis globais e deixando apenas uma página web para cada seleção de modo, onde apenas uma variável comunica o estado lógico dos sensores e atuadores.
