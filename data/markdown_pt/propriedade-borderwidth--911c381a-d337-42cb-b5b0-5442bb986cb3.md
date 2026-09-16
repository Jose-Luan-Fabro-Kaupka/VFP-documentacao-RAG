# Propriedade BorderWidth

Especifica a largura da borda de um controle. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.BorderWidth[ = nWidth]
```

# Valor de retorno
 **nWidth**
Especifica a largura, que pode variar de 0 a 8192. Observação Se a configuração BorderWidth for maior que 1, a configuração da propriedade BorderStyle é ignorada.

# Observações

Aplica-se a: Objeto Container | Objeto Control (Visual FoxPro) | Controle Line | Controle PageFrame | Controle Shape

Quando BorderWidth está definido como 0, o controle parece não ter borda. A configuração BorderWidth é ignorada para controles PageFrame quando a configuração Tabs é .T. (True).
