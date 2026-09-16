# Evento dbc_BeforeCopyProc

Ocorre antes que o comando COPY PROCEDURE comece. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeCopyProc(cFileName, nCodePage, lAdditive)
```

```foxpro
PROCEDURE dbc_BeforeCopyProc
LPARAMETERS cFileName, nCodePage, lAdditive
```

#### Parâmetros
 **cFileName**
Especifica o nome de um arquivo de texto para o qual os procedimentos armazenados serão copiados.
**nCodePage,**
Especifica a página de código do arquivo de texto para o qual os procedimentos armazenados serão copiados. O Visual FoxPro copia o conteúdo do arquivo de texto e, ao fazer isso, converte automaticamente esse conteúdo para a página de código que você especificar.
**lAdditive**
Especifica se a palavra-chave ADDITIVE foi incluída no comando COPY PROCEDURE que acionou este evento.

# Observações

Você pode usar o evento dbc_BeforeCopyProc para rastrear tentativas de acesso ao banco de dados antes que os procedimentos armazenados sejam copiados.

Retorne .F. deste procedimento para impedir que os procedimentos armazenados sejam copiados.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeCopyProc ;
         (cFileName,;
          nCodePage,;
          lAdditive)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC:      ' + SUBSTR(DBC(),RAT('\',DBC())+1)
 ? '     cFileName       = ' + TRANSFORM(cFileName)  + ' - ' + TYPE('cFileName')
 ? '     nCodePage       = ' + TRANSFORM(nCodePage)  + ' - ' + TYPE('nCodePage')
 ? '     lAdditive = ' + TRANSFORM(lAdditive) + ' - ' + TYPE('lAdditive')+' /end/ '
ENDPROC
```
