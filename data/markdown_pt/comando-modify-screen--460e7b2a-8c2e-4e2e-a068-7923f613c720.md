# Comando MODIFY SCREEN

Incluído para compatibilidade retroativa. Use o comando MODIFY FORM em vez disso.

Abre a janela Screen Design e permite criar ou modificar uma tela.

```foxpro
MODIFY SCREEN [file | ?]
	[[WINDOW window name1]
	[IN [WINDOW] window name2
	| IN SCREEN | IN MACDESKTOP]]
	[NOENVIRONMENT]
	[NOWAIT]
	[SAVE]
```

#### Parâmetros
 file

 Você pode modificar uma tela existente especificando o nome do arquivo de definição de tela. Se o arquivo especificado não existir ou não puder ser encontrado, uma nova tela é criada.

?

 Se você incluir a cláusula ? ou omitir o nome do arquivo de tela, a caixa de diálogo Open é exibida e mostra uma lista de arquivos de tela existentes para escolha. Você também pode escolher New para criar um novo arquivo de tela. Se escolher New, o nome Untitled é atribuído à janela Screen Design. Você pode salvar o arquivo de tela com um nome diferente ao fechar a janela Screen Design.

WINDOW window name1

 Se você incluir WINDOW window name1, a janela Screen Design assume as características da janela especificada. Por exemplo, se a janela for definida com a cláusula FLOAT de DEFINE WINDOW, a janela Screen Design pode ser movida. A janela especificada não precisa estar ativa ou visível, mas deve estar definida.

IN [WINDOW] window name2

 Se você incluir IN WINDOW window name2, a janela Screen Design é aberta dentro de uma janela pai sem assumir as características da janela pai. Uma janela Screen Design ativada dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai for movida, a janela Screen Design se move com ela.

 Para acessar a janela Screen Design, a janela pai deve primeiro ser definida com DEFINE WINDOW e deve estar visível.

IN SCREEN

 Ao incluir IN SCREEN, você pode colocar explicitamente uma janela Screen Design na janela principal do FoxPro quando uma janela definida pelo usuário estiver ativa. A janela Screen Design é colocada na janela principal do FoxPro por padrão.

IN MACDESKTOP

 MACDESKTOP está disponível somente no FoxPro para Macintosh.

 Inclua a cláusula MACDESKTOP para colocar uma janela Screen Design na área de trabalho do Macintosh. A janela Screen Design reside no mesmo nível da janela principal do FoxPro. A janela Screen Design pode ser movida para fora da janela principal do FoxPro e a janela principal do FoxPro pode ser trazida para a frente sobre ela. Quando você inclui a cláusula MACDESKTOP, a janela Screen Design se comporta da mesma forma que as janelas no FoxBASE+ para Macintosh.

 Incluir a cláusula MACDESKTOP substitui a configuração atual de SET MACDESKTOP. SET MACDESKTOP determina se as janelas Screen Design são colocadas na janela principal do FoxPro ou na área de trabalho do Macintosh quando a cláusula SCREEN ou MACDESKTOP não é incluída. Para mais informações sobre como colocar janelas Screen Design na janela principal do FoxPro ou na área de trabalho do Macintosh, consulte SET MACDESKTOP.

NOENVIRONMENT

 Ao fechar a janela Screen Design, você é solicitado a salvar o ambiente FoxPro atual com o arquivo de definição de tela. Salvar o ambiente FoxPro coloca um registro adicional na tabela de definição de tela. Este registro contém os nomes de todos os arquivos de tabela e índice abertos, a ordem do índice e quaisquer relacionamentos entre as tabelas.

 MODIFY SCREEN restaura automaticamente o ambiente salvo com o arquivo de definição de tela se você salvou o ambiente FoxPro. Se você incluir NOENVIRONMENT, o ambiente não é restaurado. Inclua NOENVIRONMENT para evitar alterações no ambiente atual.

NOWAIT

 Quando você emite MODIFY SCREEN de dentro de um programa, a janela Screen Design é aberta e a execução do programa é pausada até que a janela Screen Design seja fechada. Inclua NOWAIT para continuar a execução do programa após a janela Screen Design ser aberta. O programa continua executando na linha do programa imediatamente após MODIFY SCREEN NOWAIT.

 NOWAIT está disponível somente de dentro de um programa. Incluir NOWAIT não tem efeito em MODIFY SCREEN quando emitido na janela Command.

SAVE

 Inclua SAVE para manter uma imagem da janela Screen Design na janela principal do FoxPro ou em uma janela definida pelo usuário após a janela Screen Design ser fechada. Depois de fechar a janela Screen Design, ela normalmente é removida da janela principal do FoxPro ou de uma janela definida pelo usuário. Use CLEAR para apagar a janela Screen Design da janela principal do FoxPro ou de uma janela definida pelo usuário.

 SAVE está disponível somente de dentro de um programa. Incluir SAVE não tem efeito quando emitido na janela Command.

# Observações

Para mais informações sobre como criar e modificar telas, consulte o capítulo "Designing a Custom Screen with the Screen Builder" no FoxPro User's Guide ou o capítulo "Designing a Custom Input Screen" no manual FoxPro Getting Started.
