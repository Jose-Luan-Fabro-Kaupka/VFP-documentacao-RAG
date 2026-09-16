# Propriedade Themes

Especifica se os Temas do Windows XP estão habilitados ou desabilitados para um controle. Para formulários e toolbars, Themes controla se os objetos filhos usam temas. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** A propriedade Themes para classes visuais pode afetar sua interface de usuário existente ao usar o Microsoft Windows XP. Você pode desativar esse suporte definindo a propriedade Themes no nível do controle, do formulário ou da variável de sistema _SCREEN.

```foxpro
Object.Themes [ = lExpr ]
```

#### Parâmetros
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista as configurações para lExpr . lExpr True (.T.) Habilitado (Padrão) False (.F.) Desabilitado

# Observações

Aplica-se a: Variável de sistema _SCREEN | Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle ListBox | Controle OptionButton | Controle OptionGroup | Controle PageFrame | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

Controles definidos com @...GET ou @...SAY e comandos @... semelhantes não são compatíveis com Temas do Windows XP. Portanto, ao executar programas escritos com FoxPro 2.x no Windows XP ou posterior, você deve definir a propriedade _SCREEN.Themes como False (.F.); caso contrário, os controles nos formulários desaparecem. O exemplo a seguir ilustra o código que você pode usar para evitar que os controles nos formulários desapareçam:

```foxpro
_SCREEN.Themes = .T.
DEFINE WINDOW ThemesDemo AT 0.000, 0.000;
   SIZE 29.000,121.200;
   TITLE "ThemesDemo";
   FONT "MS Sans Serif", 8;
   float;
   CLOSE;
   NOMINIMIZE;
   SYSTEM;
   COLOR RGB(,,,192,192,192)
ACTIVATE WINDOW ThemesDemo
@ 2.500,55.833 GET DemoDB;
   PICTURE "@*C Demo CheckBox";
   SIZE 1.308,21.400;
   DEFAULT 0;
   FONT "Microsoft Sans Serif", 8;
   STYLE "T"
   _SCREEN.activeform.lockscreen = .T.
   _SCREEN.activeform.lockscreen = .F.
READ CYCLE
```

Você pode definir a propriedade _SCREEN.Themes como False (.F.) para desabilitar Temas inteiramente no Visual FoxPro.

> **Observação:** Quando você define a propriedade _SCREEN.Themes, você não altera de fato o estado atual de Temas definido no nível do sistema operacional. Use SYS(2700) - Enables Windows XP Themes para verificar o estado atual de Temas.

Quando Themes está habilitado, o Visual FoxPro substitui a propriedade SpecialEffect e usa o tema padrão, exceto quando SpecialEffect está definido com o valor 2 (hot tracking). Nesse cenário, o Visual FoxPro preserva o hot tracking, que exibe efeitos especiais quando você move o mouse sobre os controles CommandButton, OptionButton e CheckBox gráficos.

Para controles CheckBox, Themes suporta caixas de seleção de três estados.

Para objetos Form e ToolBar, Themes habilita temas para o formulário inteiro. Para habilitar temas para um controle, você precisa definir Themes como True (.T.) tanto para o formulário quanto para o controle. Para outros controles contêiner, como PageFrame, Themes não controla como os objetos filhos exibem temas; controla apenas aspectos visuais, como bordas ou guias.

> **Observação:** Quando Temas estão habilitados, você deve evitar usar o comando CLEAR para formulários, pois isso pode causar problemas de pintura com controles com tema, como botões de comando, que possuem efeitos ao passar o mouse.

Para controles OptionGroup, CommandGroup e Image, Themes determina se as bordas usam temas.

Controles como guias de PageFrame e cabeçalhos de Grid são desenhados dinamicamente pelo gerenciador de Temas do sistema operacional quando você move o mouse sobre eles. Portanto, não posicione outros controles sobre esses controles.

Para um controle Grid, Themes afeta a aparência visual dos cabeçalhos de coluna. Se temas estão habilitados para uma grade, as propriedades BackColor e ForeColor do cabeçalho são ignoradas porque herdam os atributos do tema. No entanto, as propriedades BackColor e ForeColor de um objeto Column são exibidas independentemente da configuração da propriedade Themes da grade.

Para controles PageFrame, Themes determina se as guias usam temas. Você pode precisar fazer pequenas modificações em formulários que contêm objetos PageFrame. A propriedade Themes fornece um efeito de gradiente nos objetos Page, de modo que um label, botão de opção ou controle semelhante com texto não aparece corretamente se a propriedade BackStyle do controle estiver definida como Opaque. Você pode corrigir essa situação definindo BackStyle como Transparent.

Se seu sistema operacional não suporta temas, ou se Themes está desativado, o Visual FoxPro usa as configurações controladas por SpecialEffect e outras propriedades.

Para detalhes mais específicos sobre Temas do Windows XP, consulte os seguintes recursos:
 - "Using Windows XP Visual Styles" em http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwxp/html/xptheming.asp .
- "Visual Styles" em http://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/CommCtls/Userex/themes.asp .
- "Microsoft Windows XP: What's in It for Developers?" em http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwxp/html/winxpintro.asp .
