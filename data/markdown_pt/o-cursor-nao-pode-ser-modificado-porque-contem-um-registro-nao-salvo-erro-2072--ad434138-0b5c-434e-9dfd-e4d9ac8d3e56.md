# O cursor não pode ser modificado porque contém um registro não salvo (Erro 2072)

Este erro geralmente ocorre quando um registro em um cursor é modificado em um grid ou janela Browse e não é salvo antes de mover para outro registro.

Qualquer código que modifica o cursor deve garantir que todas as modificações sejam salvas antes de mover o ponteiro de registro.
