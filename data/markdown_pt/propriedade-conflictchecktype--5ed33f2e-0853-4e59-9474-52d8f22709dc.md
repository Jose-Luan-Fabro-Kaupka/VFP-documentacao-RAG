# Propriedade ConflictCheckType

Especifica como tratar a verificação de conflitos durante uma operação de atualização ou exclusão usando comandos especificados pelas propriedades UpdateCmd e DeleteCmd do CursorAdapter. Leitura e gravação em tempo de design e em tempo de execução.

Você pode usar ConflictCheckType com fontes de dados nativas, Open Database Connectivity (ODBC) e ActiveX Object (ADO). Ao usar ADO, o objeto CursorAdapter deve usar um objeto ADO Command para a operação SQL UPDATE ou DELETE. Caso contrário, o Visual FoxPro ignora ConflictCheckType.

```foxpro
CursorAdapter.ConflictCheckType [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um número que determina como tratar a verificação de conflitos. A tabela a seguir lista os valores para nValue . nValue Description 0 Não realizar verificações. (Padrão) 1 No modo de atualização de linha única, verificar conflitos de atualização durante uma operação SQL UPDATE ou DELETE. Se ocorrer conflito, especificamente, nenhum registro é afetado por qualquer comando especificado pela propriedade UpdateCmd ou DeleteCmd, retornar mensagem "Update conflict (Error 1585)". 2 No modo de atualização de linha única, verificar unicidade de chave durante uma operação SQL UPDATE ou DELETE. Se mais de um registro é afetado por qualquer comando especificado pela propriedade UpdateCmd ou DeleteCmd, retornar mensagem "Warning: The key defined by the KeyField property for table " alias " is not unique. (Error 1495)" 3 Realizar verificações conforme especificado pelas configurações 1 e 2. 4 Anexar comando personalizado especificado na propriedade ConflictCheckCmd ao final do comando nas propriedades UpdateCmd e DeleteCmd. Observação Devido a limitações de ODBC e ADO, as configurações 1, 2 e 3 podem não funcionar corretamente se as propriedades UpdateCmd e DeleteCmd contiverem mais de um comando. É possível que o número de linhas afetadas não seja retornado para cada comando em um lote. Portanto, é recomendável definir ConflictCheckType como 4 e especificar um comando personalizado na propriedade ConflictCheckCmd ou garantir que apenas um comando SQL UPDATE ou DELETE será executado. Além disso, o Visual FoxPro ignora as configurações 1, 2 e 3 ao realizar uma operação TABLEUPDATE em lote.

# Observações

Aplica-se a: CursorAdapter Class
