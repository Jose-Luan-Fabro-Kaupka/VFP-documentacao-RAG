# Exemplo Create a Default Unique ID Value for a Field Sample

Arquivo: ...\Samples\Solution\Db\Newid.scx

Este exemplo usa um stored procedure em um banco de dados para fornecer um valor padrão de chave primária.

### Para criar um ID exclusivo padrão
- Adicione uma tabela separada ao banco de dados que armazena o próximo ID para cada tabela no banco de dados. O nome da tabela no exemplo é Ids.dbf. Ela contém dois campos: Table C(10), NextID I .
- Nos stored procedures do banco de dados, crie uma função que retorna o próximo valor de ID da tabela ID. O nome da função no exemplo é NewID . O código desta função está incluído neste tópico.
- Defina o valor padrão do campo para a função.

# Stored Procedure NewID

```foxpro
FUNCTION NewID(tcAlias)
LOCAL lcAlias, lnID, lcOldReprocess, lnOldArea
  lnOldArea = SELECT()

  IF PARAMETERS() < 1
    lcAlias = UPPER(ALIAS())
  ELSE
    lcAlias = UPPER(tcAlias)
  ENDIF

  lcOldReprocess = SET('REPROCESS')
  * Lock until user presses Esc
  SET REPROCESS TO AUTOMATIC
  IF !USED("IDS")
    USE newid!ids IN 0
  ENDIF
  SELECT ids

  IF SEEK(lcAlias, "Ids", "table")
    IF RLOCK()
      lnID = ids.nextid
      REPLACE ids.nextid WITH ids.nextid + 1
      UNLOCK
    ENDIF
  ENDIF

  SELECT (lnOldArea)
  SET REPROCESS TO lcOldReprocess

  RETURN lnID
ENDFUNC
```
