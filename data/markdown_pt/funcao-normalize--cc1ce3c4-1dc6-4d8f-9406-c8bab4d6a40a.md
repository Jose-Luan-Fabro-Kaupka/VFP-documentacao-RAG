# Função NORMALIZE( )

Converte uma expressão, fornecida por um usuário, na mesma forma da expressão usada internamente pelo Visual FoxPro. Você pode usar a forma normalizada de uma expressão para fazer comparações mais precisas com as expressões retornadas por comandos ou funções do Visual FoxPro.

```foxpro
NORMALIZE(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere a normalizar.

# Valor de retorno

Caractere

# Observações

NORMALIZE( ) retorna uma cadeia de caracteres da expressão de caractere cExpression com as seguintes alterações. NORMALIZE( ):
 - Converte a expressão de caractere para maiúsculas. No entanto, não altera cadeias de caracteres incorporadas. Um exemplo de cadeia de caracteres incorporada é "Hello" na expressão de caractere "LEFT('Hello',1)".
- Expande quaisquer palavras-chave abreviadas do Visual FoxPro na expressão de caractere para seu comprimento total.
- Converte em pontos quaisquer operadores -> que separam aliases de nomes de campos.
- Cerca com pontos os operadores lógicos AND, OR e NOT: .AND. .OR. .NOT.
- Em expressões de filtro, remove quaisquer espaços em branco entre termos.
- Verifica a sintaxe de quaisquer comandos ou funções do Visual FoxPro na expressão de caractere. No entanto, não avalia a expressão. Se a sintaxe estiver incorreta, o Visual FoxPro gera um erro de sintaxe. NORMALIZE( ) não procura campos, tabelas, variáveis de memória, funções definidas pelo usuário ou outras referências na expressão de caractere.

Por exemplo, um usuário pode inserir uma expressão de índice como a seguinte no Expression Builder:

```foxpro
UPPE(cust->lname) + UPPE(cust->fname)
```

Embora esta seja uma expressão de chave de índice válida do Visual FoxPro, é difícil compará-la aos valores de retorno de uma função do Visual FoxPro como KEY( ). NORMALIZE( ) retorna a seguinte cadeia de caracteres para a expressão acima:

```foxpro
UPPER(CUST.LNAME) + UPPER(CUST.FNAME)
```

Você pode comparar facilmente isso ao valor retornado por uma função como KEY( ). Isso permite verificar a existência de um índice ou tag de índice com a expressão de índice fornecida pelo usuário.

Além disso, você pode usar NORMALIZE para comparar os resultados de SET("Filter") ou FILTER( ). Por exemplo, você poderia criar a seguinte expressão de filtro:

```foxpro
STORE '"VIRGINIA" $ UPPER(state) AND NOT "MAINE" $ UPPER(state)' TO
MyFilter
USE Addresses
 LINK Word.Document.8 "C:\\Documents and Settings\\v-rodhil\\My Documents\\DocStudio\\Projects\\dv_foxhelp91\\cc1ce3c4-1dc6-4d8f-9406-c8bab4d6a40a.xml" "OLE_LINK1" \a \r  \* MERGEFORMAT STORE '"VIRGINIA" $ UPPER(state) AND NOT "MAINE" $ UPPER(state)' TO
MyFilter
SET FILTER TO &MyFilter
```

No entanto, o valor retornado por SET("Filter") ou FILTER( ) não corresponderá exatamente ao filtro original.

```foxpro
? SET("FILTER") == MyFilter  && .F.
```

SET("Filter") ou FILTER( ) retornam o seguinte:

```foxpro
"VIRGINIA"$UPPER(STATE).AND..NOT."MAINE"$UPPER(STATE)
```

Para garantir uma comparação correta, use:

```foxpro
? NORMALIZE(MyFilter) == SET("FILTER")  && .T."
```
