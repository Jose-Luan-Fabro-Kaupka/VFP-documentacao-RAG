# Otimizando o desempenho cliente/servidor

Depois de implementar sua aplicação cliente/servidor, você pode encontrar áreas onde deseja melhorar o desempenho. Por exemplo, você pode ajustar sua aplicação para obter desempenho máximo acelerando formulários e consultas e aumentando a taxa de transferência de dados.

Esta seção discute estratégias de otimização para o desempenho da aplicação no cliente, na rede e no servidor.

# Nesta seção
 **Client/Server Design for High Performance**
Construir uma aplicação cliente/servidor rápida e de alto desempenho com o Microsoft® Visual FoxPro® envolve aproveitar a enorme velocidade do mecanismo do Visual FoxPro.
**Optimizing Connections**
Estabelecer uma conexão usa tempo e memória tanto no cliente quanto no servidor. Ao otimizar conexões, você equilibra sua necessidade de alto desempenho contra os requisitos de recursos da sua aplicação.
**Speeding Up Data Retrieval**
Você pode acelerar a recuperação de dados gerenciando o número de linhas buscadas durante o progressive fetching, controlando o tamanho da busca e usando delayed Memo fetching.
**Query and View Acceleration**
Você pode melhorar o desempenho de consultas e views adicionando índices, otimizando o processamento local e remoto e otimizando expressões de parâmetro.
**Form Acceleration**
Ao projetar um formulário baseado principalmente em dados do servidor, adote uma abordagem minimalista para obter o melhor desempenho.
**Performance Improvement on Updates and Deletes**
Você pode acelerar instruções Update e Delete adicionando timestamps às suas tabelas remotas, usando a propriedade CompareMemo, usando o modo de transação manual, usando stored procedures em um servidor remoto e agrupando atualizações.

# Seções relacionadas
 **Creating Applications**
Discute como criar uma aplicação Visual FoxPro, que pode incluir um ou mais bancos de dados, um programa principal que configura o ambiente do sistema da aplicação e uma interface do usuário composta por formulários, toolbars e menus.
**How to: Set the Starting Point**
Descreve como o arquivo principal é o ponto de partida da sua aplicação e pode consistir em um programa ou formulário. Quando sua aplicação é executada, o Visual FoxPro inicia o arquivo principal da sua aplicação, que por sua vez executa todos os outros componentes conforme necessário.
**How to: Initialize the Environment**
Configurar o ambiente da aplicação é a primeira tarefa que um arquivo principal ou objeto de aplicação deve realizar.
**How to: Control the Event Loop**
Aprenda como estabelecer um loop de eventos, o que faz o Visual FoxPro começar a processar eventos do usuário, como cliques do mouse e pressionamentos de teclas. Isso ocorre depois que o ambiente é configurado e você exibiu a interface do usuário inicial.
**Creating Applications with the Application Framework**
Explica como criar aplicações com o Application Framework usando o Application Wizard e o Application builder.
**Creating the User Interface**
Aprenda como criar formulários, classes, controles e toolbars pode fornecer um conjunto rico de ferramentas para sua interface do usuário.
**Upsizing Visual FoxPro Databases**
Explica como usar os assistentes de upsizing para mover bancos de dados, tabelas e views do seu sistema para um Microsoft SQL Server remoto.
**Creating International Applications**
Descreve como você pode projetar e desenvolver suas aplicações Visual FoxPro para que sejam tão eficazes internacionalmente quanto domesticamente.
