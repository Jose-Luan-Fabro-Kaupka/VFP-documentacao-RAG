# Arquivo de log do Coverage Profiler

O Coverage Profiler usa um arquivo de log gerado pelo Visual FoxPro quando você usa a opção Coverage no menu Tools do Debugger ou usa o comando SET COVERAGE como no comando a seguir:

```foxpro
SET COVERAGE TO cCoverage.log
```

Quando você usa o comando, a cláusula ADDITIVE permite evitar a substituição de um log existente. Este comando inicia o fluxo de dados e abre o arquivo cCoverage.log, um arquivo de texto que reunirá o fluxo de detalhes sobre o arquivo ou aplicação que você examina.

Um arquivo de log de cobertura consiste em registros em linhas delimitadas por vírgula. A lista a seguir descreve a estrutura de cada registro.

| Item | Descrição |
| --- | --- |
| 1 | tempo de execução |
| 2 | classe que executa o código |
| 3 | objeto, método ou procedimento no qual o código é encontrado ou chamado |
| 4 | número da linha dentro do método ou procedimento |
| 5 | arquivo totalmente definido |
| 6 | nível da pilha de chamadas |

Após especificar o nome do arquivo de log, execute o programa ou aplicação que deseja examinar. Quando você encerra o programa, pode usar o comando SET COVERAGE TO para interromper o fluxo de dados para o log de cobertura.

Você pode visualizar o log de cobertura iniciando o Coverage Profiler no menu Tools ou usando o comando DO como no comando a seguir:

```foxpro
DO (_COVERAGE) [WITH cCoverage]
```

O Visual FoxPro solicita o nome se você não especificar um arquivo de log. A variável de sistema _COVERAGE no Visual FoxPro tem como padrão a aplicação Coverage Profiler, Coverage.app.
