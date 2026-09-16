# Propriedade XSDtotalDigits

Contém o valor XSD totalDigits da Definição de Esquema XML (XSD), que determina a precisão numérica.

> **Observação:** XSDtotalDigits é ignorado, a menos que a propriedade XSDtype do XMLField tenha um valor não vazio.

Os seguintes métodos do XMLAdapter preenchem a propriedade XSDtotalDigits conforme apropriado:
 - LoadXML
- Attach
- AddTableSchema

```foxpro
XMLField.XSDtotalDigits
```

# Valor de retorno

Tipo de dados Character. XSDtotalDigits especifica o número total de dígitos XSD.

# Observações

Aplica-se a: Classe XMLField

Ao gerar XML usando o método ToXML do XMLAdapter, você pode definir esta propriedade para especificar a restrição totalDigits no esquema XSD. Você pode precisar desse comportamento quando o valor totalDigits necessário para o esquema difere do que o Visual FoxPro calcularia de outra forma. O Visual FoxPro não realiza validação nessa situação; portanto, você precisa garantir que os dados estejam em conformidade com as restrições impostas por totalDigits.
