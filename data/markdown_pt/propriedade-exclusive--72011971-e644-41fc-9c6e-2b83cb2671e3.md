# Propriedade Exclusive

Especifica se uma tabela associada a um objeto Cursor é aberta de forma exclusiva. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
DataEnvironment.Cursor.Exclusive[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Exclusive são: Configuração Descrição True (.T.) (Padrão) A tabela associada ao Cursor é aberta de forma exclusiva quando o data environment é carregado. False (.F.) A tabela associada ao cursor não é aberta de forma exclusiva quando o data environment é carregado.

# Observações

Aplica-se a: Cursor Object

> **Observação:** Quando o objeto Cursor é acessado usando CURSORSETPROP(), a propriedade Exclusive é somente leitura em tempo de execução.

Quando o data environment é carregado, cada tabela associada a um Cursor pode ser aberta de forma exclusiva (nenhum outro usuário em um ambiente multiusuário pode acessar a tabela) ou em modo compartilhado. Use a propriedade Exclusive para especificar como a tabela é acessada.

> **Observação:** Se você definir a propriedade DataSession como 2 (Private Data Session), a configuração padrão da propriedade Exclusive para todos os objetos Cursor no data environment é alterada para false (.F.).

Para views, o próprio objeto View é sempre aberto em modo compartilhado. No entanto, as tabelas que definem a view são afetadas pela propriedade Exclusive. Para views locais, as tabelas do Visual FoxPro que definem a view são abertas em modo exclusivo ou compartilhado, dependendo da configuração da propriedade Exclusive. A propriedade Exclusive não tem efeito em views remotas.

A propriedade Exclusive imita o comportamento das cláusulas EXCLUSIVE e SHARE do comando USE.
