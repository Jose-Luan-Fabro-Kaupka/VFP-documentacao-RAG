# Função ISMEMOFETCHED( )

Determina se um campo memo foi buscado durante uma busca de memo adiada.

```foxpro
ISMEMOFETCHED(cFieldName | nFieldNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **cFieldName**
Especifica o nome do campo memo para o qual o status de busca é retornado.
**nFieldNumber**
Especifica o número do campo (baseado na estrutura física da tabela ou cursor) do campo memo para o qual o status de busca é retornado.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor que contém o campo memo para o qual o status de busca é retornado.
**cTableAlias**
Especifica o alias da tabela ou cursor que contém o campo memo para o qual o status de busca é retornado.

# Valor de retorno

Logical. Um true lógico (.T.) é retornado se o campo memo especificado foi buscado; caso contrário, um false lógico (.F.) é retornado. True (.T.) é sempre retornado para dados locais. O valor nulo (.NULL.) é retornado para um cursor se o ponteiro de registro estiver posicionado no início ou no final do cursor. Use a função BOF( ) e a função EOF( ) para determinar se o ponteiro de registro está posicionado no início ou no final do cursor.

# Observações

Muitas vezes pode levar um tempo para que uma busca de campo memo ocorra com dados remotos, então você pode optar por não baixar um campo memo até que seja absolutamente necessário.

A configuração FetchMemo nas funções DBGETPROP( ) e CURSORGETPROP( ) determina se um campo memo é recuperado com os resultados da view ou sob demanda. ISMEMOFETCHED( ) retorna true (.T.) quando o campo memo é buscado para dados Memo adiados (FetchMemo=.F.).

ISMEMOFETCHED( ) funciona com campos memo e general.
