# Função FKLABEL( )

Retorna o nome da tecla de função (F1, F2, F3 ...) a partir do número correspondente da tecla de função.

```foxpro
FKLABEL(nFunctionKeyNumber)
```

#### Parâmetros
 **nFunctionKeyNumber**
Especifica o número da tecla de função. O valor de nFunctionKeyNumber deve ser de 0 até o número de teclas de função menos 1. FKLABEL( ) retorna a cadeia de caracteres vazia se nFunctionKeyNumber for maior que o número de teclas de função menos 1. O número de teclas de função pode ser determinado com FKMAX( ).

# Valor de retorno

Caractere

# Observações

As teclas de função podem ser programadas com SET FUNCTION.

O valor retornado por FKLABEL( ) é afetado por SET COMPATIBLE. Quando COMPATIBLE é definido como FOXPLUS (o padrão), FKLABEL( ) retorna as teclas de função. Quando COMPATIBLE é definido como DB4, FKLABEL( ) retorna as teclas de função e combinações de teclas de função (F1, CTRL+F1, SHIFT+F1, F2, CTRL+F2, SHIFT+F2, ...).

# Exemplo

```foxpro
CLEAR
SET COMPATIBLE OFF
? 'COMPATIBLE OFF'
?
FOR nCount = 1 TO FKMAX()  && Loop for # of function keys
   ? FKLABEL(nCount)  && Display programmable function keys
ENDFOR
SET COMPATIBLE ON
?
? 'COMPATIBLE ON'
?
FOR nCount = 1 TO FKMAX()  && Loop for # of function keys
   ? FKLABEL(nCount)  && Display programmable function keys
ENDFOR
```
