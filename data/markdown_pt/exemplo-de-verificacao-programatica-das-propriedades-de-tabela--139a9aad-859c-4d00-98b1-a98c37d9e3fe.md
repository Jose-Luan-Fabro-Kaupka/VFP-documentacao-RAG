# Exemplo de verificação programática das propriedades de tabela

Arquivo: ...\Samples\Solution\Db\Info.scx

Este exemplo ilustra como recuperar informações sobre uma tabela em tempo de execução.

# Informações de campo

A função AFIELDS( ) fornece a maior parte das informações sobre campos de tabela exibidas neste exemplo. Além das informações exibidas, AFIELDS( ) fornece dados sobre expressões e mensagens de validação de campos e tabelas, expressões e mensagens de gatilhos, bem como nomes longos e comentários de tabelas no banco de dados.

# Informações de índice

As funções TAG( ) e KEY( ) fornecem informações de índice.

```foxpro
lo = THISFORM.edtProperties
FOR i = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(i))  && Checks for tags in the index
      lo.Value = lo.Value + TAG(i) + "  " + KEY(i)
   ELSE
      EXIT
   ENDIF
ENDFOR
```
