# Índices baseados em registros excluídos

Quando registros são marcados para exclusão no Visual FoxPro, eles não são removidos fisicamente até que o comando PACK seja chamado. Portanto, esses registros permanecem visíveis e acessíveis ao realizar operações básicas de tabela, a menos que você defina o comando SET DELETED como ON, o que oculta esses registros das operações básicas.

Para ajudar a garantir que as consultas usem a otimização Rushmore, alguns desenvolvedores criam uma tag de índice para registros excluídos usando a função DELETED( ) na expressão de índice. A função DELETED( ) determina se um registro está marcado para exclusão. Por exemplo, o código a seguir cria um índice chamado Deleted usando uma expressão de índice que inclui a função DELETED( ) que seleciona registros marcados para exclusão:

```foxpro
INDEX ON DELETED() TAG Deleted
```

No entanto, problemas de desempenho ainda podem existir com este método, geralmente ao trabalhar com grandes conjuntos de dados em um ambiente de rede LAN/WAN onde registros excluídos estão dispersos em uma tabela e ao transmitir um índice grande pela rede.

Em vez disso, você pode criar e usar um índice binário, que otimiza o bit que marca registros para exclusão, para melhorar o desempenho quando você define o comando SET DELETED como ON. Você pode criar um índice binário escolhendo o tipo de índice Binary no Table Designer ou incluindo a palavra-chave BINARY no comando INDEX. Por exemplo, o código a seguir cria um índice binário chamado myDeleted que seleciona registros marcados para exclusão:

```foxpro
INDEX ON DELETED() TAG DeletedTag BINARY
```

Para obter mais informações, consulte Visual FoxPro Index Types, DELETED( ) Function e SET DELETED Command.

# Otimização Rushmore para índices baseados em registros excluídos

Para índices baseados em registros excluídos, o Visual FoxPro inclui as seguintes melhorias de otimização Rushmore no mecanismo SQL:
 - INDEX ON NOT(DELETED()) otimiza as condições de consulta NOT(DELETED()) e DELETED(). Em versões anteriores ao Visual FoxPro 9.0, apenas DELETED() era otimizado. Por exemplo, as seguintes consultas agora são otimizadas: CLEAR CLOSE DATABASE ALL SYS(3054,1) CREATE TABLE myTable (f1 I) INDEX ON NOT(DELETED()) TAG NotDel SET DELETED OFF SELECT * FROM myTable WHERE NOT(DELETED()) INTO CURSOR tempCursor SELECT * FROM myTable WHERE DELETED() INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable INTO CURSOR tempCursor INDEX ON DELETED() TAG Del SET DELETED OFF SELECT * FROM myTable WHERE NOT(DELETED()) INTO CURSOR tempCursor SELECT * FROM myTable WHERE DELETED() INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable INTO CURSOR tempCursor CLOSE DATABASE ALL
