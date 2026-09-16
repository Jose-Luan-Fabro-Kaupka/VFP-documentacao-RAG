# Como: Gerenciar relacionamentos persistentes entre tabelas

Você pode editar e excluir relações persistentes entre tabelas de banco de dados.

## # Para editar uma relação persistente entre tabelas
- Abra a base de dados no Designer de Banco de Dados.
- No Designer de Banco de Dados, clique na linha de relacionamento entre as duas tabelas.
- No menu Banco de Dados, clique em Editar Relacionamento . Dica Você também pode clicar duas vezes na linha de relacionamento entre as duas tabelas.
- Na caixa de diálogo Editar relacionamento, altere as configurações que você deseja.

Para mais informações, consulte Editar a Janela de Relacionamento.

Para apagar uma relação persistente entre tabelas
- Abra a base de dados no Designer de Banco de Dados.
- No Designer de Banco de Dados, clique na linha de relacionamento entre as duas tabelas.
- Carregue na tecla DELETE.

For more information, see Database Designer (Visual FoxPro).

## # Para apagar uma relação persistente entre tabelas programaticamente
- Use o comando ALTER TABLE e inclua a cláusula DROP FOREIGN KEY.

For more information, see ALTER TABLE - SQL Command.

Por exemplo, o seguinte código exclui uma relação persistente entre duas tabelas, Cliente e Pedidos, com base na chave de índice primário, Cust ID, na tabela Cliente e uma chave estrangeira, Cust ID, na tabela Ordens:

```foxpro
ALTER TABLE Orders DROP FOREIGN KEY TAG Cust_ID SAVE
```

Veja também
- Como: Abrir bases de dados
- Como: Construir Integridade referencial entre tabelas
- Criar bases de dados
- Trabalhar com itens em bases de dados
