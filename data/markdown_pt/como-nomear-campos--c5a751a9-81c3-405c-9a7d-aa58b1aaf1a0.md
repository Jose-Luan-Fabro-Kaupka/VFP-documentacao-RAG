# Como: nomear campos

Você especifica nomes para campos ao construir uma tabela. Para tabelas livres, os nomes de campo podem ter até 10 caracteres. Para tabelas de banco de dados, os nomes de campo podem ter até 128 caracteres.

> **Observação:** Se você remover uma tabela de um banco de dados, os nomes longos de campo em uma tabela são truncados para 10 caracteres. Para obter mais informações, consulte Criação de campos .

### Para nomear um campo de tabela
- Abra a tabela no Table Designer .
- Clique na guia Fields.
- Na caixa Name, digite um nome para o campo.

Para obter mais informações, consulte Como: abrir tabelas (Visual FoxPro) e Guia Fields, Table Designer.

### Para nomear um campo de tabela programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, especifique o nome do campo. -OU-
- Para editar uma tabela existente, abra a tabela com o comando USE e depois use o comando SQL ALTER TABLE.

Para obter mais informações, consulte Comando CREATE TABLE - SQL ou Comando ALTER TABLE - SQL.

Por exemplo, o código a seguir cria e abre uma tabela chamada Customer com três campos, Cust_ID, Company e Contact usando o comando CREATE TABLE:

```foxpro
CREATE TABLE Customer (Cust_ID C(6), Company C(40), Contact C(30))
```

No exemplo, `C(6)` indica que o campo contém dados Character e tem largura de campo de 6 caracteres. Para obter mais informações, consulte Como: escolher tipos de dados.

O código a seguir adiciona campos a uma tabela existente usando o comando SQL ALTER TABLE:

```foxpro
ALTER TABLE Customer ;
   ADD COLUMN (Company C(40), Contact C(30))
```

# Renomeando campos

Você pode renomear campos de tabela existentes.

### Para renomear um campo de tabela
- Abra a tabela no Table Designer .
- Na caixa Name na guia Fields, insira o cursor no campo desejado e digite o novo nome do campo.

Para obter mais informações, consulte Guia Fields, Table Designer.

### Para renomear um campo de tabela programaticamente
- Use o comando SQL ALTER TABLE com a cláusula RENAME COLUMN.

Para obter mais informações, consulte Comando ALTER TABLE - SQL.

Por exemplo, o código a seguir renomeia o campo Company na tabela Customer usando o comando SQL ALTER TABLE:

```foxpro
ALTER TABLE Customer RENAME COLUMN Company TO Company_LongName
```
