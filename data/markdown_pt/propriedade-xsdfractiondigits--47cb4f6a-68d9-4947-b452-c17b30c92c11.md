# Propriedade XSDfractionDigits

Contém o valor fractionDigits da XML Schema Definition (XSD), que aparece à direita do ponto decimal.

> **Observação:** XSDfractionDigits é ignorado, a menos que XMLField XSDtype tenha um valor não vazio.

Os seguintes métodos XMLAdapter preenchem a propriedade XSDfractionDigits conforme apropriado:
 - LoadXML
- Attach
- AddTableSchema

```foxpro
XMLField.XSDfractionDigits
```

# Valor de retorno

Tipo de dados Character. XSDfractionDigits especifica os dígitos fracionários XSD.

# Observações

Aplica-se a: XMLField Class

Ao gerar XML usando o método ToXML do XMLAdapter, você pode definir esta propriedade para especificar a restrição fractionDigits no esquema XSD. Você pode precisar desse comportamento quando o valor fractionDigits exigido para o esquema difere do que o Visual FoxPro calcularia de outra forma. O Visual FoxPro não realiza validação nessa situação; portanto, você precisa garantir que os dados estejam em conformidade com as restrições impostas por fractionDigits.
