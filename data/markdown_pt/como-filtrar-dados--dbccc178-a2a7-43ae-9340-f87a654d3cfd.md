# Como: filtrar dados

Você pode limitar os registros que acessa apenas aos dados desejados usando um índice filtrado ou uma condição de filtro temporária. Quando você cria um índice filtrado, o Visual FoxPro cria chaves de índice no arquivo de índice somente para os registros que correspondem à expressão de filtro. Índices filtrados são úteis para criar condições de filtro complexas.

> **Observação:** Não é recomendado usar valores diferentes de valores de campo, constantes e funções integradas para criar expressões de filtro. Você não pode especificar expressões de filtro para índices binários.

### Para criar índice filtrado
- Abra o Table Designer para modificar a tabela e escolha a guia Indexes.
- Na caixa Filter, digite uma expressão de filtro. -OU- Construa uma expressão de filtro clicando no botão de reticências ( ... ) à direita da caixa.
- Escolha OK .

Por exemplo, a expressão de filtro a seguir seleciona somente os registros de clientes no Canadá:

```foxpro
customer.country = "Canada"
```

### Para criar índices filtrados programaticamente
- Use o comando INDEX e inclua a cláusula FOR para especificar uma expressão de filtro.

Por exemplo, suponha que você queira preparar um mailing para os representantes de vendas da sua empresa e deseja classificar o mailing por país. Você pode criar um índice que filtra a tabela employee para que apareçam somente os registros de representantes de vendas, ordenados por país e sobrenome. O código a seguir cria um índice filtrado e exibe os dados filtrados em uma janela browse:

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Employee
INDEX ON country+last_name FOR title = "Sales Representative" ;
TAG reps_cntry
BROWSE
```

Quando você visualiza a janela browse, somente os representantes de vendas são exibidos; os registros de outros funcionários não aparecem de forma alguma na janela browse.
 Um índice filtrado constrói um índice somente para registros que correspondem à expressão de filtro.

Para obter mais informações, consulte INDEX Command.

### Filtros temporários

Você também pode filtrar dados temporariamente sem criar um índice filtrado.

### Para filtrar dados temporariamente
- Use o comando SET FILTER. SET FILTER é particularmente útil quando você deseja especificar uma condição temporária que os registros em uma tabela devem atender para serem acessados.

No exemplo a seguir, SET FILTER filtra a tabela Customer para mostrar somente os clientes na Alemanha:

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
SET FILTER TO country = "Germany"
BROWSE
```

SET FILTER aceita qualquer expressão lógica Visual FoxPro válida como condição de filtro. Você pode desativar o filtro da tabela atual usando SET FILTER TO sem uma expressão.

Depois de usar SET FILTER, somente os registros que satisfazem a condição de filtro estão disponíveis na tabela. Todos os comandos que acessam a tabela respeitam a condição SET FILTER. Você pode definir um filtro separado para cada tabela aberta.

Para obter mais informações, consulte SET FILTER Command.
