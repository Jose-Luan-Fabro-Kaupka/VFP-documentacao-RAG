# Evento dbc_AfterCopyProc

Ocorre após a conclusão do comando COPY PROCEDURE. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCopyProc(cFileName, nCodePage, lAdditive)
```

```foxpro
PROCEDURE dbc_AfterCopyProc
LPARAMETERS cFileName, nCodePage, lAdditive
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo de texto para o qual os procedimentos armazenados foram copiados.
**nCodePage,**
Especifica a página de código do arquivo de programa para o qual os procedimentos armazenados são copiados. O Visual FoxPro copia o conteúdo dos procedimentos armazenados no banco de dados e, ao fazer isso, converte automaticamente esse conteúdo para a página de código que você especifica.
**lAdditive**
Especifica se a palavra-chave ADDITIVE foi incluída no comando COPY PROCEDURE que disparou este evento. Se ADDITIVE foi omitido, os procedimentos armazenados substituíram o conteúdo do arquivo de programa.

# Observações

Você pode usar o evento dbc_AfterCopyProc para rastrear o acesso ao banco de dados após a conclusão de um copy procedure.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterCopyProc ;
         (cFileName,;
          nCodePage,;
          lAdditive)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC:      ' + SUBSTR(DBC(),RAT('\',DBC())+1)
 ? '     cFileName       = ' + TRANSFORM(cFileName)  + ' - ' ;
                         + TYPE('cFileName')
 ? '     nCodePage       = ' + TRANSFORM(nCodePage)  + ' - ' ;
                         + TYPE('nCodePage')
 ? '     lAdditive      = ' + TRANSFORM(lAdditive) + ' - ' ;
                         + TYPE('lAdditive')+' /end/ '
ENDPROC
```
