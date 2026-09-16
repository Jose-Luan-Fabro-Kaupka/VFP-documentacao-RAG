# Comando MODIFY QUERY

Abre o Query designer para que você possa modificar ou criar uma consulta.

```foxpro
MODIFY QUERY [FileName | ?] [[WINDOW WindowName1] [IN SCREEN]
   [NOWAIT] [SAVE] [AS nCodePage]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo da consulta. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .qpr.
**?**
Exibe a caixa de diálogo Open, na qual você pode escolher uma consulta existente ou inserir o nome de uma nova consulta a ser criada.
**WINDOW WindowName1**
Especifica uma janela cujas características o Query Designer assume. Por exemplo, se a janela for criada com a opção FLOAT de DEFINE WINDOW, o Query Designer pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida.
**IN SCREEN**
Abre explicitamente o Query Designer na janela principal do Visual FoxPro, depois de ter sido colocado em uma janela pai. O Query Designer é colocado em uma janela pai incluindo a cláusula IN WINDOW.
**NOWAIT**
Continua a execução do programa após o Query Designer ser aberto. O programa não aguarda o fechamento do Query Designer, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY QUERY NOWAIT. Se você omitir NOWAIT quando MODIFY QUERY é emitido em um programa, o Query Designer é aberto e a execução do programa é pausada até que o Query Designer seja fechado. NOWAIT é eficaz somente a partir de um programa. Não tem efeito em MODIFY QUERY quando emitido na janela Command.
**SAVE**
Mantém o Query Designer aberto após outra janela ser ativada. Se você omitir SAVE, o Query Designer é fechado quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido na janela Command.
**AS nCodePage**
Especifica a página de código da consulta. Inclua AS nCodePage se a consulta foi criada com uma página de código diferente da página de código atual do Visual FoxPro. Quando a consulta é aberta, o Visual FoxPro converte automaticamente a consulta para a página de código atual do Visual FoxPro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para a consulta. A consulta é salva em sua página de código original quando é fechada. Se você omitir a cláusula AS nCodePage ou nCodePage for 0, a consulta não é convertida para a página de código atual do Visual FoxPro. Se você especificar um valor para nCodePage que não é suportado, o Visual FoxPro gera uma mensagem de erro. No Visual FoxPro, consultas podem ser adicionadas a um projeto, e você pode especificar a página de código da consulta a partir do Project Container. O Project Container mantém o controle da página de código da consulta. No entanto, se você usar MODIFY QUERY para abrir uma consulta fora do Project Container, deve incluir AS nCodePage para especificar a página de código da consulta.

# Observações

Para obter mais informações sobre como criar consultas, consulte How to: Create Queries (Visual FoxPro).

Emitir MODIFY QUERY sem argumentos exibe a caixa de diálogo Open. Se você escolher New nesta caixa de diálogo, o nome QUERY1 é atribuído à consulta. Você pode salvar a consulta com um nome diferente ao sair do Query Designer.

Depois de criar uma consulta, a consulta é armazenada como um arquivo de programa do Visual FoxPro com extensão .qpr. Você pode executar um programa de consulta com DO, mas deve incluir a extensão .qpr com o nome do arquivo de consulta.
