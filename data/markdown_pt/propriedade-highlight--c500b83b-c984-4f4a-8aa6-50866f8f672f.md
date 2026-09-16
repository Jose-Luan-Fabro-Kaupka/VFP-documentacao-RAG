# Propriedade Highlight

Especifica se a célula com o foco em um controle Grid aparece selecionada. Disponível em tempo de design e de leitura/gravação em tempo de execução.

```foxpro
Grid.Highlight [= lExpr ]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Highlight são: Configuração Descrição True (.T.) A célula é marcada (destacada) como selecionada. (Padrão) False (.F.) A célula não é selecionada.

# Observações

Aplica-se a: Controle Grid

Se a propriedade Highlight estiver definida como true (.T.), você pode usá-la em conjunto com a propriedade SelectOnEntry de uma Column para determinar se toda a célula aparece selecionada. Se você definir a propriedade Highlight como false (.F.), a propriedade SelectOnEntry é ignorada.
