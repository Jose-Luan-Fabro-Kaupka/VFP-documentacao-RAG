# Comando PUSH KEY

Coloca todas as configurações atuais do comando ON KEY LABEL em uma pilha na memória.

```foxpro
PUSH KEY [CLEAR]
```

#### Parâmetros
 **CLEAR**
Limpa todas as atribuições de teclas atuais da memória.

# Observações

PUSH KEY, quando usado com POP KEY, permite salvar atribuições de teclas definidas com comandos ON KEY LABEL, alterar essas atribuições e depois restaurar as atribuições anteriores.

Por exemplo, você pode querer usar um novo conjunto de comandos ON KEY LABEL ao abrir uma janela Browse. Antes de abrir a janela Browse, use PUSH KEY para salvar as atribuições de teclas ON KEY LABEL atuais na memória. Você pode então adicionar ou alterar atribuições ON KEY LABEL especificamente para a janela Browse. Depois de fechar a janela Browse, suas atribuições de teclas ON KEY LABEL anteriores podem ser restauradas da memória com POP KEY.

As configurações ON KEY LABEL são colocadas na pilha e removidas da pilha em ordem last-in, first-out.

DISPLAY STATUS e LIST STATUS mostram as atribuições de teclas atuais definidas com comandos ON KEY LABEL. As atribuições de teclas ocupam memória, portanto, todo PUSH KEY deve ter um POP KEY correspondente para garantir que o uso de memória do seu aplicativo não cresça desnecessariamente.
