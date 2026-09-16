# Função READKEY( )

Incluída para compatibilidade com versões anteriores com READ. Use o Form Designer em vez de READ.

Retorna um valor correspondente à tecla pressionada para sair de certos comandos de edição, ou um valor indicando como o último READ foi encerrado.

```foxpro
READKEY([expN])
```

# Valor de retorno

Valor de retorno - Numeric

# Observações

Se READKEY() é executado sem a expressão numérica opcional expN, o valor retornado representa a tecla pressionada para sair destes comandos de edição: APPEND, BROWSE, CHANGE, CREATE, EDIT, INSERT, MODIFY e READ.

Um inteiro entre 0 e 36, ou entre 256 e 292, é retornado. O valor retornado está entre 0 e 36 se os dados não foram modificados. O valor retornado está entre 256 e 292 se os dados foram modificados.

 Valores retornados por READKEY

Tecla(s) Sem atualização Atualização Significado

 Código Código

------ --------- ------ -------

Backspace

Seta para a esquerda 0 256 Voltar 1

Ctrl+H char.

Ctrl+S
