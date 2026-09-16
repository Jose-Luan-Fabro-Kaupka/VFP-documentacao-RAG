# Como: definir valores de campo com autoincremento

Você pode configurar campos em tabelas livres e de banco de dados com tipo Integer para incrementar automaticamente.

> **Observação:** O incremento automático de valores de campo não é suportado para views locais, remotas ou offline. Ativar valores com incremento automático em um campo define o campo como somente leitura, e seus valores não podem ser alterados com uma operação insert, update ou replace. Para obter mais informações, consulte Valores de campo com autoincremento em tabelas.

### Para definir valores com incremento automático em um campo
- Abra a tabela no Table Designer.
- Na guia Fields, selecione o campo desejado.
- Na lista Type, selecione Integer (AutoInc).
- Na área AutoIncrement, digite um valor inicial para Next Value e um valor de incremento para Step.
- Quando terminar, clique em OK. Observação Quando você seleciona o tipo Integer (AutoInc) para um campo, a caixa Default value fica indisponível. No entanto, o Visual FoxPro não descarta nem usa o valor padrão. Quaisquer expressões na caixa Default value permanecem quando você altera o tipo do campo para ou de Integer (AutoInc). Você ainda pode usar código como DBGETPROP( ) para recuperar o valor padrão do campo. Se quiser usar o valor na caixa Default value, primeiro altere o tipo de dados Integer (AutoInc).

Para obter mais informações, consulte Fields Tab, Table Designer.

### Para definir valores com incremento automático em um campo programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, inclua a cláusula AUTOINC. -OU-
- Para editar uma tabela existente, abra a tabela com o comando USE e use o comando SQL ALTER TABLE com a cláusula AUTOINC.

Para obter mais informações, consulte CREATE TABLE - SQL Command ou ALTER TABLE - SQL Command.
