# Os objetos CursorAdapter e XMLTable não pertencem à mesma sessão de dados. (Erro 2125)

Ocorre quando um objeto CursorAdapter e um XMLTable são criados em sessões de dados diferentes.
 - Certifique-se de que o objeto CursorAdapter e o XMLTable sejam criados na mesma sessão de dados antes de serem usados juntos.
