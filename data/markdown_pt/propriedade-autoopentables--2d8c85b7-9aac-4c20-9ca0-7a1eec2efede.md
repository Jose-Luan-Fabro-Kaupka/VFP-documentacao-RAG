# Propriedade AutoOpenTables

Determina se as tabelas ou views associadas ao ambiente de dados de um form set, formulário ou relatório são carregadas automaticamente. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
DataEnvironment.AutoOpenTables [= lExpr]
```

#### Parâmetros
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista os valores para lExpr . lExpr Descrição True (.T.) As tabelas e views do form set, formulário ou relatório são abertas automaticamente. (Padrão) False (.F.) As tabelas e views não são abertas automaticamente.

# Observações

Aplica-se a: objeto DataEnvironment

Quando AutoOpenTables está definido como True (.T.), o ambiente de dados chama automaticamente o método AutoOpen de qualquer objeto CursorAdapter contido no ambiente de dados. O ambiente de dados abre quaisquer cursors ou cursor adapters na ordem em que foram adicionados ao ambiente de dados.

Quando AutoOpenTables está definido como False (.F.), você pode chamar o método OpenTables do ambiente de dados para carregar programaticamente o ambiente de dados.
