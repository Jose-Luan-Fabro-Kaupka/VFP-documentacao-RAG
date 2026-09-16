# Comando MODIFY FILE

Abre uma janela de edição para que você possa modificar ou criar um arquivo de texto.

```foxpro
MODIFY FILE [FileName | ?] [NOEDIT] [NOMENU] [NOWAIT]
   [RANGE nStartCharacter, nEndCharacter] [[WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN]] [AS nCodePage] [SAME] [SAVE]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo de texto. Se você não especificar uma extensão para um novo arquivo de texto, o Visual FoxPro atribui automaticamente a extensão .txt. MODIFY FILE suporta um esqueleto de arquivo que pode conter os curingas asterisco (*) e ponto de interrogação (?). Uma janela de edição é aberta para cada arquivo de texto cujo nome corresponda ao esqueleto de arquivo. Se você omitir o nome do arquivo, uma janela de edição abre para um arquivo inicialmente chamado FILE1. Quando você fecha a janela de edição, pode salvar o arquivo com um nome diferente.
**?**
Exibe a caixa de diálogo Open, na qual você pode escolher um arquivo de texto.
**NOEDIT**
Especifica que o arquivo de texto não pode ser alterado, mas pode ser visualizado e copiado para a Área de Transferência.
**NOMENU**
Remove o título do menu Format da barra de menus do sistema do Visual FoxPro, impedindo alterações na fonte, tamanho da fonte, espaçamento entre linhas e indentação.
**NOWAIT**
Continua a execução do programa após a janela de edição ser aberta. O programa não aguarda o fechamento da janela de edição, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY FILE NOWAIT. Se você omitir NOWAIT quando MODIFY FILE é emitido em um programa, a janela de edição é aberta e a execução do programa pausa até que a janela de edição seja fechada. NOWAIT é eficaz somente dentro de um programa. Não tem efeito em MODIFY FILE quando emitido na janela Command. Um NOWAIT implícito ocorre se você abrir mais de uma janela de edição com um único comando MODIFY FILE. Por exemplo: MODIFY FILE *.TXT
**RANGE nStartCharacter , nEndCharacter**
Especifica um intervalo de caracteres selecionados quando você abre uma janela de edição. Os caracteres são selecionados começando na posição especificada com nStartCharacter até (mas não incluindo) a posição do caractere de nEndCharacter. Se nStartCharacter for igual a nEndCharacter, nenhum caractere é selecionado e o cursor é posicionado na posição especificada com nStartCharacter.
**WINDOW WindowName1**
Especifica uma janela cujas características a janela de edição assume. Por exemplo, se a janela for criada com a opção FLOAT de DEFINE WINDOW, a janela de edição pode ser movida. A janela não precisa estar ativa ou visível, mas deve estar definida.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual a janela de edição é aberta. A janela de edição não assume as características da janela pai e não pode ser movida para fora da janela pai. Se a janela pai for movida, a janela de edição se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar a janela de edição.
**IN SCREEN**
Abre explicitamente a janela de edição na janela principal do Visual FoxPro, após ela ter sido colocada em uma janela pai. Uma janela de edição é colocada em uma janela pai incluindo a cláusula IN WINDOW.
**AS nCodePage**
Converte automaticamente caracteres acentuados em um arquivo de texto criado em outra plataforma do Visual FoxPro. A expressão numérica nCodePage especifica a página de código da plataforma do Visual FoxPro na qual o arquivo de texto foi criado. O arquivo é salvo nesta página de código, a menos que você escolha Save As no menu File para salvar o arquivo em uma página de código diferente.
**SAME**
Impede que a janela de edição venha para frente como a janela ativa. Se a janela de edição estiver oculta, ela é exibida, mas não se torna a janela ativa.
**SAVE**
Mantém a janela de edição aberta após outra janela ser ativada. Se você omitir SAVE, a janela de edição é fechada quando outra janela é ativada. Incluir SAVE não tem efeito quando emitido na janela Command.

# Observações

Quando modificações são feitas em um arquivo de texto, o arquivo atualizado é gravado no disco. No Visual FoxPro, um arquivo de backup com extensão .bak é criado se você selecionar a caixa de seleção Make Backup Copy na caixa de diálogo Edit Properties, que aparece quando você escolhe Properties no menu Edit. Em versões anteriores do FoxPro, um arquivo de backup com extensão .bak é criado se você selecionar a caixa de seleção Backup na caixa de diálogo Preferences, que aparece quando você escolhe Preferences no menu Edit.

O editor do Visual FoxPro é usado, a menos que você especifique um editor externo com TEDIT no arquivo de configuração.
