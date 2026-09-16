# SYS(3055) — Complexidade das cláusulas FOR e WHERE

Define o nível de complexidade das cláusulas FOR e WHERE em comandos e funções que oferecem suporte a essas cláusulas.

```foxpro
SYS(3055 [, nComplexity])
```

#### Parâmetros
**nComplexity**
Especifica o nível de complexidade. O intervalo válido para nComplexity é de 320 a 2040. O valor padrão é 320. Se você especificar um valor ímpar, ele será arredondado para baixo até o inteiro par mais próximo.

# Valor de retorno

Caractere

# Observações

Se você receber o erro Espaço de pilha insuficiente (Erro 1308) ou SQL: instrução muito longa (Erro 1812), poderá aumentar a complexidade das cláusulas FOR e WHERE para ajudar a evitar o erro.

Por exemplo, chamar TABLEUPDATE( ) para uma tabela ou exibição local que não usa campos-chave gera uma cláusula WHERE longa para localizar a linha de atualização. O número padrão de campos aceitos na cláusula WHERE é 40. Se você receber o erro SQL: instrução muito longa (Erro 1812), use um campo-chave para a atualização ou aumente a complexidade da cláusula WHERE com SYS(3055). Se usar SYS(3055), aumente seu valor para oito vezes o número de campos da tabela:

```foxpro
= SYS(3055, 8 * MIN(40, FCOUNT()))
```

Se SYS(3055) for emitida sem o argumento nComplexity, sua configuração atual será retornada.

> **Observação:** Esta função também determina o número de itens que você pode listar na cláusula IN de uma consulta.

Os comandos e funções a seguir oferecem suporte às cláusulas FOR ou WHERE:

| APPEND FROM | APPEND FROM ARRAY | AVERAGE |
| --- | --- | --- |
| BLANK | BROWSE | CALCULATE |
| CHANGE | COPY TO ARRAY | COPY TO |
| COUNT | DEFINE PAD | DELETE |
| DELETE - SQL | DISPLAY | EXPORT |
| FOR( ) | INDEX | LABEL |
| LIST | LOCATE | RECALL |
| REPLACE | REPLACE FROM ARRAY | REPORT |
| SCAN ... ENDSCAN | SELECT - SQL | SORT |
| SUM | TABLEUPDATE( ) | UPDATE - SQL |
