# SYS(2012) - Tamanho de bloco de campo Memo

Retorna o tamanho de bloco de campo memo de uma tabela.

```foxpro
SYS(2012 [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea | cTableAlias**
Especifica o número da área de trabalho ou o alias da tabela para a qual o tamanho de bloco de campo memo é retornado. nWorkArea especifica um número de área de trabalho e cTableAlias especifica um alias de tabela. Se você não especificar uma área de trabalho ou alias, SYS(2012) retorna o tamanho de bloco de campo memo da tabela aberta na área de trabalho atualmente selecionada. SYS(2012) retorna 0 se uma tabela não estiver aberta na área de trabalho especificada ou se a tabela não tiver um campo memo.

# Valor de retorno

Caractere

# Observações

Para obter mais informações sobre como especificar o tamanho de bloco de campo memo de uma tabela, consulte Comando SET BLOCKSIZE.
