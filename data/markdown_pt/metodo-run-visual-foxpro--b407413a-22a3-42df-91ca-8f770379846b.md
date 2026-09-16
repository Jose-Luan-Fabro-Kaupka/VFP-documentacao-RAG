# Método Run (Visual FoxPro)

Executa ou visualiza um arquivo em um projeto.

```foxpro
Object.Run()
```

# Observações

Aplica-se a: File Object (Visual FoxPro)

O método Run retorna true (.T.) se o arquivo for executado ou visualizado com sucesso; caso contrário, retorna false (.F.). Etiquetas e relatórios são visualizados pelo método Run.

O evento QueryRunFile ocorre antes de o arquivo ser executado ou visualizado. Se NODEFAULT for especificado no evento QueryRunFile, o arquivo não é executado nem visualizado e o método Run retorna false (.F.). Caso contrário, o arquivo é executado ou visualizado e o método Run retorna true (.T.).

Inclua NODEFAULT no evento QueryRunFile para impedir que um arquivo seja executado ou visualizado.
