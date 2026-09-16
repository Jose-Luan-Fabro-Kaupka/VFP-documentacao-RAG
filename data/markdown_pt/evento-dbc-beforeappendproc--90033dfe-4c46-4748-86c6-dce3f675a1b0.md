# Evento dbc_BeforeAppendProc

Ocorre antes que um comando APPEND PROCEDURES seja concluído. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeAppendProc(cFileName, nCodePage, lOverwrite)
```

```foxpro
PROCEDURE dbc_BeforeAppendProc
LPARAMETERS cFileName, nCodePage, lOverwrite
```

#### Parâmetros
 **cFileName**
Especifica o nome de um arquivo de texto do qual os procedimentos armazenados serão anexados.
**nCodePage,**
Especifica a página de código do arquivo de texto do qual os procedimentos armazenados serão anexados. O Visual FoxPro copia o conteúdo do arquivo de texto e, ao fazer isso, converte automaticamente esse conteúdo para a página de código que você especificar.
**lOverwrite**
Especifica se a palavra-chave OVERWRITE foi incluída no comando APPEND PROCEDURE. Se OVERWRITE foi omitido, os procedimentos armazenados atuais no banco de dados são anexados aos procedimentos armazenados existentes; caso contrário, eles substituem quaisquer procedimentos existentes.

# Observações

Você pode usar o dbc_BeforeAppendProc para rastrear tentativas de acesso ao banco de dados antes que os procedimentos armazenados sejam anexados.

Retorne .F. deste procedimento para impedir que o conteúdo do arquivo de texto seja anexado aos procedimentos armazenados do banco de dados.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeAppendProc ;
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
