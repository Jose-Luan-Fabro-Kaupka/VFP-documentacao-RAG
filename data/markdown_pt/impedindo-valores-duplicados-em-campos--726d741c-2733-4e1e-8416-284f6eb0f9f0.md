# Impedindo valores duplicados em campos

Você pode impedir valores duplicados em um ou mais campos de tabela criando um índice primário ou candidato usando uma expressão que contenha esses campos. Quando você inclui um ou mais campos em uma expressão de índice, o Visual FoxPro gera uma chave de índice baseada nesses campos para cada registro que identifica unicamente o registro. Quando um registro novo é inserido, você pode comparar as chaves de índice do registro novo e dos registros existentes para determinar se um registro duplicado já existe e impedir que o registro duplicado seja adicionado à tabela.

> **Dica:** Se sua tabela faz parte de um banco de dados, use um índice primário ou candidato. Se sua tabela é uma tabela livre ou já tem um índice primário, você deve usar um índice candidato.

Por exemplo, suponha que você tenha uma tabela que armazena o código de área e o número de telefone em duas colunas. A tabela a seguir ilustra essas duas colunas.

| Código de área | Número de telefone |
| --- | --- |
| 206 | 444-nnnn |
| 206 | 555-nnnn |
| 313 | 444-nnnn |

Tanto a coluna de código de área quanto a coluna de número de telefone contêm valores que duplicam outros valores nas respectivas colunas. No entanto, nenhum número de telefone é duplicado porque a combinação de ambos os campos cria uma linha contendo o número de telefone completo. Da mesma forma, se o índice primário ou candidato incluísse ambos os campos na expressão de índice, as linhas no exemplo não seriam consideradas duplicadas. Portanto, se você tentasse inserir um número de telefone que contivesse exatamente o mesmo código de área e número de telefone que existe em uma das linhas, o Visual FoxPro rejeitaria a entrada como duplicada.
