# Propriedade Seconds

Especifica se a porção de segundos de um valor DateTime é exibida em uma caixa de texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Seconds[ = nValue]
```

# Valor de retorno
 **nValue**
Uma das configurações a seguir: Configuração Descrição 0 Desligado. A porção de segundos do valor DateTime não é exibida. 1 Ligado. A porção de segundos do valor DateTime é exibida. 2 (Padrão) A configuração SET SECONDS determina se a porção de segundos do valor DateTime é exibida. Se SET SECONDS estiver ON, a porção de segundos do valor DateTime é exibida. Se SET SECONDS estiver OFF, a porção de segundos do valor DateTime não é exibida.

# Observações

Aplica-se a: Controle TextBox (Visual FoxPro)

A configuração da propriedade Seconds é ignorada se a propriedade DateFormat estiver definida como Short ou Long.
