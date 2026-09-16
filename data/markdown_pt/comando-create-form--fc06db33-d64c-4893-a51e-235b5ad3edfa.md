# Comando CREATE FORM

Abre o Form Designer.

```foxpro
CREATE FORM [FormName | ?] [AS cClassName FROM cClassLibraryName | ?]
   [NOWAIT] [SAVE] [DEFAULT] [[WINDOW WindowName1] [IN [WINDOW]
            WindowName2 | IN SCREEN]]
```

#### Parâmetros
 **FormName**
Especifica o nome do arquivo do formulário. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .scx. Se um arquivo de formulário com o nome especificado já existir, você será perguntado se deseja substituir o arquivo existente (se SET SAFETY estiver definido como ON).
**?**
Exibe a caixa de diálogo Create, na qual você pode escolher um formulário ou inserir o nome de um novo formulário a criar.
**AS cClassName FROM cClassLibraryName | ?**
Cria um novo formulário a partir de uma classe de formulário em uma biblioteca de classes visuais .vcx. cClassName especifica o nome da classe de formulário definida pelo usuário da qual o novo formulário é criado. Um erro é gerado se cClassName não for baseada em um formulário. cClassLibraryName especifica o nome da biblioteca de classes visuais .vcx que contém a classe de formulário especificada com cClassName . Inclua ? para exibir a caixa de diálogo Open, permitindo especificar a biblioteca de classes visual.
**NOWAIT**
Continua a execução do programa após o Form Designer ser aberto. O programa não aguarda o fechamento do Form Designer, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE FORM NOWAIT. Se você omitir NOWAIT, quando CREATE FORM é emitido em um programa, o Form Designer é aberto e a execução do programa pausa até o Form Designer ser fechado. Incluir NOWAIT não tem efeito em CREATE FORM quando emitido na janela Command.
**SAVE**
Quando emitido em um programa, mantém o Form Designer aberto após outra janela ser trazida para frente. Incluir a opção SAVE não tem efeito quando emitido da janela Command.
**DEFAULT**
Especifica que o Form Designer é aberto com o modelo de formulário padrão do Visual FoxPro, substituindo um modelo de formulário padrão especificado na guia Forms da caixa de diálogo Options. Para informações adicionais sobre modelos de formulário, consulte Criando formulários .
**WINDOW WindowName1**
Especifica uma janela cujas características o Form Designer assume. Por exemplo, se a janela foi criada com a opção FLOAT de DEFINE WINDOW, o Form Designer pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida. O Form Designer tem um tamanho padrão que pode ser maior que a janela da qual assume as características. Nesse caso, o Form Designer ainda assume as características da janela na qual é colocado. O canto superior esquerdo do Form Designer é colocado nas mesmas coordenadas do canto superior esquerdo da janela e se estende além das bordas da janela.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual o Form Designer é aberto. O Form Designer não assume as características da janela pai e não pode ser movido para fora da janela pai. Se a janela pai é movida, o Form Designer se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar o Form Designer .
**IN SCREEN**
Especifica que o Form Designer é explicitamente aberto na janela principal do Visual FoxPro, após o Form Designer ter sido colocado em uma janela pai. O Form Designer é colocado em uma janela pai incluindo a cláusula IN WINDOW.

# Observações

Emitir CREATE FORM sem argumentos adicionais abre um novo formulário no Form Designer. Ao sair do Form Designer, você é solicitado a salvar o formulário com um nome diferente.
