# Propriedade XSDmaxLength

Contém o valor XSD maxLength da XML Schema Definition (XSD).

> **Observação:** XSDmaxLength é ignorado, a menos que XMLField XSDtype seja um valor não vazio.

Os seguintes métodos XMLAdapter preenchem a propriedade XSDmaxLength conforme apropriado:
 - LoadXML
- Attach
- AddTableSchema

```foxpro
XMLField.XSDmaxLength
```

# Valor de retorno

Tipo de dados Character. XSDmaxLength especifica o número máximo de unidades de comprimento XSD.

# Observações

Aplica-se a: Classe XMLField

Ao gerar XML usando o método ToXML do XMLAdapter, você pode definir esta propriedade para especificar a restrição maxLength no esquema XSD. Você pode precisar desse comportamento quando o valor maxLength necessário para o esquema difere do que o Visual FoxPro calcularia de outra forma. O Visual FoxPro não realiza validação nesta situação; portanto, você precisa garantir que os dados estejam em conformidade com as restrições impostas por maxLength.
