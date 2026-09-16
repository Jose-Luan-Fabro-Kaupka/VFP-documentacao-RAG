# Entender ordens de classificação

Ordens de classificação incorporam as regras de classificação de diferentes localidades, permitindo classificar dados nesses idiomas corretamente. No Visual FoxPro, a ordem de classificação atual determina os resultados de comparações de expressões de caractere e a ordem em que os registros aparecem em tabelas indexadas ou classificadas.

> **Observação:** A classificação funciona de forma diferente em ambientes de conjuntos de caracteres de byte duplo (DBCS).

Use a ordem de classificação apropriada, porque ordens de classificação diferentes produzem resultados diferentes, conforme mostrado na tabela a seguir.

| Unsorted | Machine | General | Spanish |
| --- | --- | --- | --- |
| !@#$ | Space | space | Space |
| 1234 | !@#$ | !@#$ | !@#$ |
| space | 1234 | 1234 | 1234 |
| Caesar | Caesar | a | a |
| csar | Car | ab | Ab |
| Strasse | Char | b | b |
| strae | Czech | Caesar | Caesar |
| Car | Strasse | csar | Csar |
| Char | Ab | Car | Car |
| Czech | Csar | ar | ar |
| ab | Strae | Char | Czech |
| ar | ar | Czech | Char |
| a | a | Strasse | Strasse |
| b | b | strae | Strae |

# Diretrizes de ordem de classificação

Considere as diretrizes a seguir ao escolher uma ordem de classificação:
 - Evite a ordem de classificação Machine se deseja classificar caracteres internacionais corretamente, porque Machine classifica caracteres internacionais em ordem ASCII. Por exemplo, observe que ar segue strae .
- Caracteres com marcas diacríticas classificam de forma diferente dos caracteres sem marcas diacríticas. Por exemplo, nas ordens de classificação General e Spanish, observe que a classifica antes de ab, mas ab classifica antes de b .
- Ligaduras como classificam da mesma forma que suas expansões de caractere equivalentes. Por exemplo, strae classifica da mesma forma que Strasse , e csar classifica da mesma forma que Caesar .
- Em alguns idiomas, dois caracteres classificam como um único caractere. Por exemplo, em espanhol o Ch em Char classifica como um caractere entre C e D .

As seções a seguir descrevem como especificar ordens de classificação, verificar a ordem de classificação atual e reconhecer os efeitos das ordens de classificação.

# Verificando ordens de classificação

Você pode determinar a ordem de classificação atual usando a função SET( ) Function. Por exemplo, você pode salvar a ordem de classificação atual, definir a ordem de classificação atual como Machine, executar o trabalho necessário e depois restaurar a ordem de classificação original usando o código a seguir:

```foxpro
cCurrentOrder=SET('COLLATE')
SET COLLATE TO 'MACHINE'
*
* code that requires the Machine sort order
*
SET COLLATE TO cCurrentOrder  && return to the previous sort order
```

Você também pode determinar a ordem de classificação de um índice ou tag de índice usando a função IDXCOLLATE( ) Function.

# Reconhecendo os efeitos das ordens de classificação

A ordem de classificação afeta os resultados de comparações de cadeias de caracteres, Comando SEEK e Comando SELECT - SQL, conforme descrito nas seções a seguir.

### Comparando cadeias de caracteres

Todas as ordens de classificação, exceto Machine e Unique Weight, ignoram maiúsculas e minúsculas. Isso significa que você não precisa usar UPPER( ) Function em suas expressões de índice.

A ordem de classificação atual afeta comparações de cadeias de caracteres. Por exemplo, quando você define a ordem de classificação como General, as instruções a seguir retornam True (.T.):

```foxpro
?"A" = "a"
?"Strae"="Strasse"
?"" = "ae"
```

No entanto, quando você usa a ordem de classificação Machine, todas essas instruções retornam False (.F.). porque as cadeias são comparadas para uma comparação exata, byte a byte.

O operador de comparação de cadeia de caracteres (= =) fornece o mesmo resultado que quando você compara por valor ou quando compara usando a ordem de classificação Machine; ou seja, compara cadeias byte a byte. Por exemplo, a instrução a seguir retorna False (.F.):

```foxpro
? "Strae" == "Strasse"
```

> **Observação:** O Visual FoxPro ignora SET EXACT quando você usa o operador de comparação de cadeia de caracteres (= =).

### Usando SEEK

O Visual FoxPro ignora marcas diacríticas quando você executa uma busca parcial. Uma busca parcial ocorre quando você torna o comprimento da expressão menor que o comprimento da chave. Se diacríticos são importantes, considere usar os comandos SCAN ... ENDSCAN Command ou LOCATE Command em vez do Comando SEEK.

As vantagens de usar SCAN e LOCATE em vez de SEEK incluem o seguinte:
 - SCAN e LOCATE são sensíveis a diacríticos.
- O Visual FoxPro otimiza totalmente os resultados de SCAN ou LOCATE se a ordem de classificação atual é Machine ou Unique Weight, enquanto o Visual FoxPro otimiza apenas parcialmente os resultados de SEEK.
- SCAN e LOCATE lembram a condição que os invocou, permitindo usá-los para iterar em uma condição. Em contraste, SEEK posiciona você em algum lugar no índice, e SKIP continua pelo índice a partir desse ponto. Consequentemente, SEEK pode não produzir os resultados que você deseja com dados internacionais.

### Usando SELECT - SQL

O comando SELECT - SQL Command usa a ordem de classificação atual. Por exemplo, se você tem uma tag de índice baseada na ordem de classificação General e a ordem de classificação atual (retornada por SET( ) Function) é Machine, o resultado do SELECT SQL é baseado em Machine.

Para empregar a ordem de classificação atual, use a cláusula ORDER BY do SELECT - SQL.

# Usando índices

Ordens de classificação determinam a ordem dos registros em tabelas indexadas. Considere as diretrizes a seguir para usar índices com ordens de classificação:
 - Reconstrua índices criados em versões anteriores do FoxPro se deseja que os índices usem uma ordem de classificação diferente de Machine.
- Reconstrua índices dBASE para aproveitar as ordens de classificação do Visual FoxPro.
- Use o comando REINDEX para reconstruir um índice, porque REINDEX mantém a ordem de classificação inalterada.
