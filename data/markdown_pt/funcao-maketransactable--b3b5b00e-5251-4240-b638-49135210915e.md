# Função MAKETRANSACTABLE( )

Permite que uma tabela livre ou um cursor livre suporte transações.

```foxpro
MAKETRANSACTABLE([nWorkArea | cAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela ou do cursor para o qual as transações serão suportadas.
**cAlias**
Especifica o alias da tabela ou do cursor para o qual as transações serão suportadas.

# Valor de retorno

Valor lógico. Retorna um valor lógico true (.T.) se MAKETRANSACTABLE( ) conseguiu fazer a tabela livre ou o cursor livre suportar transações; caso contrário, retorna um valor lógico false (.F.).

# Observações

Uma tabela livre é uma tabela que não foi adicionada a um banco de dados com o comando ADD TABLE. Um cursor livre é um cursor criado a partir de uma tabela livre ou com o comando CREATE CURSOR - SQL.

Quando MAKETRANSACTABLE( ) é usado para fazer uma tabela livre ou um cursor livre suportar transações, você pode usar os comandos BEGIN TRANSACTION, END TRANSACTION e ROLLBACK para a tabela livre ou o cursor livre. Use a função ISTRANSACTABLE( ) para determinar se uma tabela livre ou um cursor livre suporta transações.

> **Observação:** Quando MAKETRANSACTABLE( ) é usado para fazer uma tabela livre ou um cursor livre suportar transações, a tabela livre ou o cursor livre suporta transações em todas as áreas de trabalho e sessões de dados em que é aberto. MAKETRANSACTABLE( ) faz todas as instâncias abertas de uma tabela livre ou de um cursor livre suportar transações, incluindo aquelas em outras sessões de dados dentro de uma única instância do VFP.

Se uma tabela livre que não suporta transações estiver aberta em mais de uma sessão de dados, a tabela livre não pode ser configurada para suportar transações. Porém, você pode abrir uma tabela livre que já suporta transações em sessões de dados adicionais.

Se o buffer de linha estiver habilitado, uma atualização de tabela é executada se a tabela livre ou o cursor livre tiver alterações pendentes antes de ser configurado para suportar transações. Você não pode usar MAKETRANSACTABLE( ) para habilitar transações para uma tabela livre que tenha buffer de tabela habilitado.

Para desabilitar transações para uma tabela livre, você deve fechar a tabela livre em todas as sessões de dados.
