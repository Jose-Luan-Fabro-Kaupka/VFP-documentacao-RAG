# Comando SET INTENSITY

Incluído para compatibilidade com versões anteriores. Use o Comando SET COLOR OF SCHEME em vez disso.

Determina se o FoxPro usa o atributo de cor de tela aprimorado para a exibição de campos de edição.

```foxpro
SET INTENSITY ON | OFF
```

# Observações

SET INTENSITY está incluído para compatibilidade com versões anteriores. Use SET COLOR OF SCHEME em vez disso.

No FoxPro para MS-DOS, SET INTENSITY especifica se o atributo de tela aprimorado é usado para campos exibidos com @ ... GET, APPEND, BROWSE, CHANGE ou EDIT.

No FoxPro para Windows, SET INTENSITY especifica se uma configuração de cor do Windows é usada para regiões de edição criadas com @ ... GET.

No FoxPro para Macintosh, SET INTENSITY é ignorado.

ON

 No FoxPro para MS-DOS, o atributo de tela aprimorado é usado para destacar campos se SET INTENSITY estiver ON.

 No FoxPro para Windows e FoxPro para Macintosh, a cor de fundo de uma região de edição criada com @ ... GET é determinada pela configuração de cor do Windows para faces de botões quando INTENSITY está ON. Essa cor pode ser alterada escolhendo o ícone Colors no Painel de Controle do Windows.

 ON é a configuração padrão.

OFF

 O atributo de tela normal é usado se SET INTENSITY estiver OFF.
