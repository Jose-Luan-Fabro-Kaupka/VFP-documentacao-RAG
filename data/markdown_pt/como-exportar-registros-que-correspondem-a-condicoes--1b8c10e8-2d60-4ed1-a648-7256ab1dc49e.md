# Como: exportar registros que correspondem a condições

Se os registros que você deseja exportar não forem sequenciais na tabela, poderá criar uma expressão lógica que especifique os critérios de seleção que um registro deve atender para ser exportado. Por exemplo, você pode optar por exportar todos os registros que tenham determinado valor em um campo.

### Para inserir critérios de exportação de registros
- No menu File, escolha Export.
- Informe a tabela de origem e o arquivo de destino.
- Escolha Options.
- Escolha For para criar uma expressão na caixa de diálogo Expression Builder. Observação: não é necessário incluir o comando FOR na expressão. Por exemplo, digite customer.country = "Canada" para exportar somente dados canadenses.
- Escolha OK. O Visual FoxPro avalia todos os registros e exporta aqueles que correspondem à condição da expressão.
