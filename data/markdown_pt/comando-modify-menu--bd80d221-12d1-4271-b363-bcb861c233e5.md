# Comando MODIFY MENU

Abre o Menu designer para que você possa modificar ou criar um sistema de menu.

```foxpro
MODIFY MENU [FileName | ?] [[WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN]] [NOWAIT] [SAVE]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo do menu. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .mnx.
**?**
Exibe a caixa de diálogo Open, na qual você pode escolher um arquivo de menu existente ou inserir o nome de um novo menu a ser criado.
**WINDOW WindowName1**
Especifica uma janela cujas características o Menu Designer assume. Por exemplo, se a janela foi criada com a opção FLOAT de DEFINE WINDOW, o Menu Designer pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual o Menu Designer é aberto. O Menu Designer não assume as características da janela pai e não pode ser movido para fora da janela pai. Se a janela pai for movida, o Menu Designer se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar o Menu Designer.
**IN SCREEN**
Abre explicitamente o Menu Designer na janela principal do Microsoft Visual FoxPro, depois de ter sido colocado em uma janela pai. O Menu Designer é colocado em uma janela pai pela inclusão da cláusula IN WINDOW.
**NOWAIT**
Continua a execução do programa após o Menu Designer ser aberto. O programa não aguarda o Menu Designer ser fechado, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY MENU NOWAIT. Se você omitir NOWAIT quando MODIFY MENU é emitido em um programa, o Menu Designer é aberto e a execução do programa pausa até o Menu Designer ser fechado. NOWAIT é efetivo apenas dentro de um programa. Não tem efeito em MODIFY MENU quando emitido da janela Command. Se você emitir MODIFY MENU da janela Command sem um nome de menu e incluir NOWAIT, a caixa de diálogo Open não é exibida. A caixa de diálogo New Menu permite especificar o tipo de menu (padrão ou atalho) criado.
**SAVE**
Mantém o Menu Designer aberto após outra janela ser ativada. Se você omitir SAVE, o Menu Designer é fechado quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido da janela Command.

# Observações

Para obter mais informações sobre a criação de menus, consulte Menu System Creation.
