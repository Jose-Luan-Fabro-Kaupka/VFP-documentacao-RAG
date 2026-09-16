# Amostra Dynamically Format Grid Columns

Arquivo: ...\\Samples\\Solution\\Controls\\Grid\\Dyngrid.scx

Esta amostra ilustra a definição das propriedades DynamicForeColor e DynamicBackColor das colunas da grade.

O código de interesse nesta amostra está associado ao evento InteractiveChange da lista suspensa cboFormat.

Primeiro, o código limpa as configurações dinâmicas de cor de primeiro plano e de fundo:

```foxpro
oGrd.SetAll("dynamicbackcolor", "", "Column")
oGrd.SetAll("dynamicforecolor", "", "Column")
```

Em seguida, o código em uma instrução CASE define as novas propriedades DynamicForeColor ou DynamicBackColor. Por exemplo, a linha de código a seguir exibe itens descontinuados com ForeColor cinza.

```foxpro
oGrd.SetAll("dynamicforecolor", ;
   "IIF(discontinu, RGB(192,192,192), RGB(0,0,0))", "Column")
```

`Discontinu` é um campo lógico na tabela Products.
