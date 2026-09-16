# O resultado é incompatível com o esquema do cursor. (Erro 2074)

Ocorre se o método CursorFill for chamado com o parâmetro lUserCursorSchema definido como True (.T.) e as definições de campo não corresponderem ao tipo ou à precisão dos campos na tabela base.
 - Certifique-se de que os tipos e as precisões dos campos correspondam à tabela base.
- O parâmetro lUserCursorSchema deve ser usado somente se necessário, como ao converter XML que não tem um esquema e você precisa controlar os tipos de campo.
