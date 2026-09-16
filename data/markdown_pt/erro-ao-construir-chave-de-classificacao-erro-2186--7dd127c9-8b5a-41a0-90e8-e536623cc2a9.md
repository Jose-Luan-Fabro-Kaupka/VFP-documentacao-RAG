# Erro ao construir chave de classificação (Erro 2186)

Este erro é gerado quando o truncamento da chave de classificação está prestes a ocorrer, tipicamente durante GROUP BY, ORDER BY ou outras operações de classificação. Isso pode acontecer com o uso de uma chave de classificação que contém uma expressão, como um campo Memo, cujo comprimento não é fixo.
