# Comportamento de valores nulos em comandos e funções

A tabela a seguir descreve como comandos e funções interpretam valores nulos.

| Tipo de dados | Comportamento |
| --- | --- |
| Logical | A maioria das expressões lógicas que resultam em .NULL. retorna .NULL. ou gera um erro. EMPTY( ) , ISBLANK( ) e ISNULL( ) são exceções. |
| Numeric | Expressões numéricas que resultam em .NULL. retornam .NULL. Uma função numérica resulta em .NULL. quando recebe um valor nulo. |
| Date | Expressões de data que contêm valores nulos retornam .NULL. |
