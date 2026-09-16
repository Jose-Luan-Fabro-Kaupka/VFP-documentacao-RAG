# Comando SET SYSMENU

Habilita ou desabilita a barra de menus do sistema do Visual FoxPro durante a execução do programa e permite reconfigurá-la.

```foxpro
SET SYSMENU ON | OFF | AUTOMATIC | TO [MenuList] | TO [MenuTitleList]
   | TO [DEFAULT] | TO LTRJUSTIFY | TO RTLJUSTIFY | SAVE | NOSAVE
```

#### Parâmetros
 **ON**
Habilita a barra de menus principal do Visual FoxPro durante a execução do programa quando o Visual FoxPro está aguardando entrada do teclado durante comandos como BROWSE, READ e MODIFY COMMAND.
**OFF**
Desabilita a barra de menus principal do Visual FoxPro durante a execução do programa. O parâmetro OFF deve ser executado a partir de um programa (.prg) para ter efeito. Por exemplo, o código a seguir, quando executado a partir de um programa, desabilitará a barra de menus principal do Visual FoxPro. SET SYSMENU OFF WAIT
**AUTOMATIC**
Torna a barra de menus principal do Visual FoxPro visível durante a execução do programa. A barra de menus é acessível e os itens de menu são habilitados e desabilitados conforme apropriado para o comando atual. AUTOMATIC é a configuração padrão.
**TO [ MenuList ] | TO [ MenuTitleList ]**
Especifica um subconjunto de menus ou títulos de menu para a barra de menus principal do Visual FoxPro. A lista de menus ou títulos de menu pode conter qualquer combinação de menus ou títulos de menu separados por vírgulas. Os nomes internos dos menus e títulos de menu estão listados no tópico System Menu Names. Por exemplo, o comando a seguir remove todos os menus da barra de menus principal do Visual FoxPro, exceto os menus File e Window: SET SYSMENU TO _MFILE, _MWINDOW Use RELEASE BAR para especificar os itens de menu disponíveis nos menus.
**TO [DEFAULT]**
Restaura a barra de menus principal à sua configuração padrão. Se você modificou a barra de menus principal ou seus menus, emita SET SYSMENU TO DEFAULT para restaurá-la. Você pode especificar uma configuração padrão com SET SYSMENU SAVE.
**TO LTRJUSTIFY | TO RTLJUSTIFY**
Inclua a cláusula TO LTRJUSTIFY para ordenar os comandos de menu da esquerda para a direita. Inclua a cláusula TO RTLJUSTIFY para ordenar os comandos de menu da direita para a esquerda. Essas opções estão disponíveis apenas quando o Windows está configurado para uma localidade do Oriente Médio. Observação Você pode incluir a opção RTLJUSTIFY no comando DEFINE POPUP para criar um sistema de menu com justificação da direita para a esquerda.
**SAVE**
Torna o sistema de menu atual a configuração padrão. Se você modificar o sistema de menu depois de emitir SET SYSMENU SAVE, pode restaurar a configuração anterior emitindo SET SYSMENU TO DEFAULT.
**NOSAVE**
Redefine o sistema de menu para o menu do sistema padrão do Visual FoxPro. No entanto, o menu do sistema padrão do Visual FoxPro não é exibido até que você emita SET SYSMENU TO DEFAULT.

# Observações

SET SYSMENU controla a barra de menus principal do Visual FoxPro durante a execução do programa e permite remover seletivamente títulos e menus de e restaurá-los ao sistema de menus principal do Visual FoxPro.

Emitir SET SYSMENU TO sem argumentos adicionais desabilita a barra de menus principal do Visual FoxPro.
