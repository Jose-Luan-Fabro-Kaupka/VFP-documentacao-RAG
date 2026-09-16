# SQL: cláusula ORDER BY inválida (Erro 1808)

Um dos campos escolhidos para a cláusula ORDER BY não está na lista SELECT. Isso ocorre apenas ao usar indexação numérica, como no exemplo a seguir, em que o número escolhido excede o número de campos selecionados:

```foxpro
SELECT a,b,c FROM table ORDER BY 4
```

Este erro também será gerado se você incluir um campo do tipo Blob na cláusula ORDER BY.

Para obter mais informações, consulte Comando SELECT - SQL.
