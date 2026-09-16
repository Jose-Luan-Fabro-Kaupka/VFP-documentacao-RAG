# Campos general não podem ser usados na condição WHERE de uma instrução de atualização. Altere a propriedade WhereType da view (Erro 1489)

Na cláusula WHERE de uma instrução de atualização SQL, as expressões que você usa para impor bloqueio otimista não podem incluir campos general. Use a propriedade WhereType da view (você pode alterá-la do padrão KeyAndModified para Key) para remover campos general da cláusula WHERE de atualização.

Para obter mais informações sobre a propriedade WhereType, consulte CURSORGETPROP( ) Function ou DBGETPROP( ) Function.
