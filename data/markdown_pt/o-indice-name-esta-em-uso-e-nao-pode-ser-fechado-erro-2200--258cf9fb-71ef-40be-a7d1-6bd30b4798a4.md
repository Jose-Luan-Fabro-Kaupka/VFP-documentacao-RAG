# O índice "name" está em uso e não pode ser fechado (Erro 2200)

Este erro é gerado pelo mecanismo SQL quando há uma tentativa de fechar uma tag de índice enquanto ela está em uso. O erro pode ocorrer se você tentar excluir uma tag em uso, por exemplo, a partir de uma UDF() chamada por um Comando SELECT - SQL.
