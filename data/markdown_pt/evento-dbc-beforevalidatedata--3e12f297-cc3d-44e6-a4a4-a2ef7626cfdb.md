# Evento dbc_BeforeValidateData

Ocorre imediatamente antes da execução do comando VALIDATE DATABASE. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeValidateData
(lRecover, lNoConsole, lPrint, lFile [, cFilename])
```

```foxpro
PROCEDURE dbc_BeforeValidateData
LPARAMETERS lRecover, lNoConsole, lPrint, lFile [, cFilename]
```

#### Parâmetros
 **lRecover**
Especifica se a palavra-chave RECOVER foi incluída no comando VALIDATE DATABASE que disparou este evento.
**lNoConsole**
Especifica se a palavra-chave NOCONSOLE foi incluída no comando VALIDATE DATABASE que disparou este evento.
**lPrint**
Especifica se a palavra-chave PRINT foi incluída no comando VALIDATE DATABASE que disparou este evento.
**lFile**
Especifica se a palavra-chave FILE foi incluída no comando VALIDATE DATABASE que disparou este evento.
**cFilename**
Especifica o nome do arquivo de saída nomeado na cláusula TO FILE do comando VALIDATE DATABASE. cFilename é opcional, mas se você omiti-lo e usar a cláusula TO FILE de VALIDATE DATABASE, receberá o erro "Must specify additional parameters." Se você não usar TO FILE e incluir o parâmetro cFilename, ele receberá um valor de .F..

# Observações

Você pode usar o evento dbc_BeforeValidateData para rastrear tentativas de acesso ao banco de dados antes da validação dos dados.

Retorne .F. deste procedimento para impedir que o banco de dados seja validado.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameters passed.
PROCEDURE dbc_BeforeValidateData;
         (lRecover, ;
          lNoConsole, ;
          lPrint, ;
          lFile, ;
          cFileName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     lRecover   = ' + TRANSFORM(lRecover)   + ' - ' ;
                    + TYPE('lRecover')
 ? '     lNoConsole = ' + TRANSFORM(lNoConsole) + ' - ' ;
                    + TYPE('lNoConsole')
 ? '     lPrint     = ' + TRANSFORM(lPrint)     + ' - ' ;
                    + TYPE('lPrint')
 ? '     lFile      = ' + TRANSFORM(lFile)      + ' - ' ;
                    + TYPE('lFile')
 ? '     cFileName  = ' + TRANSFORM(cFileName)  + ' - ' ;
                    + TYPE('cFileName ')+' /end/ '
ENDPROC
```
