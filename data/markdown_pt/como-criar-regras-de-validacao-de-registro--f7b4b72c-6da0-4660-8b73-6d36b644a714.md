# Como: criar regras de validação de registro

Você usa regras de validação em nível de registro quando deseja controlar o tipo de informação que um usuário pode inserir em um registro de tabela de banco de dados. Você também pode especificar uma mensagem personalizada para exibir em valores inválidos em vez da mensagem de erro padrão.

> **Observação:** Certifique-se de que as regras de validação de campo não entrem em conflito semanticamente com as regras de validação de registro. O Visual FoxPro não compara as expressões em nível de campo e em nível de registro quanto à consistência.

### Para criar uma regra de validação de registro
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer.
- No Table Designer, clique na guia Table.
- Na caixa Rule da área Record validation, digite a expressão de validação desejada. Para construir uma expressão, clique no botão de reticências (...).
- Quando terminar, clique em OK.
- Para exibir uma mensagem de erro personalizada, na caixa Message, digite a mensagem ou expressão de erro personalizada que deseja exibir para valores inválidos. Para construir uma expressão, clique no botão de reticências (...). Observação Certifique-se de colocar o texto da mensagem entre aspas ("").
- Quando terminar, clique em OK.

Para obter mais informações, consulte Table Tab, Table Designer.

### Para criar uma regra de validação de registro programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, inclua a cláusula CHECK. Para incluir texto de mensagem de erro personalizado, inclua a cláusula ERROR. -OU-
- Para editar uma tabela existente, abra a tabela com o comando USE e use o comando SQL ALTER TABLE com a cláusula CHECK ou SET CHECK. Para incluir texto de mensagem de erro personalizado, inclua a cláusula ERROR.

Para obter mais informações, consulte CREATE TABLE - SQL Command e ALTER TABLE - SQL Command.

> **Observação:** Você não pode usar a função DBSETPROP( ) para definir regras de validação de registro e texto de erro; no entanto, pode recuperá-las usando a função DBGETPROP( ) e as propriedades de tabela RuleExpression e RuleText. Para obter mais informações, consulte DBSETPROP( ) Function.

Por exemplo, suponha que você queira garantir que novos funcionários em uma tabela de funcionários tenham 18 anos ou mais. O código a seguir adiciona uma regra de validação de registro exigindo que a data de contratação na coluna Hire_Date seja igual ou posterior à data de nascimento mais 18 anos usando a cláusula SET CHECK. A cláusula ERROR especifica uma mensagem de erro personalizada:

```foxpro
ALTER TABLE Employee SET CHECK Hire_Date >= birth_date + (18 * 365.25) ;
   ERROR "Employees must be 18 years or older by date of hire."
```

Se o usuário inserir um registro de funcionário com data inválida, o Visual FoxPro exibe a mensagem de erro personalizada definida e não atualiza o registro.
