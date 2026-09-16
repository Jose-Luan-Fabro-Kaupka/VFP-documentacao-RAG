# Como: criar exibições parametrizadas

Você pode filtrar registros de uma exibição sem criar exibições separadas para cada valor usando uma exibição parametrizada. Ela usa uma instrução SQL SELECT com uma cláusula WHERE cuja expressão de filtro contém um parâmetro. O valor pode ser fornecido posteriormente pelo usuário ou por programação. Nomes de parâmetros podem combinar letras, números e aspas simples.

### Para especificar um parâmetro de filtro
- Abra a exibição no Designer de Exibições e clique na guia Filter.
- Crie um filtro ou selecione um existente.
- Na caixa Example, digite o nome do parâmetro. Para solicitar o valor ao abrir a exibição, coloque um ponto de interrogação (?) imediatamente antes do nome. A caixa View Parameter será exibida. O nome é avaliado como expressão do Visual FoxPro; se a avaliação falhar, o valor será solicitado e enviado à fonte de dados como parte de SQL SELECT.

Para obter mais informações, consulte Como: editar exibições e Guia Filter, Designers de Consulta e Exibição.

### Para criar uma exibição parametrizada por meio de programação
- Use o comando CREATE SQL VIEW com a cláusula AS para especificar uma instrução SQL SELECT.
- Na cláusula WHERE, inclua a expressão de filtro com o nome do parâmetro no local apropriado.

Para obter mais informações, consulte Comando CREATE SQL VIEW e Comando SELECT - SQL.

O código a seguir abre o banco de dados de exemplo Northwind e cria uma exibição que seleciona os registros de Customers cujo campo Country corresponde a `cCountry`:

```foxpro
OPEN DATABASE HOME(2) + "Northwind\Northwind"
CREATE SQL VIEW Customer_Remote_View ;
   AS SELECT * FROM Customers WHERE Customers.Country = ?cCountry
```

Ao abrir a exibição, o Visual FoxPro solicita um valor e exibe os resultados:

```foxpro
USE Customer_Remote_View
BROWSE
```

Ao terminar, exclua a exibição:

```foxpro
DELETE VIEW Customer_Remote_View
```

Você também pode passar o valor por programação. O código a seguir cria a mesma exibição sem o ponto de interrogação e armazena "Sweden" em `cCountry`:

```foxpro
OPEN DATABASE HOME(2) + "Northwind\Northwind"
CREATE SQL VIEW Customer_Remote_View ;
   AS SELECT * FROM Customers WHERE Customers.Country = cCountry
cCountry = 'Sweden'
USE Northwind!Customer_Remote_View
BROWSE
```

Ao terminar:

```foxpro
DELETE VIEW Customer_Remote_View
```
