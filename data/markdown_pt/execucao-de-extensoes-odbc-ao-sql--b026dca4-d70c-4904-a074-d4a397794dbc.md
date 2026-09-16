# Execução de extensões ODBC ao SQL

Você pode usar a função SQLEXEC( ) para executar extensões ODBC ao SQL colocando a instrução SQL entre a sintaxe de escape padrão ou estendida do SQL Access Group. Para obter mais informações sobre extensões ODBC ao SQL, consulte o apêndice SQL Grammar na documentação ODBC.

# Criando junções externas usando a cláusula de escape ODBC

Você pode usar SQL pass-through para realizar junções externas em dados remotos usando a sintaxe de escape ODBC, se seu servidor suportar junções externas. Uma junção externa combina informações de uma ou mais tabelas independentemente de registros correspondentes serem encontrados.

A sintaxe para junções externas usando a cláusula de escape ODBC é:

```foxpro
{oj outer-join expression}
```

O exemplo a seguir cria um conjunto de resultados dos nomes e departamentos de funcionários trabalhando no projeto 544:

```foxpro
SELECT employee.name, dept.deptname;
   FROM {oj employee LEFT OUTER JOIN dept;
            ON employee.deptid = dept.deptid};
   WHERE employee.projid = 544
```

Para obter mais informações sobre sintaxe de junção externa e tipos de junções externas, consulte a documentação do servidor. Para obter informações sobre como criar uma conexão nomeada, consulte Como: definir conexões com fontes de dados remotas.
