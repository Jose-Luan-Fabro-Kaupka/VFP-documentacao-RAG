# Propriedade IncrementalSearch

Especifica se um controle suporta uma pesquisa incremental para navegação por teclado. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.IncrementalSearch[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade IncrementalSearch são: Configuração Descrição True (.T.) (Padrão) Suporta pesquisa incremental. False (.F.) Não suporta pesquisa incremental.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Um exemplo de pesquisa incremental é se você estiver procurando a palavra "ELASTIC," você pode digitar E-L-A, e assim por diante. Conforme você digita, o Visual FoxPro pesquisa incrementalmente a combinação de letras que você digitou para corresponder à palavra que você está procurando. Caso contrário, ele encontra a primeira palavra que começa com E, depois a primeira palavra que começa com L, e assim por diante.

Observe que a configuração da variável de sistema _INCSEEK determina quanto tempo aguardar a digitação da próxima letra. Você pode precisar ajustar o valor de _INCSEEK para fazer a pesquisa incremental funcionar corretamente.

Uma combo box com a propriedade Style definida como 0 (Dropdown Combo) mostrará pesquisa incremental apenas na caixa de texto se a lista suspensa for exibida. Com a propriedade Style definida como 2 (Dropdown List), a pesquisa incremental será exibida na caixa de texto, independentemente de a lista suspensa ser exibida ou não.
