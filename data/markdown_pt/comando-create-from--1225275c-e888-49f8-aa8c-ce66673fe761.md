# Comando CREATE FROM

Cria uma tabela a partir de uma tabela criada pelo comando COPY STRUCTURE EXTENDED.

```foxpro
CREATE [FileName1 [DATABASE DatabaseName [NAME LongTableName]]]
   FROM [FileName2]
```

#### Parâmetros
 **FileNam e1**
Especifica o nome da nova tabela a ser criada.
**DATABASE DatabaseName**
Especifica um banco de dados ao qual a nova tabela será adicionada.
**NAME LongTableName**
Especifica um nome longo para a nova tabela. Nomes longos podem conter até 128 caracteres e podem ser usados no lugar de nomes curtos de arquivo no banco de dados.
**FROM [ FileName2 ]**
Especifica a tabela, criada manualmente ou com COPY STRUCTURE EXTENDED, a partir da qual a nova tabela será criada.

# Observações

Esta variação de CREATE pressupõe que a tabela especificada em FileName2 tenha sido criada manualmente ou com COPY STRUCTURE EXTENDED. Uma nova tabela FileName1 é criada com a estrutura descrita em FileName2. A tabela recém-criada torna-se a tabela ativa.

Se FileName1, FileName2 ou ambos não forem incluídos, será exibida uma caixa de diálogo. Nela, você pode especificar o arquivo a ser criado, o arquivo FROM ou ambos.

> **Observação:** Todos os registros de FileName2, inclusive os marcados para exclusão, são usados para criar FileName1.

CREATE FROM ativa o incremento automático para campos quando o campo FIELD_STEP da tabela criada por COPY STRUCTURE EXTENDED contém um valor válido. Os valores de incremento automático e de passo são mantidos da tabela original.

# Exemplo

O exemplo a seguir exibe a estrutura da tabela "Orders", copia o arquivo de estrutura estendida para a tabela "Temp", navega por "Temp", cria uma tabela chamada "Backup" a partir de "Temp" e exibe a estrutura de "Backup".

```foxpro
CLOSE DATABASES
CLEAR
SET PATH TO (HOME(2) + 'Data\')     && Sets path to database.
USE Orders
DISPLAY STRUCTURE
WAIT WINDOW 'Structure of the Orders table' NOWAIT
COPY STRUCTURE EXTENDED TO Temp
USE Temp
WAIT WINDOW 'Temp table has 1 row per field in Orders' NOWAIT
BROWSE
CREATE Backup FROM Temp
USE Backup
DISPLAY STRUCTURE
WAIT WINDOW 'Backup.dbf has the same structure as Orders' NOWAIT
USE
DELETE FILE Temp.dbf
DELETE FILE Backup.dbf
```
