# Função IIF( )

Retorna um de dois valores dependendo do valor de uma expressão lógica.

```foxpro
IIF(lExpression, eExpression1, eExpression2)
```

#### Parâmetros
 **lExpression**
Especifica a expressão lógica que IIF( ) avalia.
**eExpression1 , eExpression2**
Se lExpression avaliar como True (.T.), eExpression1 é retornado e eExpression2 não é avaliado. Se lExpression avaliar como False (.F.) ou null (.NULL.), eExpression2 é retornado e eExpression1 não é avaliado.

# Valor de retorno

Caractere, Numérico, Moeda, Data ou DateTime

# Observações

Esta função, também conhecida como IF imediato, avalia uma expressão lógica e retorna uma de duas expressões. Se a expressão lógica avaliar como True (.T.), IIF( ) retorna a primeira expressão. Se a expressão lógica avaliar como False (.F.) ou null (.NULL.), IIF( ) retorna a segunda expressão.

> **Dica:** Esta função pode ser usada no lugar de IF ... ENDIF para expressões condicionais simples, e é especialmente útil em expressões de relatório e etiqueta que especificam condicionalmente o conteúdo de campos. A função IIF( ) também executa mais rapidamente que um IF ... ENDIF equivalente.

# Exemplo

O exemplo a seguir usa IIF( ) para verificar se o campo `notes` na tabela `employee` está vazio. Se estiver vazio, "No description" é exibido; caso contrário, o conteúdo do campo memo é exibido.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee  && Open Employee table
CLEAR
SCAN
   ? IIF(EMPTY(notes), 'No notes', notes)    && Empty memo field?
ENDSCAN
```