- INDEX ON ... FOR DELETED( ) ou INDEX ON ... FOR NOT(DELETED()) otimiza as condições de consulta DELETED() ou NOT(DELETED()), respectivamente, quando INDEX ON DELETED() ou INDEX ON NOT(DELETED()) não está presente. Por exemplo, as seguintes consultas agora são otimizadas: CLEAR CLOSE DATABASES ALL SYS(3054,1) CREATE TABLE myTable (f1 I) INDEX ON f1 TAG f1_NotDel FOR NOT(DELETED()) INDEX ON f1 TAG f1_Del FOR DELETED() SET DELETED OFF SELECT * FROM myTable WHERE NOT(DELETED()) INTO CURSOR tempCursor SELECT * FROM myTable WHERE DELETED() INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable INTO CURSOR tempCursor INDEX ON DELETED() TAG DeletedRec SET DELETED OFF SELECT * FROM myTable WHERE NOT(DELETED()) INTO CURSOR tempCursor SELECT * FROM myTable WHERE DELETED() INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable INTO CURSOR tempCursor CLOSE DATABASES ALL
- Quando o Visual FoxPro pode determinar que uma consulta não deve retornar registros excluídos ou não excluídos, e se nenhum índice não filtrado estiver presente, ele usa INDEX ON <expression> ... FOR DELETED() ou INDEX ON <expression> FOR NOT(DELETED()) . Por exemplo, as seguintes consultas agora são otimizadas: CLEAR CLOSE DATABASE ALL SYS(3054,1) CREATE TABLE myTable (f1 I,f2 I) INDEX ON f1 TAG f1_NotDel FOR NOT(DELETED()) INDEX ON f1 TAG f1_Del FOR DELETED() SET DELETED OFF SELECT * FROM myTable WHERE ; (NOT(DELETED()) AND f1>3) OR ; && Tag f1_NotDel used for optimization. (DELETED() AND f1<3) ; && Tag f1_Del used for optimization. INTO CURSOR tempCursor SELECT * FROM myTable WHERE ; (f1>3 AND NOT(DELETED())) OR ; && Not optimized. f1>3 comes first. (f1<3 AND DELETED()) ; && Not optimized. f1<3 comes first. INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable WHERE ; (f1>3000) OR ; && Tag f1_NotDel used for optimization. (f1<1000) ; && Tag f1_NotDel used for optimization. INTO CURSOR tempCursor INDEX ON f1 TAG f1 SET DELETED OFF SELECT * FROM myTable WHERE ; (NOT(DELETED()) AND f1>3) OR ; && Tag f1 used for optimization. (DELETED() AND f1<3) ; && Tag f1 used for optimization. INTO CURSOR tempCursor SET DELETED ON SELECT * FROM myTable WHERE ; (f1>3000) OR ; && Tag f1 used for optimization. (f1<1000) ; && Tag f1 used for optimization. INTO CURSOR tempCursor CLOSE DATABASE ALL
- Se apenas índices com expressões de filtro NOT(DELETED()) são usados para otimização Rushmore e SET DELETED está definido como ON , então a otimização adicional usando NOT(DELETED()) não é realizada, pois é desnecessária.

# Otimizações SQL para funções de agregação MIN( ) e MAX( )

Quando apropriado, o Visual FoxPro usa expressões de filtro `FOR DELETED()` e `FOR NOT(DELETED())` para otimizar as funções de agregação MIN( ) e MAX( ). O Visual FoxPro usa índices filtrados baseados em expressões de índice `DELETED()` quando disponíveis.

Índices filtrados que usam `FOR NOT(DELETED())` podem fornecer otimização adicional com consultas SQL com qualquer configuração de SET DELETED. No entanto, uma tag de índice filtrado com FOR `DELETED()` fornece benefícios apenas quando SET DELETED está definido como OFF.

> **Observação:** Essas otimizações não são baseadas em Rushmore; portanto, não aparecem nos resultados retornados por SYS(3054) - Rushmore Query Optimization Level .

```foxpro
CLEAR
SET SAFETY OFF
CLOSE DATABASE ALL
CREATE TABLE myTable (f1 I)
INDEX ON f1 TAG f1
SET DELETED OFF
SELECT MAX(f1) FROM myTable INTO CURSOR temp1
* tag f1 is used to optimize MAX(f1)
SELECT MAX(f1) FROM myTable WHERE DELETED()INTO CURSOR temp1
* MAX(f1) is not optimized and slow
SET DELETED ON
SELECT MAX(f1) FROM myTable INTO CURSOR temp1
* MAX(f1) is not optimized and slow
SELECT myTable
INDEX ON f1 TAG f1Del FOR DELETED()
INDEX ON f1 TAG f1NotDel FOR NOT(DELETED())
SET DELETED OFF
SELECT MAX(f1) FROM myTable INTO CURSOR temp1
* tag f1 is used to optimize MAX(f1)
SELECT MAX(f1) FROM myTable WHERE DELETED()INTO CURSOR temp1
* tag f1Del is used by  MAX(f1)
SET DELETED ON
SELECT MAX(f1) FROM myTable INTO CURSOR temp1
* tag f1NotDel is used to optimize MAX(f1)
CLOSE DATABASE ALL
```
