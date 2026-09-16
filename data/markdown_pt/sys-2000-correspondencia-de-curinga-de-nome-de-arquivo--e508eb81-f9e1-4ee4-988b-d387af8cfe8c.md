# SYS(2000) - Correspondência de curinga de nome de arquivo

Retorna o nome do primeiro arquivo em ordem alfabética por nome de arquivo e extensão, que corresponde a um skeleton de nome de arquivo.

```foxpro
SYS(2000, Skeleton [, 1])
```

#### Parâmetros
 **Skeleton**
Especifica o skeleton de nome de arquivo. O skeleton de arquivo pode conter os curingas ? e *.
**1**
Retorna o nome do próximo arquivo correspondente.

# Valor de retorno

Character

# Observações

A cadeia de caracteres vazia é retornada se um arquivo correspondente não puder ser encontrado.

# Exemplo

```foxpro
? SYS(2000,'FOX.*')
? SYS(2000,'FOX.*',1)
```
