# Comando SET TYPEAHEAD

Especifica o número máximo de caracteres que podem ser armazenados no buffer de type-ahead.

```foxpro
SET TYPEAHEAD TO nCharacters
```

#### Parâmetros
 **nCharacters**
Especifica o número máximo de caracteres a armazenar no buffer de type-ahead. Nenhum caractere é mantido no buffer de type-ahead se você emitir SET TYPEAHEAD TO 0. Esta instrução desativa INKEY( ) e ON KEY.

# Observações

O buffer de type-ahead pode armazenar até 32.000 caracteres até que estejam prontos para serem processados. O valor padrão de SET TYPEAHEAD é 20.
