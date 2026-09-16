# Como: passar parâmetros para um formulário

Às vezes você deseja passar parâmetros para formulários ao executá-los para definir valores de propriedades ou especificar padrões operacionais.

### Para passar um parâmetro para um formulário criado no Form Designer
- Crie propriedades no formulário para armazenar os parâmetros, como ItemName e ItemQuantity.
- No código do evento Init do formulário, inclua uma instrução PARAMETERS como: PARAMETERS cString, nNumber
- No código do evento Init do formulário, atribua os parâmetros às propriedades, como neste exemplo: THIS.ItemName = cString THIS.ItemQuantity = nNumber
- Ao executar o formulário, inclua uma cláusula WITH no Comando DO FORM : DO FORM myform WITH "Bagel", 24
