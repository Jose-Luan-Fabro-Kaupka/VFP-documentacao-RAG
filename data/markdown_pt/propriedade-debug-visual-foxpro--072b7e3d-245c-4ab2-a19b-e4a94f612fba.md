# Propriedade Debug (Visual FoxPro)

Especifica se informações de depuração são incluídas com o código-fonte compilado de um projeto.

```foxpro
Object.Debug[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade Debug são: Configuração Descrição True (.T.) (Padrão) As informações de depuração são incluídas com o código-fonte compilado. False (.F.) As informações de depuração não são incluídas, e você não pode visualizar a execução de um programa na janela Trace nem usar MESSAGE(1) para retornar o código-fonte de uma linha que causa um erro. Definir lExpression como false (.F.) é idêntico a incluir o argumento NODEBUG no comando COMPILE.

# Observações

Aplica-se a: Objeto Project (Visual FoxPro)

O código-fonte de um projeto inclui arquivos de programa e formato, código-fonte em bibliotecas de formulários, etiquetas, relatórios e classes visuais e procedimentos armazenados em bancos de dados. A propriedade Debug corresponde à caixa de seleção Debug info na guia Project da caixa de diálogo Project Information.
