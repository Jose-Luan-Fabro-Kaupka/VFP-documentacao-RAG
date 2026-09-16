# Comando SET CPDIALOG

Especifica se a caixa de diálogo Code Page é exibida quando uma tabela é aberta.

```foxpro
SET CPDIALOG ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Exibe a caixa de diálogo Code Page quando você abre uma tabela e as seguintes condições são verdadeiras: A tabela é aberta exclusivamente. A tabela não está marcada com uma página de código.
**OFF**
Não exibe a caixa de diálogo Code Page quando uma tabela é aberta.

# Observações

A caixa de diálogo Code Page permite especificar uma página de código para tabelas criadas em versões anteriores do FoxPro e em outros produtos que criam tabelas Visual FoxPro. A tabela é marcada com a página de código que você escolher.

Ao criar um aplicativo, emita SET CPDIALOG ON para garantir que as tabelas incluídas em seu aplicativo estejam marcadas com a página de código apropriada. Em seu aplicativo concluído, certifique-se de que SET CPDIALOG esteja OFF.

Você também pode especificar interativamente se a caixa de diálogo Code Page é exibida com a caixa de seleção Prompt for Code Page na guia Data da caixa de diálogo Options. A caixa de diálogo Options é exibida ao escolher Options no menu Tools.

> **Observação:** Para informações adicionais sobre páginas de código e suporte internacional do Visual FoxPro, consulte Code Pages Supported by Visual FoxPro in Developing International Applications.
