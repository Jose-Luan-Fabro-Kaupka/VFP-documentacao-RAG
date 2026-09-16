# Como: filtrar registros em tabelas

Você pode especificar que apenas determinados registros sejam exibidos em janelas de navegação definindo um filtro de dados.

> **Cuidado:** Se você restringir o acesso a todos os campos em uma tabela, pode não conseguir abrir a tabela em uma janela de navegação.

### Para filtrar registros em uma janela de navegação
- Abra a tabela em uma janela de navegação.
- No menu Table, clique em Properties para abrir a caixa de diálogo Work Area Properties.
- Na caixa Data filter, digite a expressão de filtro desejada. Para construir uma expressão, clique no botão de reticências ( ... ).
- Clique em OK . A janela de navegação exibe apenas os registros que atendem à expressão de filtro.

Por exemplo, a seguinte expressão de filtro exibe apenas os registros em uma tabela Customer em que o campo Country está definido como "USA":

```foxpro
Customer.Country = "USA"
```
