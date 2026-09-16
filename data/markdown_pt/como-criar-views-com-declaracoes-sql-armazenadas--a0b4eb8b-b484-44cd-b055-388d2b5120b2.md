# Como: Criar Views com Declarações SQL Armazenadas

Você pode usar substituição de macro para armazenar a declaração SQL SELECT criada para uma view em uma variável que você usa com a cláusula AS no comando CREATE SQL VIEW.

### Para criar uma view usando substituição de macro
- Crie uma variável e armazene a declaração SQL SELECT na variável.
- Na cláusula AS do comando CREATE SQL VIEW, use o caractere de substituição de macro (&) seguido do nome da variável.

Por exemplo, o código a seguir armazena uma declaração SQL SELECT na variável MyEmpCustSQL. CREATE SQL VIEW cria uma view chamada EmpCustView usando a variável:

```foxpro
MyEmpCustSQL = "SELECT employee.emp_id, customer.cust_id, ;
   customer.emp_id, customer.contact, customer.company ;
   FROM employee, customer WHERE employee.emp_id = customer.emp_id"
CREATE SQL VIEW EmpCustView AS &MyEmpCustSQL
```
