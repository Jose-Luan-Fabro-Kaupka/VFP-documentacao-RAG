# Como: criar regras de validação de campo

Você pode criar regras de validação de campo para controlar o tipo de informação que um usuário pode inserir em campos de tabelas de banco de dados. Você também pode especificar uma mensagem personalizada para exibir para valores inválidos em vez da mensagem de erro padrão.

> **Observação:** Certifique-se de que as regras de validação de campo não conflitem semanticamente com regras de validação de registro. O Visual FoxPro não compara as expressões em nível de campo e em nível de registro para consistência.

### Para criar uma regra de validação de campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer .
- No Table Designer , selecione o campo desejado.
- Na caixa Rule da área Field validation, digite a expressão de validação desejada. Para construir uma expressão, clique no botão de reticências (...).
- Quando terminar, clique em OK .
- Para exibir uma mensagem de erro personalizada, na caixa Message, digite a mensagem de erro personalizada ou expressão que deseja exibir para valores inválidos. Para construir uma expressão, clique no botão de reticências (...). Observação Certifique-se de colocar o texto da mensagem entre aspas ("").
- Quando terminar, clique em OK .

Para obter mais informações, consulte Fields Tab, Table Designer.

### Para criar uma regra de validação de campo programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, inclua a cláusula CHECK. Para incluir texto de mensagem de erro personalizado, inclua a cláusula ERROR. -OU-
- Para editar uma tabela existente, abra a tabela com o comando USE e depois use o comando SQL ALTER TABLE com a cláusula CHECK ou SET CHECK. Para incluir texto de mensagem de erro personalizado, inclua a cláusula ERROR. -OU-
- Use a função DBSETPROP( ) para definir as propriedades RuleExpression e RuleText do campo.

Para obter mais informações, consulte CREATE TABLE - SQL Command, ALTER TABLE - SQL Command e DBSETPROP( ) Function.

Por exemplo, suponha que você deseja que o número de itens inseridos para um registro em uma tabela de itens de pedido seja igual ou maior que 1. O código a seguir adiciona uma regra de validação de campo exigindo que os números inseridos no campo Quantity sejam iguais ou maiores que 1 usando a cláusula SET CHECK. A cláusula ERROR especifica uma mensagem de erro personalizada:

```foxpro
ALTER TABLE OrdItems ALTER COLUMN Quantity SET CHECK Quantity >= 1 ;
   ERROR "Quantity must be a value greater than or equal to 1."
```

Quando o usuário tenta inserir um valor menor que 1, o Visual FoxPro exibe a mensagem de erro personalizada e rejeita o valor.
