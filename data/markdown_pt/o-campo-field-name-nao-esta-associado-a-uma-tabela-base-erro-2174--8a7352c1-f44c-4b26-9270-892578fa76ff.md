# O campo "field name" não está associado a uma tabela base (Erro 2174)

Este erro é gerado pela Classe CursorAdapter quando ela tenta busca de memo atrasada. A tabela base é especificada com a Propriedade Tables do CursorAdapter. O campo memo deve ser associado à tabela base com a Propriedade UpdateNameList do CursorAdapter.
