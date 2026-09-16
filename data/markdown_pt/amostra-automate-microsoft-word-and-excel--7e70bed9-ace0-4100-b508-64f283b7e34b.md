# Amostra Automate Microsoft Word and Excel

Arquivo: ...\Samples\Solution\OLE\Oleaut1.scx

Esta é uma amostra simples que mostra o Visual FoxPro como controlador de automação. Demonstra como selecionar dados de um banco de dados do Visual FoxPro, colocar os dados em uma planilha do Microsoft Excel, criar um gráfico dos dados usando Chart e, em seguida, exibir o gráfico no Word. Para usar esta amostra, você precisa de pelo menos Excel 5.0, Word 6.0 e Testdata.dbc, localizado no diretório ...\Samples\Data.

A linha de código a seguir cria uma referência a uma planilha do Microsoft Excel.

```foxpro
objXLsheet=createobject("Excel.Sheet")
```

A linha de código a seguir adiciona um gráfico à planilha.

```foxpro
objChart1 = objXLsheet.ChartObjects.Add(100, 100, 200, 200)
```

A linha de código a seguir cria uma referência ao Microsoft Word.

```foxpro
objWDdoc=createobject("word.basic")
oWordRef = GetObject('','word.basic')
```
