# Comando RESTORE WINDOW

Restaura definições de janela e status de janela salvos em um arquivo de janela ou campo memo.

```foxpro
RESTORE WINDOW WindowNameList | ALL FROM FileName
 | FROM MEMO MemoFieldName
```

#### Parâmetros
 **WindowNameList**
Especifica uma ou mais janelas a serem restauradas. Separe os nomes das janelas com vírgulas.
**ALL**
Restaura todas as definições de janela no arquivo de janela ou campo memo.
**FROM FileName**
Especifica o arquivo de janela do qual as janelas são restauradas. Um arquivo de janela tem extensão .win. Se o arquivo recebeu outra extensão quando foi salvo, você deve incluir essa extensão em FileName .
**FROM MEMO MemoFieldName**
Especifica o campo memo do qual as janelas são restauradas.

# Observações

Use SAVE WINDOW para armazenar definições de janela em um arquivo de janela ou em um campo memo.

Quaisquer janelas na memória com os mesmos nomes das restauradas são substituídas. O status de uma janela (oculta, ativa e assim por diante) quando ela é salva é preservado quando é restaurada.

# Exemplo

No exemplo a seguir, uma janela chamada `wOutput1` é definida e salva em uma variável. Todas as janelas são limpas e a janela chamada `wOutput1` é restaurada e ativada.

```foxpro
CLEAR
DEFINE WINDOW wOutput1 FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
SAVE WINDOW wOutput1 TO temp
CLEAR WINDOWS
RESTORE WINDOW wOutput1 FROM temp
ACTIVATE WINDOW wOutput1
WAIT "The window wOutput1 has been restored" WINDOW
RELEASE WINDOW wOutput1
```
