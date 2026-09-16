# SYS(2001) - Status do comando SET ...

Retorna o status dos comandos SET especificados.

```foxpro
SYS(2001, cSETCommand [, 1 | 2])
```

#### Parâmetros
 **cSETCommand**
Especifica o comando SET cujo status SYS(2001) retorna.
**1 | 2**
Alguns comandos SET possuem duas ou mais configurações; por exemplo, SET PRINTER ON, SET PRINTER OFF e SET PRINTER TO FileName . Use SYS(2001) sem 1 ou 2 para retornar a configuração da chave ON ou OFF. Use SYS(2001) com 1 ou 2 para retornar as configurações adicionais. Consulte a Função SET( ) para uma lista de comandos SET para os quais informações adicionais são retornadas quando 1 ou 2 é incluído.

# Valor de retorno

Caractere

# Observações

SYS(2001) é idêntico a SET( ).

# Exemplo

```foxpro
? SYS(2001,'PRINTER')
? SYS(2001,'PRINTER',1)
```
