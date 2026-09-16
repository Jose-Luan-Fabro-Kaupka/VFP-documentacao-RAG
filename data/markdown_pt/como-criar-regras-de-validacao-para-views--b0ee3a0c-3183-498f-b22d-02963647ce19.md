# Como: criar regras de validação para views

Você pode criar versões locais de regras de validação de campo e de registro para views. A criação de regras de validação locais oferece os seguintes benefícios:
 - Reduz o tempo de resposta.
- Reduz o impacto nos recursos de rede.
- Testa os dados antes de enviá-los à fonte de dados remota.
- Impede o envio de dados incorretos à fonte de dados remota.

No entanto, o Visual FoxPro não compara as regras de validação que você cria localmente com as regras de validação na fonte de dados remota. Portanto, você deve criar regras apropriadas e compatíveis com a fonte de dados remota. Se as regras da fonte de dados remota mudarem, as regras de validação locais devem corresponder.

Para obter mais informações, consulte Working with Validation Rules.

### Para criar uma regra de validação de campo ou de registro para views
- Abra a view no View Designer e clique na guia Fields.
- Na lista Selected Fields, clique em um campo e clique em Properties.
- Na caixa Rule da área Field validation, digite a expressão de validação desejada. Para construir uma expressão, clique no botão de reticências (...).
- Para exibir uma mensagem de erro personalizada, na caixa Message, digite a mensagem de erro personalizada ou a expressão que deseja exibir para valores inválidos. Para construir uma expressão, clique no botão de reticências (...). Observação Certifique-se de colocar o texto da mensagem entre aspas ("").

### Para criar uma regra de validação de campo ou de registro para views programaticamente
- Use a função DBSETPROP( ) para definir as propriedades RuleExpression e RuleText de campo ou de registro para views.

Para obter mais informações, consulte a função DBSETPROP( ).

Por exemplo, o código a seguir cria uma regra em nível de campo em `orditems_view` que impede a entrada de uma quantidade menor que 1:

```foxpro
OPEN DATABASE testdata
USE VIEW orditems_view
DBSETPROP('Orditems_view.quantity','Field', ;
         'RuleExpression', 'quantity >= 1')
DBSETPROP('Orditems_view.quantity','Field', ;
         'RuleText', ;
'"Quantities must be greater than or equal to 1"')
```
