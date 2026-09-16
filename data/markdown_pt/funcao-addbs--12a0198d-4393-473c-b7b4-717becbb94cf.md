# Função ADDBS( )

Adiciona uma barra invertida (se necessário) a uma expressão de caminho.

```foxpro
ADDBS(cPath)
```

#### Parâmetros
 **cPath**
Especifica o nome do caminho ao qual a barra invertida será adicionada.

# Valor de retorno

Caractere

# Exemplo

O código a seguir exibe um caminho de diretório e demonstra que a função ADDBS( ) adiciona uma barra invertida se ela não existir, mas não a duplica se já existir.

```foxpro
*-- Both print C:\Windows\
? ADDBS( "C:\Windows" )
? ADDBS( "C:\Windows\" )
```
