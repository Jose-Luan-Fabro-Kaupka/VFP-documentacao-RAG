# O buffer de tabela ou linha requer que SET MULTILOCKS esteja definido como ON (Erro 1589)

Todos os modos de buffer exigem que o comando SET MULTILOCKS esteja habilitado. Para desabilitar o buffer, defina o buffer como 1 (DB_BUFOFF) usando a função CURSORSETPROP( ).
