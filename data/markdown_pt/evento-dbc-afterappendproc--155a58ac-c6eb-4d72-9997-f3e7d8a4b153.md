# Evento dbc_AfterAppendProc

Ocorre após a conclusão do comando APPEND PROCEDURE. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterAppendProc(cFileName, nCodePage, lOverwrite)
```

```foxpro
PROCEDURE dbc_AfterAppendProc
LPARAMETERS cFileName, nCodePage, lOverwrite
```

#### Parâmetros
 **cFileName**
Especifica o nome de um arquivo de texto do qual os procedimentos armazenados foram acrescentados.
**nCodePage,**
Especifica a página de código do arquivo de texto do qual os procedimentos armazenados foram acrescentados. O Visual FoxPro copia o conteúdo do arquivo e o converte automaticamente para a página de código especificada.
**lOverWrite**
Especifica se os procedimentos armazenados atuais do banco de dados foram sobrescritos pelos do arquivo de texto. Se a palavra-chave OVERWRITE tiver sido omitida do comando APPEND PROCEDURE, os procedimentos armazenados atuais do banco de dados serão acrescentados aos procedimentos existentes no arquivo de texto.

# Observações

Você pode usar o evento dbc_AfterAppendProc para acompanhar o acesso ao banco de dados após o acréscimo de procedimentos armazenados.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterAppendProc ;
         (cFileName,;
          nCodePage,;
          lOverwrite)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC:      ' + SUBSTR(DBC(),RAT('\',DBC())+1)
 ? '     cFileName       = ' + TRANSFORM(cFileName)  + ' - ' ;
                         + TYPE('cFileName')
 ? '     nCodePage       = ' + TRANSFORM(nCodePage)  + ' - ' ;
                         + TYPE('nCodePage')
 ? '     lOverwrite      = ' + TRANSFORM(lOverwrite) + ' - ' ;
                         + TYPE('lOverwrite')+' /end/ '
ENDPROC
```
