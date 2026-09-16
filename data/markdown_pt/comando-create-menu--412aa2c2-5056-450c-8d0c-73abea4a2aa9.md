# Comando CREATE MENU

Abre o Menu Designer no Visual FoxPro.

```foxpro
CREATE MENU [FileName | ?] [NOWAIT] [SAVE] [WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo para a tabela de menu. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .mnx.
**?**
Exibe a caixa de diálogo Create que solicita que você nomeie o menu sendo criado.
**NOWAIT**
Continua a execução do programa após o Menu Designer ser aberto. O programa não aguarda o fechamento do Menu Designer, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE MENU NOWAIT. Se você omitir NOWAIT, quando CREATE MENU é emitido em um programa, o Menu Designer é aberto e a execução do programa pausa até que o Menu Designer seja fechado. Se você emitir CREATE MENU na janela Command e incluir NOWAIT, a caixa de diálogo New Menu não é exibida. A caixa de diálogo New Menu permite especificar o tipo de menu (padrão ou de atalho) criado.
**SAVE**
Mantém o Menu Designer aberto após outra janela ser ativada. Se você omitir SAVE, o Menu Designer é fechado quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido na janela Command.
**WINDOW WindowName1**
Especifica uma janela cujas características o Menu Designer assume. Por exemplo, se a janela foi criada com a opção FLOAT de DEFINE WINDOW, o Menu Designer pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida. O Menu Designer tem um tamanho padrão que pode ser maior que a janela da qual assume as características. Nesse caso, o Menu Designer ainda assume as características da janela em que é colocado. O canto superior esquerdo do Menu Designer é colocado nas mesmas coordenadas do canto superior esquerdo da janela e se estende além das bordas da janela.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual o Menu Designer é aberto. O Menu Designer não assume as características da janela pai e não pode ser movido para fora da janela pai. Se a janela pai é movida, o Menu Designer se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar o Menu Designer.
**IN SCREEN**
Especifica que o Menu Designer é aberto explicitamente na janela principal do Visual FoxPro, após o Menu Designer ter sido colocado em uma janela pai. O Menu Designer é colocado em uma janela pai incluindo a cláusula IN WINDOW.

# Observações

Emitir CREATE MENU sem argumentos adicionais abre o Menu Designer no qual você pode definir um sistema de menu. O nome MENU1 é temporariamente atribuído à tabela de definição de menu. Quando você sai do Menu Designer, pode salvar a definição de menu com um nome diferente.
