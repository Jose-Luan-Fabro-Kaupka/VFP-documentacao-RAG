# Propriedade OpenViews

Determina o tipo de views associadas ao ambiente de dados de um form-set, formulário ou relatório que são abertas automaticamente. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
DataEnvironment.OpenViews[ = nExpression]
```

# Valor de retorno
 **nExpression**
As configurações da propriedade OpenViews são: Configuração Descrição 0 (Padrão) Local e Remota. Tanto as views locais quanto as remotas do ambiente de dados do form-set, formulário ou relatório são abertas automaticamente. 1 Somente local. Somente as views locais do ambiente de dados do form-set, formulário ou relatório são abertas automaticamente. 2 Somente remota. Somente as views remotas do ambiente de dados do form-set, formulário ou relatório são abertas automaticamente. 3 Nenhuma. Nenhuma view é aberta para o ambiente de dados do form-set, formulário ou relatório.

# Observações

Aplica-se a: DataEnvironment Object

A propriedade OpenViews se aplica quando a propriedade AutoOpenTables Property está definida como true (.T.) ou o método OpenTables é executado.
