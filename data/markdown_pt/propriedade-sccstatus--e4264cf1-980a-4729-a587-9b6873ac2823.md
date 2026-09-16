# Propriedade SCCStatus

Contém um valor numérico indicando o status de controle de origem de um arquivo em um projeto. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.SCCStatus
```

# Observações

Aplica-se a: File Object (Visual FoxPro)

A tabela a seguir lista os valores que a propriedade SCCStatus pode conter:

| Valor | Constante FoxPro.h | Descrição |
| --- | --- | --- |
| 0 | SCCFILE_NOTCONTROLLED | O arquivo não está sob controle de origem. |
| 1 | SCCFILE_NOTCHECKEDOUT | O arquivo está sob controle de origem, mas não está com check-out. |
| 2 | SCCFILE_CHECKEDOUTCU | O arquivo está com check-out para o usuário atual. |
| 3 | SCCFILE_CHECKEDOUTOU | O arquivo está com check-out para outra pessoa que não o usuário atual. |
| 4 | SCCFILE_MERGECONFLICT | O arquivo tem um conflito de mesclagem. |
| 5 | SCCFILE_MERGE | O arquivo foi mesclado sem conflito. |
| 6 | SCCFILE_CHECKEDOUTMU | O arquivo está com check-out para vários usuários. |
