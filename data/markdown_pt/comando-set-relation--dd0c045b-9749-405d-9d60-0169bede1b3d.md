# Comando SET RELATION

Estabelece um relacionamento entre tabelas abertas de modo que mover o ponteiro de registro na tabela pai move o ponteiro de registro na tabela filha.

```foxpro
SET RELATION TO [eExpression1 INTO nWorkArea1 | cTableAlias1
   [, eExpression2 INTO nWorkArea2 | cTableAlias2 ...]
   [IN nWorkArea | cTableAlias] [ADDITIVE]]
```

#### Parâmetros
 **eExpression1**
Especifica a expressão relacional que cria um relacionamento entre as tabelas pai e filha. The relational expression is usually the index expression of the controlling index of the child table. If eExpression1 is numeric, it is evaluated when the record pointer in the parent table is moved. The record pointer in the child table is then moved to record number eExpression1 . Omitting arguments for SET RELATION removes all relationships in the currently selected work area. You can remove a specific parent-child relationship using SET RELATION OFF . For more information, see SET RELATION OFF Command .
**INTO nWorkArea1 | cTableAlias1**
Especifica o número da área de trabalho ou alias da tabela filha.
**eExpression2 INTO nWorkArea2 | cTableAlias2 ...**
Especifica uma expressão relacional e o número da área de trabalho ou um alias de tabela filha para que você possa criar um relacionamento adicional entre a tabela pai e tabelas filhas. Precede each relationship definition with a comma.
**IN nWorkArea**
Especifica a área de trabalho da tabela pai.
**IN cTableAlias**
Especifica o alias da tabela pai. The IN clause makes it possible for you to create a relationship without first selecting the parent table's work area. If you omit nWorkArea and cTableAlias , the parent table must be open in the currently selected work area.
**ADDITIVE**
Preserva todos os relacionamentos existentes na área de trabalho atual e cria o relacionamento especificado. Omitting ADDITIVE breaks any relationships in the current work area and creates the specified relationship.

# Observações

Antes de criar um relacionamento, as tabelas devem estar abertas em áreas de trabalho diferentes. A tabela filha deve estar indexada no campo comum, a menos que a expressão relacional seja numérica. The index for the child table can be a single-entry (.idx) index, a structural compound (.cdx) index, or an non-structural compound index. If the index is a compound index, specify the proper index tag to order the records in the child table using the SET ORDER command.

> **Observação:** If you call SET RELATION with a nonnumeric relational expression and the child table has not been ordered with an index, Visual FoxPro generates an error message.

Normalmente você pode criar relacionamentos entre tabelas que têm um campo comum. Você pode criar várias relações entre uma única tabela pai e várias tabelas filhas usando um único comando SET RELATION.

> **Observação:** Se um registro correspondente não for encontrado na tabela filha, o ponteiro de registro na tabela filha é posicionado no final da tabela.

If the child table has an active index, the data type of eExpression1 must be the same as the child table's active index key. If the child table does not have an active index, then eExpression1 must have a numeric data type, in which case it represents a record number to move to in the child table.

# Exemplos

Example 1

O exemplo a seguir cria um relacionamento entre uma tabela de clientes e uma tabela de pedidos em que um registro de cliente na tabela de clientes pode ter muitos registros de pedidos na tabela de pedidos. Ao criar um relacionamento usando um campo comum, você pode ver todos os pedidos de qualquer cliente. This example creates relationship using the Cust_ID field in the customer table and the Cust_ID index tag in the orders table. The index in the orders table organizes records by customer.

The following code uses the USE command to open the customer table as the parent table in work area 1 and open the orders table as the child table in work area 2. The SELECT command selects the work area for the orders table. The SET ORDER command specifies the order of the orders table using the Cust_ID index tag:

```foxpro
USE Customer IN 1
USE Orders IN 2
SELECT Orders
SET ORDER TO TAG Cust_ID
```

The following code uses the SELECT command to select the work area for the customer table. SET RELATION creates the relationship between the parent table and the controlling index in the child table:

```foxpro
SELECT Customer
SET RELATION TO Cust_ID INTO Orders
```

The following code opens the customer table in a browse window, selects the work area of the orders table and opens a browse window for the orders table:

```foxpro
BROWSE NOWAIT
SELECT Orders
BROWSE NOWAIT
```

Quando você move o ponteiro de registro na tabela de clientes, o ponteiro de registro na tabela de pedidos também se move. Opening the Data Session window displays the relationship created between the two tables.

Example 2

O exemplo a seguir cria um relacionamento dentro de uma única tabela, ou um relacionamento autorreferencial. By opening the same table with two different aliases in different work areas, you can create a relationship in the same table by using the two aliases. The following code selects the work area of the table with the SELECT command and opens the table with the Manager alias with the USE command. The SELECT command then selects the same work area and opens the table again with the Employee alias with the USE command and the AGAIN keyword. The tables open in two different work areas:

```foxpro
SELECT 0
USE Employees ALIAS Manager
SELECT 0
USE Employees AGAIN ALIAS Employee
```

The following code creates an index on the based on the Reports_To field with the index tag Mgr_ID for the table using the INDEX command and sets the order in the table to that index using the SET ORDER command. The index created organizes records by manager.

```foxpro
INDEX ON Reports_To TAG Mgr_ID
SET ORDER TO Mgr_ID
```

The following code selects the Manager alias as the parent using the SELECT command.

SET RELATION creates the relationship between the parent table and the controlling index tag in the child table. The controlling index in the child table organizes records by employee.

```foxpro
SELECT Manager
SET RELATION TO Emp_ID INTO Employee
```

The following code opens the table with the Manager alias in a browse window, selects the work area of the table with the Employee alias and opens a browse window for the table:`BROWSESELECT EmployeeBROWSE`

Quando você move o ponteiro de registro na tabela manager, o ponteiro de registro na tabela employee também se move e exibe somente os funcionários que reportam ao gerente selecionado.
