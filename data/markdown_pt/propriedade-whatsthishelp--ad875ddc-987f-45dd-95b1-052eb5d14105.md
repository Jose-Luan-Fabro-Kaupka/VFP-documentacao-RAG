# Propriedade WhatsThisHelp

Especifica se a Ajuda sensível ao contexto usa a Ajuda What's This ou o arquivo de ajuda do Windows especificado com SET HELP.

```foxpro
Form.WhatsThisHelp[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: Configuração Descrição True (.T.) O formulário usa uma das três técnicas de Ajuda What's This para abrir o arquivo de ajuda do Windows especificado com SET HELP e exibir o tópico especificado com a propriedade WhatsThisHelpID. False (.F.) (Padrão) O formulário usa a tecla F1 para abrir o arquivo de ajuda do Windows especificado com SET HELP. O tópico de Ajuda especificado com a propriedade HelpContextID é exibido.

# Observações

Aplica-se a: Objeto Form

As três técnicas de Ajuda What's This são as seguintes:
 - Um botão What's This é exibido na barra de título do formulário. Quando este botão é clicado, o ponteiro do mouse muda para uma seta com ponto de interrogação. O tópico de Ajuda exibido quando um controle é clicado é especificado com a propriedade WhatsThisHelpID do controle.
- O método WhatsThisMode é invocado, alterando o ponteiro do mouse para uma seta com ponto de interrogação. O tópico de Ajuda exibido quando um controle é clicado é especificado com a propriedade WhatsThisHelpID do controle.
- O método ShowWhatsThis é invocado para um controle. O tópico de Ajuda exibido é especificado com a propriedade WhatsThisHelpID do controle.

Se Help estiver definido para um arquivo HTML Help, por exemplo, HelpFileName.chm, o tópico de Ajuda é exibido no visualizador HTML Help. Se Help estiver definido para um arquivo Windows Help, por exemplo, HelpFileName.hlp, o tópico de Ajuda é exibido em uma pequena janela popup ao lado do controle.
