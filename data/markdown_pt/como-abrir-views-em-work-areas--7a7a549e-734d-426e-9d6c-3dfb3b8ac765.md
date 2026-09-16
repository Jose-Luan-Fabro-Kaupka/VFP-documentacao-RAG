# Como: abrir views em work areas

Você pode abrir uma view em work areas separadas de forma semelhante a como pode abrir uma tabela em work areas diferentes. Para obter mais informações, consulte How to: Open Tables in Work Areas.

No entanto, ao contrário das tabelas, views recuperam um novo conjunto de dados cada vez que você usa a view. Quando você abre a view programaticamente com o comando USE, pode abrir instâncias adicionais da view sem recuperar dados da fonte de dados. Isso é particularmente útil quando você deseja abrir uma remote view em múltiplas work areas sem esperar para baixar dados de fontes de dados remotas.

### Para abrir outra instância de uma view sem baixar dados
- Abra a view com o comando USE e inclua a cláusula NOREQUERY ou AGAIN.

Você pode especificar um número de data session ao usar a cláusula NOREQUERY. Se omitir um número de data session, o Visual FoxPro pesquisa em todas as data sessions. Se um conjunto de resultados aberto for encontrado para a view, o Visual FoxPro abre o cursor novamente no mesmo conjunto de resultados. Se nenhum conjunto de resultados aberto for encontrado, o Visual FoxPro recupera um novo conjunto de resultados para a view. Como é verdade com tabelas, se a view não for encontrada, o Visual FoxPro abre um novo cursor para a view.

Se deseja que o Visual FoxPro pesquise somente a data session atual por um conjunto de resultados aberto, use a cláusula AGAIN. Abrir outra instância de uma view com a cláusula AGAIN é equivalente a usar a cláusula NOREQUERY com o número da session atual.

Para obter mais informações, consulte USE Command.

Por exemplo, o código a seguir abre o banco de dados de exemplo Northwind usando o comando OPEN DATABASE, cria uma remote view chamada Product_View usando o comando CREATE SQL VIEW e seleciona todos os registros na tabela Products. O comando USE abre a view e o comando BROWSE exibe a primeira instância da view em uma janela browse. O comando SELECT seleciona a work area da view e o comando USE abre a mesma view com a cláusula NOREQUERY. Desta vez, o comando BROWSE exibe a view em uma janela browse sem recuperar os dados da fonte de dados:

```foxpro
OPEN DATABASE HOME(2) + "Northwind\Northwind"
CREATE SQL VIEW Product_View AS SELECT * FROM Products
USE Product_View
BROWSE
SELECT 0
USE Product_View NOREQUERY
BROWSE
```

O código a seguir usa o comando USE para abrir a view e o comando BROWSE para exibir a view em uma janela browse. O segundo comando USE abre a view da data session atual com a cláusula AGAIN usando um alias diferente. O comando BROWSE exibe a view com o alias diferente:

```foxpro
OPEN DATABASE HOME(2) + "Northwind\Northwind"
USE Product_View
BROWSE
USE Product_View AGAIN IN 0
BROWSE
```

O comando a seguir exclui a view quando você termina de trabalhar com ela:

```foxpro
DELETE VIEW Product_View
```

Para obter mais informações, consulte OPEN DATABASE Command, CREATE SQL VIEW Command, BROWSE Command, SELECT Command e DELETE VIEW Command.
