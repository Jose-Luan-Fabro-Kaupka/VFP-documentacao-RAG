# SYS(20) - Transformar texto alemão

Incluído para compatibilidade com versões anteriores. Use o comando SET COLLATE em vez disso.

Transforma uma expressão de caractere contendo texto alemão em uma cadeia de caracteres.

```foxpro
SYS(20, expC, expN)
```

# Valor de retorno

Valor de retorno - Character

# Observações

SYS(20) é usado para ordenar campos contendo palavras e nomes alemães. Os campos são ordenados para se assemelhar à ordenação em uma lista telefônica alemã — maiúsculas e minúsculas são intercaladas, eszets são classificados imediatamente após duplo s, e caracteres com trema são classificados imediatamente após o caractere sem adorno seguido da letra e.

SYS(15) também pode ser usado para indexar e classificar campos que contêm marcas diacríticas.

SYS(20) transforma a expressão de caractere expC. A expressão numérica expN especifica o número de caracteres em expC a transformar, começando com o primeiro caractere em expC. Quaisquer caracteres adicionais após a posição especificada por expN são ignorados. O comprimento da cadeia de caracteres retornada por SYS(20) é 2 * expN + 10 caracteres, com comprimento máximo de 254 caracteres.

# Exemplo

No exemplo a seguir, o campo CONTACT contém os nomes dos clientes. Este campo é indexado usando SYS(20) e os primeiros 20 caracteres no campo. Uma tag de índice estrutural chamada GCONTACT é criada.

```foxpro
USE CUSTOMER
INDEX ON SYS(20, contact, 20) TAG gcontact
```
