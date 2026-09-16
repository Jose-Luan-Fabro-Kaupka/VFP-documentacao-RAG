# Variável de sistema _MLINE

Contém o deslocamento do campo memo para a função MLINE( ).

```foxpro
_MLINE = nNumberOfCharacters
```

#### Parâmetros
**nNumberOfCharacters**
Especifica o deslocamento do campo memo. Para obter mais informações sobre o uso de _MLINE e um exemplo, consulte MLINE( ).

# Observações

MLINE( ) retorna uma linha de texto de um campo memo. MLINE( ) armazena o local do deslocamento do campo memo na variável de sistema _MLINE. Use _MLINE como o segundo argumento numérico da função MLINE( ) para melhorar o desempenho de MLINE( ).

O valor padrão de inicialização de _MLINE é 0. Redefina _MLINE como 0 antes de usá-la novamente com a função MLINE( ).
