# Propriedade Hours

Especifica se a porção de horas de um valor DateTime é exibida em formato de hora de 12 ou 24 horas. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Hours[ = nValue]
```

# Valor de retorno
 **nValue**
Uma das seguintes configurações: Configuração Descrição 0 (Padrão) A configuração SET HOURS determina se a porção de horas de um valor DateTime é exibida em formato de hora de 12 ou 24 horas. Se SET HOURS for 12, a porção de horas de um valor DateTime é exibida em formato de hora de 12 horas. Se SET HOURS for 24, a porção de horas de um valor DateTime é exibida em formato de hora de 24 horas. 12 A porção de horas do valor DateTime é exibida em formato de hora de 12 horas. 24 A porção de horas do valor DateTime é exibida em formato de hora de 24 horas.

# Observações

Aplica-se a: Controle TextBox (Visual FoxPro)

A configuração da propriedade Hours é ignorada se a propriedade DateFormat estiver definida como Short ou Long.
