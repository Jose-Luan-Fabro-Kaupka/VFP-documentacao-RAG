# Propriedade ClipControls

Determina se os métodos gráficos em eventos Paint repintam o objeto inteiro ou apenas áreas recém expostas. Também determina se o ambiente gráfico do sistema operacional cria uma região de recorte que exclui controles não gráficos contidos pelo objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ClipControls[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações para a propriedade ClipControls são: Configuração Descrição True (.T.) (Padrão) Métodos gráficos em eventos Paint repintam o objeto inteiro. Uma região de recorte é criada ao redor de controles não gráficos em um formulário antes de um evento Paint. False (.F.) Métodos gráficos em eventos Paint repintam apenas áreas recém expostas. Uma região de recorte não é criada ao redor de controles não gráficos.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN
