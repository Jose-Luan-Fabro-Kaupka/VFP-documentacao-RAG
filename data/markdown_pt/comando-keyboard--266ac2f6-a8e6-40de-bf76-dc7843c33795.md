# Comando KEYBOARD

Coloca a expressão de caracteres especificada no buffer do teclado.

Os caracteres permanecem no buffer até o Visual FoxPro solicitar entrada de teclado e então são processados como se fossem digitados. KEYBOARD pode criar demonstrações autoexecutáveis.

```foxpro
KEYBOARD cKeyboardValue [PLAIN] [CLEAR]
```

#### Parâmetros
 **cKeyboardValue**
Especifica a expressão colocada no buffer: cadeia de caracteres, rótulo de tecla, conjunto de rótulos ou função definida pelo usuário. Rótulos devem ficar entre chaves e aspas. A opção PAUSE nSeconds pode inserir uma pausa.
**PLAIN**
Ignora macros e comandos ON KEY LABEL ativos, inserindo o caractere literal.
**CLEAR**
Esvazia o buffer antes de preenchê-lo com cKeyboardValue.

# Observações

O buffer comporta até 128 caracteres. Quando está cheio, caracteres adicionais são ignorados.
