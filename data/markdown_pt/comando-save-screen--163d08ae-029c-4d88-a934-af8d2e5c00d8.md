# Comando SAVE SCREEN

Salva uma imagem da janela principal do Visual FoxPro ou de uma janela definida pelo usuário ativa no buffer de tela, em uma variável ou em um elemento de matriz.

```foxpro
SAVE SCREEN [TO VarName]
```

#### Parâmetros
 **TO VarName**
Especifica a variável ou o elemento de matriz no qual a imagem da tela ou da janela é salva.

# Observações

Use RESTORE SCREEN para exibir novamente imagens salvas no buffer de tela, em uma variável ou em um elemento de matriz.

Variáveis ou elementos de matriz que contêm uma imagem da janela principal do Visual FoxPro ou de uma janela definida pelo usuário têm tipo de dados S quando você visualiza as variáveis ou os elementos de matriz com DISPLAY ou LIST MEMORY.

Se emitido sem a cláusula TO VarName, SAVE SCREEN salva a janela principal do Visual FoxPro ou a janela definida pelo usuário no buffer de tela.
