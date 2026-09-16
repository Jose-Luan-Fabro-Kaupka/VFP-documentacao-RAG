# Comando SAVE WINDOWS

Salva todas ou definições de janela especificadas em um arquivo de janela ou campo memo.

```foxpro
SAVE WINDOWS WindowNameList | ALL TO FileName | TO MEMO MemoFieldName
```

#### Parâmetros
 **WindowNameList**
Especifica uma ou mais janelas a serem salvas. Separe os nomes das janelas com vírgulas.
**ALL**
Salva todas as definições de janela no arquivo de janela ou campo memo.
**TO FileName**
Especifica o arquivo de janela no qual as definições de janela são salvas. Se você não especificar uma extensão ao nomear o arquivo, a extensão padrão .win é atribuída. Se você especificar outra extensão ao salvar as definições de janela em um arquivo, deve incluir a extensão ao restaurar as definições de janela do arquivo.
**TO MEMO MemoFieldName**
Especifica o campo memo no qual as definições de janela são salvas. A tabela contendo o campo memo deve estar aberta; no entanto, não precisa estar na área de trabalho atualmente selecionada. Para salvar definições de janela em uma tabela em outra área de trabalho, inclua o alias da tabela ao especificar o campo memo.

# Observações

Use RESTORE WINDOW para restaurar definições de janela de um arquivo de janela ou campo memo. O status de cada janela também é salvo. Por exemplo, se uma janela estiver oculta quando for salva em um arquivo ou campo memo, ela permanece oculta quando for restaurada.

# Exemplo

No exemplo a seguir, uma janela chamada `wOutput1` é criada e a definição da janela é salva no arquivo Temp.win. Todas as janelas são limpas e `wOutput1` é restaurada do arquivo e ativada.

```foxpro
CLEAR
DEFINE WINDOW wOutput1 FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
ACTIVATE WINDOW wOutput1
@ 1,1 SAY 'This is the contents of the window'
SAVE WINDOWS wOutput1 TO temp
CLEAR WINDOWS
WAIT WINDOW 'The window has been saved - Press a key'
RESTORE WINDOW wOutput1 FROM temp
ACTIVATE WINDOW wOutput1
WAIT WINDOW 'The window has been restored - Press a key'
DEACTIVATE WINDOW wOutput1
RELEASE WINDOW wOutput1
DELETE FILE temp.win
```
