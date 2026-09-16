# Exemplo Manipulate Display Characteristics of a Graph

Arquivo: ...\Samples\Solution\OLE\Olegraph.scx

Este exemplo mostra como incorporar MS Graph em seus aplicativos. MS Graph 5.0 é um servidor Automation que o Visual FoxPro pode automatizar usando a função padrão CREATEOBJECT( ). Com o Visual FoxPro, objetos Graph podem ser incorporados em controles OLE vinculados ou não vinculados. Um OleBoundControl (vinculado a um campo General) é a única forma de inserir dados programaticamente em um gráfico.

O suporte de automação do MS Graph fornece acesso apenas a um objeto graph, não à sua planilha de dados. Dados podem ser inseridos em um Graph apenas com o comando APPEND GENERAL em um campo General. O código a seguir usa a propriedade HasLegend e é um exemplo de automação:

```foxpro
cGData = ""+TAB+"Cats"+TAB+"Dogs"+CRLF+;
      "1994"+TAB+"11"+TAB+"22"+CRLF+;
      "1995"+TAB+"33"+TAB+"44"+CRLF+;
      "1996"+TAB+"55"+TAB+"55"+CRLF
APPEND GENERAL gen1 CLASS "msgraph.chart" DATA m.cGData
THIS.OleBoundControl1.ControlSource = "Gen1"
THIS.OleBoundControl1.HasLegend = .F.
```

O comando APPEND GENERAL neste caso cria um novo objeto chart. Se você não incluir a cláusula CLASS "msgraph.chart", o gráfico é apenas atualizado. A cláusula CLASS criará um novo gráfico e substituirá qualquer formatação existente.
