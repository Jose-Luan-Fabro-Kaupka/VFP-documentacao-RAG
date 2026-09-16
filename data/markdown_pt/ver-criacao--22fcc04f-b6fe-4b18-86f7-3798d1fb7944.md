# Ver Criação

O processo básico para criar uma visualização é geralmente o mesmo, independentemente do método the usado e do tipo de visualização criada:
 - Determine o tipo de visualização que você precisa criar.
- Especifique as tabelas ou visualizações das quais deseja recuperar registros e suas condições de associação.
- Selecione os campos dos quais deseja recuperar dados.
- Especifique quaisquer critérios adicionais para recuperar registros dessas tabelas.
- Especifique se deseja atualizar as tabelas originais ou tabelas base usadas para construir a visualização.
- Gere a visualização para recuperar e visualizar os registros resultantes.

Semelhante às consultas, quando você cria uma visualização, o Visual FoxPro cria e executa uma instrução SQL que define o conjunto de dados para a visualização usando a definição de visualização que você criou. Você também pode definir propriedades para visualizações.

# Combinando visualizações

Você pode combinar visualizações quando precisar de um subconjunto de dados de outras visualizações ou se desejar combinar dados locais e remotos em uma única visualização. A visualização A construída a partir de outras visualizações é chamada de visualização de nível superior. A A visualização construída a partir de tabelas locais e visualizações locais ou remotas é chamada de visualização multicamadas.

O processo básico para combinar dados locais e remotos em uma única visualização é descrito nas seguintes etapas:
 - Crie uma visualização remota.
- Crie uma visualização local e adicione a visualização remota que você criou.
- Adicione quaisquer tabelas locais desejadas à visualização local e junte-as em um campo comum.
- Na visualização local, defina os campos e filtre os registros que desejar.
- Execute a visualização.
- Atualize os resultados da visualização para atualizar a tabela local e a visualização remota.
- Feche a visualização local e depois a visualização remota para atualizar os dados no servidor remoto.

Você também pode combinar dados locais e remotos em uma visualização criando uma nova visualização local com base em uma visualização local e em uma visualização remota. Você pode ter vários níveis de visualizações entre a visualização de nível superior e as tabelas base locais ou remotas. Ao usar uma visualização multicamadas, as visualizações nas quais a visualização de nível superior se baseia e quaisquer tabelas base do Visual FoxPro usadas nas visualizações de nível superior ou intermediário aparecem na janela Sessão de Dados do banco de dados. As tabelas remotas não aparecem na janela Sessão de Dados.

Por exemplo, o código a seguir usa o banco de dados de exemplo Northwind e cria uma exibição local que combina dados de uma tabela de funcionários local e da tabela de pedidos remotos. Você pode usar o código a seguir:

```foxpro
OPEN DATABASE HOME(2) + "Northwind\Northwind"
CREATE SQL VIEW Local_Employee_View AS SELECT * FROM Employees
CREATE SQL VIEW Remote_Orders_View ;
   CONNECTION Remote_01 AS SELECT * FROM Orders
CREATE SQL VIEW Local_Employee_Remote_Orders_View ;
   AS SELECT * FROM Northwind!Local_Employee_View, ;
   Northwind!Remote_Orders_View ;
   WHERE Local_Employee_View.Emp_ID = Remote_Orders_View.Emp_ID
```
