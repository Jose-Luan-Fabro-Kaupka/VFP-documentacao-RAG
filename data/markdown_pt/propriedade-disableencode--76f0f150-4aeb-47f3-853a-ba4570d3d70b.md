# Propriedade DisableEncode

Habilita ou desabilita a codificação base64 ou hexBinary para campos Memo ou Character.

Definir DisableEncode no nível do XMLAdapter define os valores padrão de DisableEncode para objetos XMLField quando eles são criados e adicionados à coleção Fields pelos seguintes métodos do XMLAdapter:
 - Método LoadXML
- Método Attach (Visual FoxPro)
- Método AddTableSchema

Além disso, alterar DisableEncode no nível do XMLAdapter afeta apenas o próximo conjunto de objetos XMLField criados, não os objetos XMLField existentes na coleção Fields. Portanto, para modificar a configuração de DisableEncode para um objeto XMLField existente, altere o valor no nível do XMLField.

> **Observação:** DisableEncode se aplica a objetos XMLField somente se IsBinary estiver definido como True (.T.). Para obter mais informações, consulte Propriedade IsBinary .

```foxpro
Object.DisableEncode [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) Desabilita a codificação base64 ou hexBinary para campos Memo ou Character. (Padrão) True (.T.) Habilita a codificação base64 ou hexBinary para campos Memo ou Character.

# Observações

Aplica-se a: Classe XMLAdapter | Classe XMLField

O Visual FoxPro ignora caracteres inválidos ou comprimento incorreto em cadeias de caracteres codificadas em base64 e hexBinary.

Se DisableEncode do XMLAdapter for True (.T.) quando o método LoadXML for executado, a propriedade MaxLength do XMLField é definida como o comprimento máximo para os dados codificados. Caso contrário, o Visual FoxPro usa o valor original de MaxLength.

Se DisableEncode do XMLAdapter for True (.T.) quando o método ToXML for executado, o valor xsd:maxLength no esquema da Definição de Esquema XML (XSD) é definido como o comprimento máximo para os dados decodificados. Caso contrário, o Visual FoxPro usa o valor da propriedade MaxLength do XMLField.
