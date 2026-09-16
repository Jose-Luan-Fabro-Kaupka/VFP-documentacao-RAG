# Propriedade Exclude (Visual FoxPro)

Especifica se um arquivo é excluído de um aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe) quando ele é compilado a partir de um projeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Exclude[ = lExpression]
```

# Valor de retorno
 **lExpression**
Especifica se o arquivo é excluído de um .app, .dll ou .exe quando é compilado. Se lExpression for true (.T.), o arquivo é excluído; caso contrário, o arquivo é incluído. O tipo de arquivo determina o valor padrão de lExpression. Por exemplo, tabelas são automaticamente excluídas quando adicionadas a um projeto.

# Observações

Aplica-se a: File Object (Visual FoxPro)

Arquivos excluídos aparecem com um círculo riscado antes de seus nomes no Project Manager. Arquivos excluídos são listados na janela do Project Manager para sua referência, mas você deve distribuí-los manualmente se o aplicativo precisar deles. Você também pode excluir um arquivo escolhendo Exclude no menu Project.
