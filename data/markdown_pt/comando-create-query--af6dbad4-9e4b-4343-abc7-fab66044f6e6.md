# Comando CREATE QUERY

Abre o Query designer.

```foxpro
CREATE QUERY [FileName | ?] [NOWAIT]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo da consulta. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .qpr.
**?**
Exibe a caixa de diálogo Create, que solicita que você nomeie a consulta sendo criada.
**NOWAIT**
Continua a execução do programa após o Query Designer ser aberto. O programa não aguarda o fechamento do Query Designer, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE QUERY NOWAIT. Se você omitir NOWAIT quando CREATE QUERY é emitido em um programa, o Query Designer é aberto e a execução do programa pausa até que o Query Designer seja fechado. NOWAIT é eficaz somente a partir de um programa. Não tem efeito em CREATE QUERY quando emitido da Command window.

# Observações

CREATE QUERY abre o Query designer para que você possa criar uma consulta de forma interativa.

Um comando SQL SELECT é usado para recuperar dados de tabelas. SELECT é muito poderoso e pode substituir uma série de comandos do Visual FoxPro. Como um SQL SELECT executa a função de uma série de comandos do Visual FoxPro, SELECT otimiza o desempenho do programa.

Pense em SELECT como uma forma de fazer uma consulta ao Visual FoxPro para obter informações de tabelas. SELECT permite especificar as informações que você deseja sem informar ao Visual FoxPro como recuperar as informações. O Visual FoxPro determina a melhor forma de recuperar as informações.

Depois de criar uma consulta, ela é armazenada como um arquivo de programa do Visual FoxPro com extensão .qpr. Um programa de consulta pode ser executado com DO. Você deve incluir a extensão do arquivo de consulta ao executar uma consulta com DO, conforme mostrado no exemplo a seguir.

```foxpro
DO my_query.qpr
```

Emitir o comando CREATE QUERY sem argumentos adicionais abre uma nova janela de consulta. O nome QUERY1 é atribuído à consulta. Quando você sai da janela Query, pode salvar a consulta com um nome diferente.
