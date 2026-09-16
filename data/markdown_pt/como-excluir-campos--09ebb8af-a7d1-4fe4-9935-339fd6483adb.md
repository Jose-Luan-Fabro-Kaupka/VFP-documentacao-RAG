# Como: excluir campos

Você pode excluir um campo de uma tabela.

> **Cuidado:** Excluir um campo de uma tabela exclui as informações sobre ele, incluindo seu valor padrão, definições de regras e Caption. Se uma chave de índice ou expressão de gatilho fizer referência ao campo, a expressão se tornará inválida quando ele for excluído. A chave ou expressão inválida não gerará erro até o tempo de execução.

### Para excluir um campo de uma tabela
- Abra a tabela no Designer de Tabelas.
- Na guia Fields, selecione o campo desejado.
- Clique em Delete.

### Para excluir um campo de uma tabela por meio de programação
- Use o comando SQL ALTER TABLE com a cláusula DROP COLUMN.

Para obter mais informações, consulte Comando ALTER TABLE - SQL.

Por exemplo, o comando a seguir exclui um campo chamado Fax de uma tabela de clientes:

```foxpro
ALTER TABLE Customer DROP COLUMN Fax
```
