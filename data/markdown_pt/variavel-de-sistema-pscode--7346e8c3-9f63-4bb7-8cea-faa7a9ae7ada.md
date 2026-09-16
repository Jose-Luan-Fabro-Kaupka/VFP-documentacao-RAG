# Variável de sistema _PSCODE

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Define códigos de impressão iniciais.

```foxpro
_PSCODE = expC
```

# Observações

_PSCODE é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PSCODE contém um valor de caractere que é emitido quando PRINTJOB é executado. expC pode conter qualquer coleção de códigos de impressão de até 255 caracteres; o padrão é a cadeia de caracteres nula. Códigos válidos variam de 0 a 255.

Para obter informações completas sobre o efeito de sequências específicas de código de controle, consulte o manual da sua impressora.
