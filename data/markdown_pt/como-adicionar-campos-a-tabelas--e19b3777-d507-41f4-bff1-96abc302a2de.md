# Como: adicionar campos a tabelas

Ao abrir a tabela no Table Designer, a guia Fields exibe uma linha para o primeiro campo e adiciona um campo após o campo conforme você o define. Você pode adicionar campos adicionais à tabela na ordem desejada.

### Para adicionar um campo a uma tabela
- Abra a tabela no Table Designer .
- Na guia Fields, insira o cursor no campo que segue o que você deseja adicionar.
- Clique em Insert . Um novo campo aparece antes do campo selecionado com um nome, tipo e largura de campo padrão.
- Altere os atributos do campo para os desejados.
- Quando terminar, clique em OK . O Visual FoxPro solicita que você confirme as alterações na estrutura da tabela.
- Para confirmar as alterações na estrutura da tabela, clique em Yes .

### Para adicionar um campo a uma tabela programaticamente
- Use o comando SQL ALTER TABLE e inclua a cláusula ADD COLUMN.

Para obter mais informações, consulte Comando ALTER TABLE - SQL.

Por exemplo, o código a seguir adiciona um campo chamado Fax com tipo Character e largura de campo de 10 caracteres a uma tabela de clientes:

```foxpro
ALTER TABLE Customer ADD COLUMN Fax C(20)
```
