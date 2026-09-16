# Como: personalizar consultas

Você pode personalizar suas consultas ainda mais no Query Designer. Você pode usar filtros para expandir ou restringir os resultados da sua consulta. Também pode adicionar expressões para executar cálculos ou funções nos dados de seus campos.

# Filtrando registros em consultas

Você pode usar expressões de filtro para restringir ou expandir o intervalo de registros que sua consulta recupera. Por exemplo, suponha que você deseja recuperar registros que atendam a mais de um critério; por exemplo, você deseja recuperar clientes de um determinado estado que tenham saldos pendentes maiores que US$ 1.000. Neste cenário, você deseja restringir o intervalo de registros que sua consulta recupera. Em contraste, suponha que você deseja recuperar registros que atendam a qualquer critério; por exemplo, clientes de Washington ou da Califórnia. Neste cenário, você deseja restringir o intervalo de registros que sua consulta recupera.

Quando você deseja criar expressões de filtro que incluam mais de um critério, use o operador lógico AND. Quando você deseja criar expressões de filtro que usem qualquer critério que especificar, use o operador lógico OR.

Você também pode combinar condições AND e OR para selecionar conjuntos específicos de registros. Por exemplo, você pode querer recuperar registros de clientes de Washington ou da Califórnia que tenham valores máximos de pedido maiores que US$ 5.000.

### Para especificar condições AND ou OR para expressões de filtro
- Abra a consulta no Query Designer .
- Clique na guia Filter e selecione a expressão de filtro desejada.
- Na coluna Logical, clique em AND ou OR .

Para obter mais informações, consulte Filter Tab, Query and View Designers.

# Eliminando registros duplicados em consultas

Você pode remover registros duplicados de consultas. Registros duplicados contêm campos em que todos os valores nos campos correspondem entre si.

### Para remover registros duplicados de consultas
- Abra a consulta no Query Designer .
- Clique na guia Miscellaneous e depois em No duplicates . Observação Selecionar No duplicates insere a palavra-chave DISTINCT antes dos campos na instrução SQL SELECT da consulta. Para obter mais informações, consulte SELECT - SQL Command .

# Recuperando o número ou percentual superior de registros

Você pode especificar quantos registros ou qual percentual de registros com os valores mais altos ou mais baixos em um campo específico você deseja que a consulta retorne. Por exemplo, a consulta pode exibir os registros com os 10 valores mais altos ou mais baixos em um campo específico ou os registros com os 10% mais altos ou mais baixos de valores no campo.

Usando a configuração Top na guia Miscellaneous, você pode definir um número ou um percentual de registros que deseja ver. Para definir se está escolhendo o topo ou a base, defina a ordem de classificação da sua consulta como descendente para ver o topo ou ascendente para ver a base.

### Para recuperar um número ou percentual de registros superiores
- Na guia Order By, selecione o campo para o qual deseja recuperar os valores superiores e escolha Descending para exibir os valores mais altos ou Ascending para exibir os valores mais baixos. Se estiver classificando em campos adicionais, coloque-os após o campo de valores superiores na lista order by.
- Na guia Miscellaneous, digite o número para o percentual ou o número de valores mais altos ou mais baixos que deseja recuperar na caixa Number of records . Para exibir um percentual, escolha Percent .
- Se não deseja que registros duplicados sejam incluídos no número ou percentual, escolha No duplicates .

# Adicionando expressões a consultas

Você pode criar consultas mais flexíveis e poderosas se incorporar expressões, seja em um filtro ou como campos de resultado. Você pode incluir funções e expressões na saída da sua consulta, usando a caixa na parte inferior da guia Fields. Se deseja nomear o campo que contém a expressão, pode adicionar um alias.

Por exemplo, você pode querer que os resultados da sua consulta incluam a soma de todos os valores de pedido com o alias `Total`:

```foxpro
SUM(orders.order_amt) AS Total
```

Você pode digitar uma expressão diretamente na caixa ou usar o Expression Builder na guia Fields.

### Para adicionar uma expressão à saída da sua consulta
- Na guia Fields, digite a expressão na caixa Functions and Expressions . -ou- Escolha o botão de diálogo para usar o Expression Builder e insira uma expressão na caixa Functions and expressions .
- Escolha o botão Add para colocar a expressão na caixa Selected fields . Observação Valores nulos são ignorados em cálculos. Para obter mais informações sobre valores nulos em expressões, pesquise por "Null Values".

Em vez de pesquisar registros que correspondam a um ou mais campos, você pode usar uma expressão para combinar dois campos ou executar um cálculo baseado em um campo e pesquisar registros que correspondam ao campo combinado ou calculado.

Você pode digitar expressões diretamente na caixa Example. Se deseja alguma ajuda, pode usar o Expression Builder, que está disponível no botão de diálogo ao lado da caixa Expressions and Functions na guia Fields.

Por exemplo, usando a tabela Orders, você pode querer verificar os descontos totais de um cliente combinando valor do pedido e desconto do pedido em uma expressão como a seguinte:

```foxpro
Orders.order_amt * Orders.order_dsc
```
