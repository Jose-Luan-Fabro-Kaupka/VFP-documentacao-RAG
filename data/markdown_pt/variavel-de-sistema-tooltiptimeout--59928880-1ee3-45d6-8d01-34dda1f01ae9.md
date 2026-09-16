# Variável de sistema _TOOLTIPTIMEOUT

Especifica por quanto tempo uma dica de ferramenta é exibida se o ponteiro do mouse permanecer parado.

```foxpro
_TOOLTIPTIMEOUT = [nValue]
```

#### Parâmetros
 **nValue**
As configurações para nValue são: Configuração Descrição -1 (Padrão) Exibe a dica de ferramenta pelo tempo especificado pelo Windows. 0 Exibe a dica de ferramenta até que o mouse seja movido. > 0 Quantidade de tempo em milissegundos para exibir a dica de ferramenta. Omita o parâmetro nValue para determinar o valor atual de _TOOLTIPTIMEOUT.

# Observações

A configuração de _TOOLTIPTIMEOUT se aplica apenas a controles que têm a propriedade ToolTipText definida e a campos em janelas Browse que são dimensionados menores que seu conteúdo.
