# Tratamento procedural de erros

Você pode detectar e tratar erros em uma ou várias linhas de código usando o comando ON ERROR e especificando qualquer comando ou expressão válida. No entanto, normalmente você usa o comando DO para especificar um procedimento ou programa de tratamento de erros. Normalmente, você usa ON ERROR como o manipulador de erros geral em seu aplicativo para aqueles erros que manipuladores de erro mais locais, como eventos Error e TRY...CATCH...FINALLY, não tratam.

Por exemplo, suponha que você tenha a seguinte linha de código inválida em um arquivo de programa (.prg):

```foxpro
qxy
```

Quando você executa o programa, o Visual FoxPro exibe a mensagem de erro apropriada, "Unrecognized command verb." No entanto, você pode criar uma rotina ON ERROR para detectar este comando inválido e executar um procedimento ou programa que trate este erro. As linhas de código a seguir precedem o comando inválido com o comando ON ERROR, que inclui a função ERROR( ) e exibe os resultados usando o comando ?:

```foxpro
ON ERROR ?ERROR()
qxy
```

Quando essas linhas de código são executadas, o comando ON ERROR detecta o erro e exibe o número de erro retornado pela função ERROR( ) para a mensagem de erro "Unrecognized command verb" na janela de saída ativa em vez da própria mensagem de erro.

Em sua forma básica, o código a seguir ilustra uma rotina ON ERROR:

```foxpro
LOCAL lcOldOnError
lcOldOnError = ON("ERROR") && Save default error handler.
* Call ON ERROR with an error procedure.
ON ERROR DO ErrHandler WITH ERROR(), MESSAGE()
* Insert code that error handling routine applies to.
* Reset original error handler.
ON ERROR &lcOldOnError
PROCEDURE ErrHandler
   LOCAL aErrInfo[1]
   AERROR(aErrInfo)
   DO CASE
      CASE aErrInfo[1] = ErrorNum && Specify appropriate error number.
         * Display appropriate message and insert code to fix error.
      OTHERWISE
         * Display generic message.
ENDPROC
```

Para obter mais informações, consulte ON ERROR Command. Você também pode incluir outros manipuladores de erro, como TRY...CATCH...FINALLY em código procedural.
