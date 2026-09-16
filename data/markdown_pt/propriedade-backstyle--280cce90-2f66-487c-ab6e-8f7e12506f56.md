# Propriedade BackStyle

Especifica se o plano de fundo de um objeto é transparente ou opaco. Disponível em tempo de projeto e execução.

```foxpro
Object.BackStyle[ = nStyle]
```

# Valor de retorno
 **nStyle**
Configurações: 0 Transparente. Tudo atrás do objeto fica visível. 1 (Padrão) Opaco. BackColor preenche o controle e oculta cores ou elementos gráficos atrás dele.

# Observações

Aplica-se a: controle CheckBox | controle CommandGroup | objeto Container | objeto Control | controle EditBox | controle Image | controle Label | controle OptionButton | controle OptionGroup | objeto Page | controle Shape | controle TextBox

Use BackStyle para criar controles transparentes sobre uma cor de fundo de um objeto Form ou sobre um elemento gráfico. Use um controle opaco para destacá-lo em um fundo carregado.

BackColor é ignorada quando BackStyle é 0 (Transparente).

Para um objeto Page, BackStyle é somente leitura quando Tabs é True (.T.) no PageFrame que contém Page.

BackStyle é ignorada quando Theme do objeto é True (.T.).
