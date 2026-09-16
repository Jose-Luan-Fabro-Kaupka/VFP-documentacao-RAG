# Propriedade ConflictCheckCmd

Especifica um comando personalizado a ser usado para verificar conflitos de atualização ou exclusão quando CursorAdapter ConflictCheckType está definido como 4. Leitura/gravação em tempo de design e em tempo de execução.

Você pode usar ConflictCheckCmd com fontes de dados nativas, Open Database Connectivity (ODBC) e ActiveX Object (ADO). Ao usar ADO, o objeto CursorAdapter deve usar um objeto ADO Command para a operação SQL UPDATE ou DELETE. Caso contrário, o Visual FoxPro ignora ConflictCheckCmd.

```foxpro
CursorAdapter.ConflictCheckCmd [= cValue]
```

#### Parâmetros
 **cValue**
Especifica uma referência de cadeia de comando personalizada a ser anexada aos comandos especificados pelas propriedades UpdateCmd e DeleteCmd para verificar conflitos de atualização ou exclusão. O valor padrão de cValue contém uma cadeia de caracteres vazia.

# Observações

Aplica-se a: classe CursorAdapter
