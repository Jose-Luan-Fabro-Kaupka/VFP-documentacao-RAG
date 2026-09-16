# Função INPUTBOX( )

Exibe uma caixa de diálogo modal usada por uma view parametrizada para entrada de uma única cadeia de caracteres.

```foxpro
INPUTBOX(cInputPrompt [, cDialogCaption [, cDefaultValue [, nTimeout [,cTimeoutValue] [,cCancelValue]]]])
```

#### Parâmetros
 **cInputPrompt**
Especifica o Prompt exibido acima da caixa de entrada de texto.
**cDialogCaption**
Especifica o texto a exibir na barra de título da caixa de diálogo.
**cDefaultValue**
Especifica um valor padrão a exibir na caixa de entrada de texto.
**nTimeout**
Especifica um valor de tempo limite em 1/1000 segundos. Especifique zero em nTimeout para impedir que a caixa de diálogo expire. Isso é idêntico a omitir nTimeout .
**cTimeoutValue**
Especifica o valor a retornar se ocorrer um tempo limite. cTimeoutValue não é retornado se nTimeout estiver definido como zero ou for omitido.
**cCancelValue**
Especifica um valor de caractere a retornar se o usuário sair da caixa de diálogo escolhendo o botão Cancel ou pressionando a tecla Esc.

# Observações

A caixa de diálogo exibe uma caixa de edição e botões OK e Cancel. O botão OK retorna o conteúdo da caixa de edição. Um tempo limite retorna o texto especificado em cTimeoutValue ou uma cadeia vazia se cTimeoutValue não for especificado. O botão Cancel ou a tecla Esc retorna o texto especificado em cCancelValue ou uma cadeia vazia se cCancelValue não for especificado.

# Exemplo 1

```foxpro
Y = "Nothing at all"
Y = INPUTBOX("TypeHere","Input ",Y,5000)
         && Displays dialog box for 5 seconds,
```

# Exemplo 2

O exemplo a seguir exibe uma caixa de diálogo por cinco segundos e exibe o valor de retorno na janela principal do Visual FoxPro. Se o usuário clicar em OK, a caixa de edição retorna o texto, que é o valor padrão, "Nothing at all," ou texto especificado pelo usuário. Se o usuário clicar em Cancel ou pressionar a tecla ESC, a caixa de edição retorna "Canceled." Se o usuário aguardar o período de tempo limite, a caixa de edição fecha e retorna "Timed Out."

```foxpro
CLEAR
Y = INPUTBOX("Type Here:", "Input Title",  ;
"Nothing at all", 5000, 'Timed Out', 'Canceled')
? Y
```
