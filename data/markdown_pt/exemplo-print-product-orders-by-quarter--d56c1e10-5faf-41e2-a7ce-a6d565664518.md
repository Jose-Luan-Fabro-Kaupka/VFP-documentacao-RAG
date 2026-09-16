# Exemplo Print Product Orders By Quarter

Arquivo: ...\Samples\Solution\Reports\Ordgraph.scx

Este exemplo ilustra a geração e impressão de gráficos sob demanda. O Visual FoxPro permite adicionar gráficos a formulários como OleControls ou OleBoundControls. O último representa um gráfico vinculado a dados usando um campo General.

Se você pretende usar o gerador de relatórios do Visual FoxPro para imprimir gráficos, precisa usar campos General para armazenar os gráficos. A maneira mais fácil de criar um novo gráfico em um campo General é usar o comando APPEND GENERAL, por exemplo:

```foxpro
APPEND GENERAL graphfield CLASS "msgraph"
```

O exemplo acima criará um gráfico em um campo General; no entanto, ele não conterá seus dados. A cláusula DATA na verdade passa dados ao gráfico.

O código a seguir percorre registros que já contêm dados e constrói uma cadeia de caracteres para passar ao gráfico com APPEND GENERAL .... DATA:

```foxpro
SCAN NEXT m.totrecs
   m.cData = ""+TAB+m.f2+TAB+m.f3+TAB+m.f4+CRLF+;
      EVAL(fields(1))+ TAB + ;
      ALLTRIM(STR(EVAL(field(2))))+ TAB +;
      ALLTRIM(STR(EVAL(field(3))))+ TAB + ;
      ALLTRIM(STR(EVAL(field(4))))
   m.cDetails = ;
f2+"-" +ALLTRIM(STR(EVAL(FIELD(2)))) ;
      + CRLF + f3+"-" +ALLTRIM(STR(EVAL(FIELD(3)))) ;
      + CRLF + f4+" - "+ALLTRIM(STR(EVAL(FIELD(4)))) +CRLF
   INSERT INTO prodsales ;
VALUES(SalesData.prod_name,tmpgrph.graph,m.cDetails)
   APPEND GENERAL prodsales.sales DATA m.cData
ENDSCAN
```

Depois de ter uma tabela ou cursor contendo um campo General com seus gráficos, você pode imprimi-lo em um relatório do Visual FoxPro usando o comando REPORT FORM. Você não pode incluir um controle ActiveX em um relatório.
