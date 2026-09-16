# Propriedade Encrypted

Especifica se o código-fonte compilado em um projeto está criptografado.

```foxpro
Object.Encrypted[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade Encrypted são: Configuração Descrição True (.T.) O código-fonte compilado está criptografado. Definir lExpression como true (.T.) fornece proteção adicional para seu código-fonte e é idêntico a incluir o argumento ENCRYPT no comando COMPILE. False (.F.) (Padrão) O código-fonte compilado não está criptografado.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

O código-fonte em um projeto inclui arquivos de programa e de formato, código-fonte em bibliotecas de formulários, etiquetas, relatórios e classes visuais, e procedimentos armazenados em bancos de dados. A propriedade Encrypted corresponde à caixa de seleção Encrypted na guia Project da caixa de diálogo Project Information Dialog Box.
