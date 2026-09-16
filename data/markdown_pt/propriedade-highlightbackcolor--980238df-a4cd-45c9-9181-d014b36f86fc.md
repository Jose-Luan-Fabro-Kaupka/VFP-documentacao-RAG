# Propriedade HighlightBackColor

Especifica a cor de fundo de uma linha do Grid quando ela é selecionada. A propriedade HighlightBackColor de um grid se aplica apenas quando a propriedade HighlightStyle do grid está definida com um valor maior que 0. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Grid.HighlightBackColor [= nColor ]
```

#### Parâmetros
 **nColor**
Tipo de dados Numeric. HighlightBackColor especifica um inteiro que representa um único valor de cor. O Visual FoxPro deriva a configuração de cor padrão da configuração de cor do sistema operacional Windows para Itens selecionados. Para obter mais informações sobre valores de cor válidos, consulte Propriedades BackColor, ForeColor.

# Observações

Aplica-se a: Controle Grid | Comando BROWSE

Se HighlightStyle contém um valor maior que 0, o Visual FoxPro exibe HighlightBackColor por padrão como um preenchimento gradiente 50% mais claro. Se você substituir a configuração HighlightBackColor, o Visual FoxPro não aplica nenhum efeito de gradiente.

Para obter mais informações, consulte Propriedade HighlightForeColor.
