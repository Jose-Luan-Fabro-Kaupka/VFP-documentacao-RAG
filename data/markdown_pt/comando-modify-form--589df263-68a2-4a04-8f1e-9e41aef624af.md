# Comando MODIFY FORM

Abre o Form Designer para que você possa modificar ou criar um Form.

```foxpro
MODIFY FORM [FormName | ?][NOWAIT][METHOD MethodName]
   [NOENVIRONMENT][SAVE]
   [[WINDOW WindowName1] [IN [WINDOW] WindowName2 | IN SCREEN]]
```

#### Parâmetros
 **FormName**
Especifica o nome do arquivo do Form. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .scx.
**?**
Exibe a caixa de diálogo Open na qual você pode escolher um Form existente ou inserir o nome de um novo Form a ser criado.
**NOWAIT**
Continua a execução do programa depois que o Form Designer foi aberto. O programa não aguarda o fechamento do Form Designer, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY FORM NOWAIT. Se você omitir NOWAIT, quando MODIFY FORM é emitido em um programa, o Form Designer é aberto e a execução do programa é pausada até que o Form Designer seja fechado. NOWAIT é efetivo somente a partir de um programa. Não tem efeito em MODIFY FORM quando emitido da janela Command. Se NOWAIT for incluído com a cláusula METHOD, certifique-se de colocar NOWAIT antes da cláusula METHOD ou NOWAIT será ignorado.
**METHOD MethodName**
Especifica um evento ou método para o qual a janela Code é aberta no Form Designer. A cláusula METHOD permite que você comece imediatamente a editar código de evento ou método no Form Designer. MethodName suporta a sintaxe de objeto do Visual FoxPro. Por exemplo, para editar imediatamente o código do evento Click de uma caixa de texto chamada txtFirstName em um formulário chamado frmAddress, use o seguinte comando: MODIFY FORM frmAddress METHOD txtFirstName.Click Se você incluir apenas um nome de evento ou método na cláusula METHOD, a janela Code é aberta para o evento ou método do formulário. Por exemplo, para editar imediatamente o código do evento Click de um formulário chamado frmAddress, use o seguinte comando: MODIFY FORM frmAddress METHOD Click
**NOENVIRONMENT**
Incluído para compatibilidade com telas 2.x, impedindo que o ambiente salvo com a tela seja restaurado. No Visual FoxPro, o ambiente de dados associado a um formulário do Visual FoxPro é restaurado definindo a propriedade AutoOpenTables do ambiente de dados como true (.T.), que é o padrão. Para garantir que o ambiente do formulário seja fechado quando o formulário é liberado, defina a propriedade AutoCloseTables do ambiente de dados como true (.T.), que também é o padrão. Ao criar ou modificar formulários, você pode salvar o ambiente de dados atual do Visual FoxPro com o arquivo de definição do formulário. Salvar o ambiente de dados do Visual FoxPro coloca registros adicionais na tabela de definição do formulário para todas as tabelas e arquivos de índice abertos, a ordem do índice e quaisquer relacionamentos entre as tabelas.
**SAVE**
Quando emitido em um programa, mantém o Form Designer aberto depois que outra janela é trazida para frente. Incluir a opção SAVE não tem efeito quando emitido da janela Command.
**WINDOW WindowName1**
Especifica uma janela cujas características o Form Designer assume. Por exemplo, se a janela foi criada com a opção FLOAT do DEFINE WINDOW, o Form Designer pode ser movido. A janela não precisa estar ativa ou visível, mas deve estar definida. O Form Designer tem um tamanho padrão que pode ser maior que a janela da qual assume suas características. Nesse caso, o Form Designer ainda assume as características da janela na qual é colocado. O canto superior esquerdo do Form Designer é colocado nas mesmas coordenadas do canto superior esquerdo da janela e se estende além das bordas da janela.
**IN [WINDOW] WindowName2**
Especifica uma janela pai na qual o Form Designer é aberto. O Form Designer não assume as características da janela pai e não pode ser movido para fora da janela pai. Se a janela pai for movida, o Form Designer se move com ela. A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível para acessar o Form Designer.
**IN SCREEN**
Especifica que o Form Designer é explicitamente aberto na janela principal do Visual FoxPro, depois que o Form Designer foi colocado em uma janela pai. O Form Designer é colocado em uma janela pai incluindo a cláusula IN WINDOW.

# Observações

Emitir MODIFY FORM sem argumentos exibe a caixa de diálogo Open. Você pode salvar o formulário com um nome diferente ao fechar o Form Designer.

# Exemplo

O exemplo a seguir abre o exemplo de controle cronômetro (SWATCH.SCX) no Form Designer.

```foxpro
MODIFY FORM (HOME(2) + 'solution\controls\timer\swatch.scx')
```
