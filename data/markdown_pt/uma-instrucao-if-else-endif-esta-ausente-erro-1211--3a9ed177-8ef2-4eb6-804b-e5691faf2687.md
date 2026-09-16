# Uma instrução IF | ELSE | ENDIF está ausente (Erro 1211)

Uma parte da instrução está ausente ou mal posicionada. Verifique o uso incorreto de IF … ENDIF dentro de outra instrução de controle.

O exemplo a seguir falha porque ENDIF está posicionado dentro da instrução DO CASE....ENDCASE.

`IF .T.`

`DO CASE`

`CASE .T.`

`ENDIF`

`ENDCASE`

Para obter mais informações sobre a execução condicional de comandos, consulte o comando IF ... ENDIF.
