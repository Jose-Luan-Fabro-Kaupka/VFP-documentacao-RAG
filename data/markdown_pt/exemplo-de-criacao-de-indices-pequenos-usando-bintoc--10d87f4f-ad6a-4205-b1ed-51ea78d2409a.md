# Exemplo de criação de índices pequenos usando BINTOC( )

Arquivo: ...\Samples\Solution\Db\Index1.scx

Este exemplo mostra vários esquemas de indexação que você pode usar com tipos de dados numéricos e inteiros para obter economia significativa no tamanho do índice e no espaço em disco. Além disso, índices menores normalmente resultam em pesquisas mais rápidas. A função BINTOC() permite converter um valor inteiro (numérico) em uma representação binária de caracteres.

Sintaxe

BINTOC(nExpression [, nSize])

Dependendo do tamanho da expressão, você pode definir o parâmetro nSize para comportar seu valor com o menor número de caracteres.

A linha de código a seguir cria um índice em um campo numérico:

```foxpro
INDEX on line_no TAG line_no
```

Da próxima vez que trabalhar com índices em dados numéricos inteiros, considere usar algo como:

```foxpro
INDEX on BINTOC(line_no,1) TAG line_no
```
