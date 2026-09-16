# Propriedade TabOrientation

Especifica onde as guias são exibidas em um controle PageFrame. Leitura/gravação em tempo de design e execução.

```foxpro
PageFrame.TabOrientation [ = nValue ]
```

#### Parâmetros
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores possíveis para nValue . nValue Setting 0 Top (default) 1 Bottom 2 Left 3 Right

# Observações

Aplica-se a: PageFrame Control

Você geralmente pode especificar teclas de atalho em captions de Page incluindo os caracteres "\<". Embora o Visual FoxPro ofereça suporte funcional a teclas de atalho quando TabOrientation está definido para posições esquerda ou direita, as teclas de atalho não são exibidas visualmente.

Para objetos Page, definir a propriedade TabOrientation não tem efeito a menos que a fonte do caption da página seja uma fonte TrueType ou OpenType. Para obter mais informações, consulte Caption Property (Visual FoxPro) e FontName Property.
