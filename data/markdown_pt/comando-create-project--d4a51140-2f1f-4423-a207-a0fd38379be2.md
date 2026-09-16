# Comando CREATE PROJECT

Abre o Project Manager para que você possa criar um projeto.

```foxpro
CREATE PROJECT [FileName | ?] [NOWAIT] [SAVE] [WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN [NOSHOW] [NOPROJECTHOOK]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo para a tabela de projeto. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .pjx.
**?**
Exibe a caixa de diálogo Create que solicita que você nomeie o projeto sendo criado.
**NOWAIT**
Continua a execução do programa após o Project Manager ser aberto. O programa não espera que o Project Manager seja fechado, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE PROJECT NOWAIT. Se você omitir NOWAIT quando CREATE PROJECT é emitido em um programa, o Project Manager é aberto e a execução do programa pausa até que o Project Manager seja fechado. Incluir NOWAIT não tem efeito em CREATE PROJECT quando emitido na janela Command.
**SAVE**
Mantém o Project Manager aberto após outra janela ser ativada. Se você omitir SAVE, o Project Manager é fechado quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido da janela Command.
**WINDOW WindowName1**
Especifica uma janela cujas características o Project Manager assume. Por exemplo, se a janela foi criada com a opção FLOAT de DEFINE WINDOW, o Project Manager pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida. O Project Manager tem um tamanho padrão que pode ser maior que a janela da qual assume as características. Nesse caso, o Project Manager ainda assume as características da janela em que é colocado. O canto superior esquerdo do Project Manager é colocado nas mesmas coordenadas do canto superior esquerdo da janela e se estende além das bordas da janela.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual o Project Manager é aberto. O Project Manager não assume as características da janela pai e não pode ser movido fora da janela pai. Se a janela pai é movida, o Project Manager se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar o Project Manager.
**IN SCREEN**
Especifica que o Project Manager é explicitamente aberto na janela principal do Visual FoxPro, após o Project Manager ter sido colocado em uma janela pai. O Project Manager é colocado em uma janela pai incluindo a cláusula IN WINDOW.
**NOSHOW**
Especifica que o Project Manager é ocultado (sua propriedade Visible é definida como False (.F.)) quando é aberto. Para exibir o Project Manager, defina a propriedade Visible do Project Manager como True (.T.). NOSHOW permite manipular um projeto antes de exibi-lo no Project Manager. Observe que para evitar confusão com a palavra-chave NOSHADOW, você não pode abreviar NOSHOW para menos de cinco caracteres.
**NOPROJECTHOOK**
Especifica que um objeto ProjectHook não seja criado quando o Project Manager é aberto. Inclua NOPROJECTHOOK para projetos que não serão manipulados programaticamente através dos hooks do Project Manager. Observe que um objeto Project ainda é criado sempre que um arquivo de projeto (.pjx) é aberto.

# Observações

Um projeto é uma tabela que acompanha todos os arquivos necessários para criar uma aplicação, bem como todas as dependências, referências e conexões entre os arquivos. Uma tabela de projeto tem extensão .pjx e um arquivo de memo associado com extensão .pjt. Em um projeto, você especifica todas as peças necessárias para uma aplicação, e o Visual FoxPro garante que os arquivos compilados sejam baseados nos arquivos de origem mais recentes.

Uma tabela de projeto pode ser aberta com USE e manipulada como qualquer outra tabela do Visual FoxPro.

Emitir o comando CREATE PROJECT sem argumentos adicionais exibe a caixa de diálogo Create, permitindo especificar um nome para o projeto.
