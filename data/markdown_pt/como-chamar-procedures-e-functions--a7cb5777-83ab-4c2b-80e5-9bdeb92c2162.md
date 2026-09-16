# Como: chamar procedures e functions

Você pode chamar funções nativas do Visual FoxPro, user-defined functions e procedures de diferentes maneiras. Além disso, você pode chamar user-defined functions (UDFs) da mesma forma que chama procedures. Você pode chamar procedures que cria em um arquivo de programa (.prg) como se fossem programas independentes ou como functions se seus procedures retornarem valores que você deseja usar.

> **Dica:** Se você incluir procedures e user-defined functions em um arquivo de programa (.prg) separado, pode abrir esses arquivos usando o comando SET PROCEDURE. Por exemplo, suponha que você tenha um arquivo chamado ProcFile.prg. A linha de código a seguir abre o arquivo:

```foxpro
SET PROCEDURE TO ProcFile.prg
```

### Para chamar uma função Visual FoxPro ou user-defined
- Chame a função sem armazenar o valor de retorno. -OU-
- Chame a função e atribua o valor de retorno a uma variável. -OU-
- Inclua a chamada de função dentro de outro comando ou função.

Algumas funções também aceitam dados como argumentos passados do programa chamador. Para obter mais informações, consulte Passing Data to Parameters e Parameters in Procedures and Functions.

No exemplo a seguir, a primeira linha de código chama a função DATE( ), que retorna a data atual do sistema, sem realizar operações com o valor de retorno. A segunda linha de código armazena o valor de retorno em uma variável chamada `dToday`. A terceira linha de código inclui a função em outro comando e envia o valor de retorno para a janela de saída atualmente ativa. A quarta linha de código inclui a função em outra função e passa o valor de retorno para a função externa, que retorna o dia da semana.

```foxpro
DATE()
dToday = DATE()
? DATE()
DOW(DATE())
```

Para obter mais informações, consulte Returning Data from Procedures and Functions.

### Para chamar um procedure
- Use o comando DO seguido do nome do procedure.

No exemplo a seguir, o comando DO chama procedures chamados myProc1 e myProc2. A primeira linha de código chama myProc1 sem argumentos. A segunda linha de código inclui a cláusula WITH no comando DO para passar uma lista de argumentos para myProc2.

```foxpro
DO myProc1
var1=4
var2=5
DO myProc2 WITH (var1, var2)
```

Para obter mais informações, consulte DO Command.
