# Variável de sistema _PECODE

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Define códigos de impressão de encerramento.

```foxpro
_PECODE = expC
```

# Observações

_PECODE é incluída para compatibilidade com versões anteriores. Use o Report Writer.

_PECODE contém um valor de caractere que é emitido quando ENDPRINTJOB é executado. expC pode conter qualquer coleção de códigos de impressão até um máximo de 255 caracteres. O _PECODE padrão é a cadeia de caracteres nula. Códigos válidos variam de 0 a 255.

Para obter informações completas sobre os efeitos de sequências específicas de códigos de controle, consulte o manual da sua impressora.
