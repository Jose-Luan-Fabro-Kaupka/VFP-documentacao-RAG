# Como: filtrar registros em views

Quando você acessa uma fonte de dados local ou remota, pode recuperar quantidades potencialmente grandes de dados. No entanto, você pode restringir o escopo dos registros somente àqueles que precisa para a view fornecendo um filtro. Filtrar registros também reduz o tráfego de rede ao trabalhar com dados remotos e aumenta o desempenho da sua view.

Você pode filtrar registros em views especificando uma expressão de filtro. Ao gerar a view, o Visual FoxPro avalia a expressão de filtro e compara o resultado com valores nos campos da view. Se os valores atendem aos requisitos da expressão, o Visual FoxPro inclui os registros no conjunto de resultados. Adicionar uma expressão de filtro adiciona uma cláusula WHERE à instrução SQL da view.

Por exemplo, suponha que você deseja criar um filtro que inclua somente clientes de um determinado país. Nas linhas de código a seguir, a cláusula WHERE contém uma expressão de filtro que seleciona todos os clientes em uma tabela de clientes onde o campo country na tabela de clientes contém o valor "Sweden":

```foxpro
SELECT * FROM Customer ;
   WHERE Customer.Country = 'Sweden'
```

Este código aumenta o desempenho recuperando somente os registros de um determinado país em vez de todos os clientes. No entanto, este código também exige que você crie uma view separada para cada país porque o valor real é codificado na instrução SQL SELECT da view. Em vez disso, você pode criar uma view parametrizada que usa um parâmetro na expressão de filtro para aceitar um valor para a cláusula WHERE. Para obter mais informações, consulte How to: Create Parameterized Views.

### Para filtrar registros em uma view
- Abra a view no View Designer e clique na guia Filter.
- Na lista Field Name, selecione um dos seguintes: Um campo de tabela que deseja incluir na expressão de filtro. -OU- <Expression> para abrir o Expression Builder para que você possa construir uma expressão de filtro. Observação Se você está criando uma view de uma fonte de dados remota, as funções disponíveis no Expression Builder refletem as funções suportadas por esse servidor. Para uma lista de funções que seu servidor remoto suporta, consulte a documentação do seu servidor. O Visual FoxPro não tenta analisar as expressões que você especifica; em vez disso, ele as passa para o servidor remoto.
- Na lista Criteria, selecione o operador de comparação que deseja usar. Dica Para negar a condição, clique na coluna NOT para a expressão.
- Na caixa Example, digite o valor ou expressão que deseja usar para comparar o valor do campo.

Para obter mais informações, consulte Filter Tab, Query and View Designers e Expression Builder Dialog Box.
