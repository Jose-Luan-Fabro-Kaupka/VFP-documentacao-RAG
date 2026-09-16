# Comando RESTORE SCREEN

Restaura a janela principal do Visual FoxPro ou uma janela definida pelo usuário previamente salva no buffer de tela, em uma variável ou em um elemento de array.

```foxpro
RESTORE SCREEN   [FROM VarName]
```

#### Parâmetros
 **FROM VarName**
Especifica o nome de uma variável ou elemento de array do qual você deseja restaurar a imagem da tela ou da janela.

# Observações

Use SAVE SCREEN para colocar a janela principal atual do Visual FoxPro ou a janela definida pelo usuário ativa no buffer de tela, em uma variável ou em um elemento de array.

Variáveis ou elementos de array contendo imagens de tela ou janela armazenadas têm um tipo de dados S quando você visualiza as variáveis ou elementos de array com DISPLAY ou LIST MEMORY. A janela principal do Visual FoxPro ou janelas definidas pelo usuário salvas em variáveis ou elementos de array também podem ser salvas e restauradas de arquivos de variáveis com SAVE TO e RESTORE FROM.

Se emitido sem a cláusula FROM, RESTORE SCREEN restaura a janela principal do Visual FoxPro ou a janela definida pelo usuário do buffer de tela.
