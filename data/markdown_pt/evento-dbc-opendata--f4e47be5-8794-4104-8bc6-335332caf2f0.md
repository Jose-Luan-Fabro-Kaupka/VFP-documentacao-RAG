# Evento dbc_OpenData

Ocorre quando um banco de dados é aberto explicitamente pelo comando OPEN DATABASE ou implicitamente por outro comando, como MODIFY DATABASE ou USE com uma tabela contida em um banco de dados fechado. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_OpenData (cDatabaseName, lExclusive, lNoUpdate, lValidate )
```

```foxpro
PROCEDURE dbc_OpenData
LPARAMETERS [cDatabaseName, lExclusive, lNoUpdate, lValidate ]
```

#### Parâmetros
 **cDatabaseName**
Especifica o nome do banco de dados sendo aberto.
**lExclusive**
Especifica se o banco de dados está sendo aberto em modo exclusivo.
**lNoUpdate**
Especifica se a palavra-chave NOUPDATE foi incluída no comando OPEN DATABASE, o que significa que o banco de dados está sendo aberto em modo somente leitura.
**lValidate**
Especifica se a palavra-chave VALIDATE foi incluída no comando OPEN DATABASE, o que faz com que o banco de dados seja validado ao ser aberto.

# Observações

Você pode usar o evento dbc_OpenData para acompanhar tentativas de acesso ao banco de dados enquanto o banco de dados é aberto.

Ao retornar false, este método impede que o banco de dados seja aberto.

# Exemplo

```foxpro
PROCEDURE dbc_OpenData ;
         (cDatabaseName, ;
          lExclusive, ;
          lNoUpdate, ;
          lValidate)
 ? '     cDatabaseName = ' + TRANSFORM(cDatabaseName) + ' - ' ;
                       + TYPE('cDatabaseName')
 ? '     lExclusive    = ' + TRANSFORM(lExclusive) + ' - ' ;
                       + TYPE('lExclusive')
 ? '     lNoUpdate     = ' + TRANSFORM(lNoUpdate)  + ' - ' ;
                       + TYPE('lNoUpdate')
 ? '     lValidate     = ' + TRANSFORM(lValidate)  + ' - ' ;
                       + TYPE('lValidate'
ENDPROC
```
