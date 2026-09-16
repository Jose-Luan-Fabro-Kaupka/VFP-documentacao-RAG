# Comando CREATE SCREEN

Incluído para compatibilidade com versões anteriores. Use o Comando CREATE FORM em vez disso.

Abre uma janela Screen Design.

```foxpro
CREATE SCREEN [file | ?]
	[NOWAIT] [SAVE]
	[[WINDOW window name1]
	[IN [WINDOW] window name2
	| IN SCREEN | IN MACDESKTOP]]
```

#### Parâmetros
 file

 Emitir CREATE SCREEN sem argumentos adicionais abre uma nova janela Screen Design. O nome UNTITLED é atribuído à definição de tela. Quando você sai da janela Screen Design, é solicitado que salve a definição de tela com um nome diferente.

 Se um nome de arquivo for incluído, a tela é salva com esse nome. Uma extensão .SCX é atribuída automaticamente. Se um arquivo de tela com esse nome já existir, você será perguntado se deseja substituir o arquivo existente (se SET SAFETY estiver ON).

?

 A caixa de diálogo Abrir aparece quando o ponto de interrogação (?) é incluído. Uma lista de arquivos de tela existentes é exibida. Escolha uma das telas existentes ou insira o nome de uma nova tela para criar.

NOWAIT

 Quando CREATE SCREEN é emitido em um programa, uma janela Screen Design é aberta e a execução do programa é pausada até que a janela Screen Design seja fechada.

 A opção NOWAIT continua a execução do programa depois que a janela Screen Design foi aberta. O programa não aguarda que a janela Screen Design seja fechada, mas continua a execução na linha do programa imediatamente após a linha que contém CREATE SCREEN NOWAIT. Incluir a opção NOWAIT não tem efeito no comando CREATE SCREEN quando ele é emitido na janela Command.

SAVE

 Durante a execução do programa, SAVE deixa a janela Screen Design aberta depois que outra janela é trazida para frente. Incluir a opção SAVE não tem efeito quando emitido da janela Command.

 No FoxPro para MS-DOS, você pode fechar uma janela Screen Design aberta com a opção SAVE pressionando Ctrl+W, Ctrl+End, Ctrl+Q ou Esc, clicando na caixa de fechamento ou escolhendo a opção Fechar no menu Arquivo.

 No FoxPro para Windows, você pode fechar uma janela Screen Design aberta com a opção SAVE pressionando Ctrl+W, Ctrl+End ou Esc, clicando na caixa de fechamento ou escolhendo Fechar no menu de controle da janela Screen Design ou no menu Arquivo.

 No FoxPro para Macintosh, você pode fechar uma janela Screen Design aberta com a opção SAVE pressionando Ctrl+W, Ctrl+End ou Esc, clicando na caixa de fechamento ou escolhendo Fechar no menu Arquivo.

WINDOW window name1

 Se você incluir WINDOW window name1, a janela Screen Design assume as características da janela especificada. Por exemplo, se a janela for criada com a opção FLOAT de DEFINE WINDOW, a janela Screen Design pode ser movida. A janela não precisa estar ativa ou visível, mas deve estar definida.

 A janela Screen Design tem um tamanho padrão que pode ser maior que a janela da qual ela assume as características. Nesse caso, a janela Screen Design ainda assume as características da janela na qual é colocada. O canto superior esquerdo da janela Screen Design é colocado nas mesmas coordenadas do canto superior esquerdo da janela e pode se estender além das bordas da janela.

IN [WINDOW] window name2

 Se IN WINDOW window name2 for incluído, a janela Screen Design é aberta dentro de uma janela pai. Ela não assume as características da janela pai na qual é colocada. Uma janela Screen Design ativada dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai for movida, a janela Screen Design se move com ela.

 A janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar ativa e visível para acessar a janela Screen Design.

IN SCREEN

 Você pode colocar uma janela Screen Design na janela principal do FoxPro incluindo IN SCREEN. Esta cláusula permite colocar explicitamente uma janela Screen Design na janela principal do FoxPro quando uma janela definida pelo usuário está ativa. As janelas Screen Design são colocadas na janela principal do FoxPro por padrão.

IN MACDESKTOP

 MACDESKTOP está disponível apenas no FoxPro para Macintosh.

 Inclua a cláusula MACDESKTOP para colocar uma janela Screen Design na área de trabalho do Macintosh. A janela Screen Design reside no mesmo nível da janela principal do FoxPro. A janela Screen Design pode ser movida para fora da janela principal do FoxPro e a janela principal do FoxPro pode ser trazida para frente sobre ela. Quando você inclui a cláusula MACDESKTOP, a janela Screen Design se comporta da mesma maneira que as janelas no FoxBASE+ para Macintosh.

 Incluir a cláusula MACDESKTOP substitui a configuração atual de SET MACDESKTOP. SET MACDESKTOP determina se as janelas Screen Design são colocadas na janela principal do FoxPro ou na área de trabalho do Macintosh quando a cláusula SCREEN ou MACDESKTOP não é incluída. Para obter mais informações sobre como colocar janelas Screen Design na janela principal do FoxPro ou na área de trabalho do Macintosh, consulte SET MACDESKTOP.

# Observações

CREATE SCREEN também pode ser usado para gerar uma tela rápida sem abrir a janela de layout de tela. Para obter mais informações, consulte CREATE SCREEN - Quick Screen e o capítulo "Designing Screens with the Screen Builder" no FoxPro User's Guide.
