# Amostra Interactively Build a SELECT Statement

Arquivo: ...\Samples\Solution\Forms\Makesql.scx

Esta amostra mostra como permitir que um usuário construa uma consulta personalizada em tempo de execução. Combo boxes no formulário permitem que um usuário escolha campos da tabela atualmente aberta. O método BldSQL processa os nomes dos campos e os valores que os usuários digitam nas text boxes para criar uma instrução SQL SELECT executável.

Métodos adicionais, ValidateType e SetTextboxFormat, garantem que os valores apropriados sejam inseridos nas text boxes e corretamente incorporados na instrução SELECT.

Depois que a cláusula WHERE foi construída e armazenada na variável lcWhere, o comando a seguir cria a instrução SELECT:

```foxpro
lcSQL = "SELECT * FROM " + lcAlias + " " + lcWHERE
```

Depois que a instrução SELECT é construída, ela pode ser executada com substituição de macro.

```foxpro
&lcSQL
```
