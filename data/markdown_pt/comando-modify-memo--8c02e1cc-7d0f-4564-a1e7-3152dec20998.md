# Comando MODIFY MEMO

Abre uma janela de edição para um campo Memo ou campo Blob no registro atual.

Você pode visualizar ou alterar o conteúdo do campo Memo; no entanto, o campo Blob é exibido na janela de edição como somente leitura.

```foxpro
MODIFY MEMO MemoField1 [, MemoField2 ...] [NOEDIT] [NOMENU]
   [NOWAIT] [RANGE nStartCharacter, nEndCharacter]
   [[WINDOW WindowName1] [IN [WINDOW] WindowName2 | IN SCREEN]]
   [SAME] [SAVE]
```

#### Parâmetros
 **MemoField1 [, MemoField2 ...]**
Especifica os nomes de um ou mais campos Memo a editar. Dica Para abrir uma janela de edição para um campo Memo em uma tabela aberta em outra área de trabalho, inclua o alias da tabela com o nome do campo.
**NOEDIT**
Especifica que o campo Memo aberto não pode ser alterado; em vez disso, pode ser visualizado e copiado para a Área de Transferência.
**NOMENU**
Oculta o menu Format na barra de menu do sistema do Visual FoxPro para impedir alterações de formatação no campo Memo.
**NOWAIT**
Continua a execução do programa que abre a janela de edição. Observação NOWAIT se aplica apenas quando usado em um programa Visual FoxPro (.prg). Não tem efeito ao executar MODIFY MEMO na janela Command. O programa não espera que a janela de edição seja fechada, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY MEMO NOWAIT. Se você omitir NOWAIT, uma janela de edição é aberta e a execução do programa pausa até que a janela de edição seja fechada.
**RANGE nStartCharacter , nEndCharacter**
Especifica um intervalo de caracteres a aparecer selecionados quando a janela de edição abre. Começando na posição especificada com nStartCharacter, os caracteres são selecionados até, mas não incluindo, a posição do caractere de nEndCharacter. Se nStartCharacter for igual a nEndCharacter, nenhum caractere é selecionado e o cursor é posicionado na posição especificada com nStartCharacter.
**WINDOW WindowName1**
Especifica uma janela cujas características a janela de edição usa. Por exemplo, se a janela for criada com a opção FLOAT do comando DEFINE WINDOW, a janela de edição pode ser movida. A janela especificada deve apenas ser definida; não precisa estar ativa ou visível.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual abrir a janela de edição. Observação A janela pai deve primeiro ser definida com o comando DEFINE WINDOW e deve estar visível para acessar a janela de edição. A janela de edição não assume as características da janela pai e não pode ser movida para fora da janela pai. Se a janela pai for movida, a janela de edição se move com ela.
**IN SCREEN**
Abre a janela de edição explicitamente na janela principal do Visual FoxPro, depois de colocar a janela de edição em uma janela pai. Você pode colocar uma janela de edição em uma janela pai incluindo a cláusula IN WINDOW.
**SAME**
Impede que a janela de edição apareça como a janela ativa em primeiro plano. Se a janela de edição estiver oculta, ela é exibida, mas não se torna a janela ativa.
**SAVE**
Mantém a janela de edição aberta após ativar outra janela. Se você omitir SAVE, a janela de edição fecha quando outra janela é ativada. Observação Incluir SAVE não tem efeito quando usado na janela Command.

# Observações

Em uma tabela que está aberta para acesso compartilhado em uma rede, o registro atual é automaticamente bloqueado quando a edição começa em um de seus campos Memo.

> **Observação:** Em aplicações de tempo de execução distribuídas, a coloração de sintaxe em janelas de edição de campo Memo está desabilitada. Para obter mais informações, consulte How to: Display and Print Source Code in Color.

# Exemplo

O exemplo a seguir usa o banco de dados de exemplo do Visual FoxPro, TestData, e MODIFY MEMO com as opções NOEDIT e RANGE para abrir um campo Memo chamado Notes para o primeiro registro da tabela Employee. O campo memo abre em uma janela de edição como somente leitura e exibe os primeiros 10 caracteres como selecionados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE employee  && Opens Employee table
MODIFY MEMO Notes NOEDIT RANGE 1,10
```
