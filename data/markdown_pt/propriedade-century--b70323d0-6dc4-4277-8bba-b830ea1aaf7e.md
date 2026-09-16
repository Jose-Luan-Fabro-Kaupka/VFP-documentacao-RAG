# Propriedade Century

Especifica se a porção do século de uma data é exibida em uma caixa de texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Century[ = nValue]
```

# Valor de retorno
 **nValue**
Uma das seguintes configurações: Configuração Descrição 0 Desativado. A porção do século da data não é exibida. 1 (Padrão) Ativado. A porção do século da data é exibida. 2 A configuração SET CENTURY determina se a porção do século da data é exibida. Se SET CENTURY estiver ON, a porção do século da data é exibida. Se SET CENTURY estiver OFF, a porção do século da data não é exibida.

# Observações

Aplica-se a: TextBox Control (Visual FoxPro)

A configuração da propriedade Century é ignorada se a propriedade DateFormat estiver definida como Short ou Long.

Observe que em versões anteriores do Visual FoxPro o padrão da propriedade Century é 2.
