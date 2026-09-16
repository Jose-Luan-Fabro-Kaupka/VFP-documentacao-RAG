# Como: remover regras de validação

Se você não deseja mais usar uma regra de validação de campo ou registro, pode removê-la.

> **Observação:** Regras de validação são armazenadas no arquivo de banco de dados (.dbc). Remover ou excluir uma tabela de banco de dados remove e exclui todas as regras de validação de campo e registro associadas a essa tabela. No entanto, procedimentos armazenados referenciados pelas regras de validação removidas ou excluídas permanecem.

### Para remover uma regra de validação de campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer .
- No Table Designer , selecione o campo desejado.
- Na caixa Rule da área Field validation, exclua a expressão de validação.
- Na caixa Message, exclua a mensagem de erro personalizada ou expressão.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Fields, Table Designer.

### Para remover uma regra de validação de registro
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer .
- No Table Designer , clique na guia Table.
- Na caixa Rule da área Record validation, exclua a expressão de validação.
- Na caixa Message, exclua a mensagem de erro personalizada ou expressão.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Table, Table Designer.

### Para remover uma regra de validação programaticamente
- Abra a tabela com o comando USE.
- Use o comando SQL ALTER TABLE com a cláusula DROP CHECK.

Para obter mais informações, consulte Comando ALTER TABLE - SQL.
