# Comando ERROR

Gera um erro do Visual FoxPro.

Você pode usar o comando ERROR para testar rotinas de tratamento de erros ou para exibir mensagens de erro personalizadas.

```foxpro
ERROR nErrorNumber | nErrorNumber, cMessageText1 | [cMessageText2]
```

#### Parâmetros
 **nErrorNumber**
Especifica o número do erro a ser gerado. A mensagem de erro padrão do Visual FoxPro é usada quando um número de erro é especificado. Para uma lista de mensagens de erro do Visual FoxPro e seus números de erro, consulte Mensagens de erro listadas alfabeticamente.
**cMessageText1**
Especifica o texto exibido em uma mensagem de erro que fornece informações adicionais sobre o erro. Por exemplo, se você referenciar uma variável de memória que não existe, o Visual FoxPro fornece o nome da variável de memória na mensagem de erro.
**cMessageText2**
Especifica o texto exibido na mensagem de erro. Quando cMessageText2 é especificado em vez de nErrorNumber, o erro número 1098 do Visual FoxPro (erro definido pelo usuário) é gerado. Para mover uma parte da mensagem de erro para a próxima linha, use um retorno de carro (CHR(13)) em cMessageText2.

# Observações

Se uma rotina de tratamento de erros ON ERROR estiver em vigor quando ERROR é emitido, o Visual FoxPro executa a rotina ON ERROR. Se ocorrer um erro para um objeto, o evento Error do objeto é executado.

Se você emitir ERROR na janela Comando e uma rotina de tratamento de erros ON ERROR não estiver em vigor, o Visual FoxPro exibe a mensagem de erro. Se ERROR é emitido em um programa e uma rotina de tratamento de erros ON ERROR não estiver em vigor, o Visual FoxPro exibe a mensagem de erro e permite cancelar ou suspender o programa ou ignorar o erro.

> **Observação:** O evento Error não ocorre se uma rotina ON ERROR estiver na pilha de chamadas.

# Exemplos

O exemplo a seguir gera três mensagens de erro. A primeira linha de código exibe o erro "Variable not found" (Erro 12):

```foxpro
ERROR 12
```

A segunda linha de código gera o Erro 12 novamente, mas inclui o nome da variável MyVariable e exibe "Variable 'MyVariable' not found":

```foxpro
ERROR 12, 'MyVariable'
```

A terceira linha de código exibe uma mensagem de erro definida pelo usuário (Erro 1098) "My error message."

```foxpro
ERROR 'My error message'
```
