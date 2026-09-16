# Propriedade OneToMany

Ao percorrer registros na tabela pai, especifica se o ponteiro de registro permanece no mesmo registro pai até que o ponteiro de registro da tabela filha percorra todos os registros relacionados. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.DataEnvironment.Relation.OneToMany[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade OneToMany são: Configuração Descrição True (.T.) O ponteiro de registro permanece no mesmo registro pai até que o ponteiro de registro da tabela filha percorra todos os registros relacionados. False (.F.) (Padrão) O ponteiro de registro da tabela pai move-se para o registro especificado e o ponteiro de registro da tabela filha move-se para o primeiro registro relacionado.

# Observações

Aplica-se a: Relation Object

A propriedade OneToMany pode ser usada para especificar o movimento do ponteiro de registro em uma relação simples pai-filho. Para especificar o movimento do ponteiro de registro em uma relação mais complexa (por exemplo, avô-pai-filho), use SET SKIP no método Init do formulário ou relatório.

Quando OneToMany é definido como true (.T.), ele imita o comportamento de SET SKIP.
