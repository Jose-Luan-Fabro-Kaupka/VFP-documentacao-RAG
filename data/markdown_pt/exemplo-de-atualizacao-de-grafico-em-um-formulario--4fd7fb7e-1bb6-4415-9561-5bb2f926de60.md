# Exemplo de atualização de gráfico em um formulário

Arquivo: ...\Samples\Solution\OLE\Stock.scx

Este exemplo ilustra a seleção de dados de uma tabela e a passagem deles para o MS Graph para atualizar os valores em um gráfico. A maior parte do código para fazer isso está associada ao evento InteractiveChange da caixa de combinação cboMonth.

# Selecionar os dados em um cursor

```foxpro
SELECT date, close;
  FROM Stock1 WHERE MONTH(date) = THIS.Value ;
  ORDER BY date INTO CURSOR wtemp
```

# Criar uma cadeia de caracteres contendo os dados selecionados

```foxpro
SELECT wtemp
lcData = " " + TAB + "Closing Price" + CRLF
SCAN
 lcData = lcData + DTOC(date)
 lcData = lcData + TAB
 lcData = lcData + ALLTRIM(STR(close)) + CRLF
ENDSCAN
```

# Enviar a cadeia de caracteres para o MS Graph

```foxpro
SELECT Graph
APPEND GENERAL msgraph DATA lcData
```
