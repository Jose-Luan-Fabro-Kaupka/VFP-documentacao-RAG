# Como: exportar uma quantidade ou intervalo de registros

Uma forma de limitar o número de registros é especificar uma quantidade ou intervalo. Com a opção Scope, você pode exportar um único registro ou um grupo posicionado sequencialmente no arquivo.

> **Observação:** O índice ativo e o ponteiro do registro atual afetam os resultados de Next e Rest. Por exemplo, o próximo registro em uma tabela indexada por sobrenome provavelmente será diferente daquele em uma tabela indexada por estado. Isso não afeta Record, pois o número de um registro não muda quando a tabela é indexada.

### Para exportar um número limitado de registros
- No menu File, escolha Export.
- Informe a tabela de origem e o arquivo de destino.
- Escolha Options.
- Escolha Scope.
- Selecione a opção apropriada e preencha a caixa Scope: All exporta todos os registros; Next exporta um intervalo a partir do atual; Record exporta um registro pelo número; Rest exporta o atual e todos os seguintes até o fim.
- Clique em OK. O Visual FoxPro exportará os registros do escopo selecionado.
