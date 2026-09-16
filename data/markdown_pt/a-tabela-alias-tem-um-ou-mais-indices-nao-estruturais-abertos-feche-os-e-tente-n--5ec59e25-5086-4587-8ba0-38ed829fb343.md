# A tabela "alias" tem um ou mais índices não estruturais abertos. Feche-os e tente novamente o Begin Transaction (Erro 1548)

Feche todos os índices não estruturais (não-.CDX) e tente a operação novamente.

Se outros índices estiverem abertos no arquivo, suas gravações irão diretamente para o disco e não serão refletidas nas alterações da tabela até que você emita o END TRANSACTION Command. Consequentemente, se um ROLLBACK Command for emitido, os índices não estruturais ficarão incorretos.
