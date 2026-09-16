# Comando PACK

Remove permanentemente todos os registros marcados para exclusão na tabela atual e reduz o tamanho do arquivo memo (.fpt) da tabela associada à tabela.

> **Observação:** Você deve abrir a tabela de forma exclusiva antes de usar o comando PACK.

```foxpro
PACK [MEMO | DBF] [Tablename ] [IN nWorkarea | cTableAlias]
```

#### Parâmetros
 **MEMO**
Remove o espaço não utilizado do arquivo memo, mas não remove registros marcados para exclusão da tabela. As informações em campos memo são armazenadas em um arquivo memo (.fpt) associado à tabela, que tem o mesmo nome de arquivo da tabela.
**DBF**
Remove registros marcados para exclusão da tabela, mas não afeta o arquivo memo.
**Tablename**
Especifica a tabela a compactar. O Visual FoxPro abre a tabela especificada, compacta e a fecha.
**IN nWorkArea | cTableAlias**
Especifica a área de trabalho ou o alias da tabela afetado pelo comando PACK. Use esta cláusula para especificar uma área de trabalho ou uma tabela fora da área de trabalho atual.

# Observações

Quando você usa PACK, o Microsoft Visual FoxPro copia todos os registros não marcados para exclusão para uma tabela temporária. Depois que PACK termina de executar, o Visual FoxPro exclui a tabela original do disco e renomeia a tabela temporária com o nome original da tabela. Se você pressionar a tecla ESC para cancelar PACK, a tabela temporária é excluída e a tabela original permanece inalterada. A tabela original também é recuperada se você ficar sem espaço em disco enquanto PACK está executando.

Quando você emite PACK sem as cláusulas MEMO e DBF, PACK afeta tanto a tabela quanto o arquivo memo.

PACK requer uso exclusivo da tabela. Para obter mais informações sobre como abrir uma tabela de forma exclusiva em uma rede, consulte Comando SET EXCLUSIVE.

Se a tabela atual tem um ou mais índices abertos, PACK reconstrói os arquivos de índice.

> **Cuidado:** Tenha cuidado para marcar apenas registros que você não precisa mais. Não há forma de recuperar registros excluídos depois de usar PACK.

Se você omitir a cláusula IN, PACK funciona na área de trabalho atual.

Quando você usa PACK com uma tabela que contém campos de autoincremento, a tabela resultante não é reincrementada, ou seja, os valores existentes são preservados e existem lacunas onde os registros excluídos foram removidos. Para obter mais informações, consulte Valores de campo de autoincremento em tabelas.

Se não existem registros excluídos, PACK não modifica a tabela nem seu índice.
