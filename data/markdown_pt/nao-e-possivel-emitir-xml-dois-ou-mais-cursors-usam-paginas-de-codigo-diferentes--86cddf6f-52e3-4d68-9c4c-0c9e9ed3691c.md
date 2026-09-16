# Não é possível emitir XML; dois ou mais cursors usam páginas de código diferentes. (Erro 2133)

Ocorre ao tentar chamar o método ToXML de um objeto XMLAdapter quando o método AddTableSchema do objeto XMLAdapter foi usado para adicionar um esquema de dois ou mais cursors que possuem páginas de código diferentes.
 - Verifique se todos os cursors que estão sendo convertidos para XML possuem a mesma página de código.
