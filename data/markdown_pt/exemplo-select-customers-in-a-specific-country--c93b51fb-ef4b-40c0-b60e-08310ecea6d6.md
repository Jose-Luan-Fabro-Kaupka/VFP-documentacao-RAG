# Exemplo Select Customers in a Specific Country

Arquivo: ...\Samples\Data\Testdata.dbc

Este exemplo ilustra o uso de uma view parametrizada ("customers in specific country" no banco de dados testdata) para exibir um subconjunto de registros que correspondem a uma variável definida em tempo de execução.

Para criar uma view parametrizada no View Designer, digite uma variável prefixada com ponto de interrogação (?) na caixa Example da guia Filter.

Se a variável não existir em tempo de execução, o usuário é solicitado a digitar um valor para a variável, `whichcountry` neste exemplo. Se a variável já existir, a view exibe os registros correspondentes sem solicitar um novo valor.
