# Método Remove (Objeto File)

Remove um arquivo de sua coleção files e do projeto.

```foxpro
Object.Remove()
```

# Observações

Aplica-se a: Objeto File (Visual FoxPro)

O método Remove para objetos file retorna true (.T.) se o arquivo for removido com sucesso do projeto; caso contrário, false (.F.) é retornado. Observe que um aviso não é exibido quando você usa o método Remove para remover arquivos de um projeto, incluindo arquivos que estão sob controle de código-fonte.

O evento QueryRemoveFile ocorre antes que o arquivo seja removido de sua coleção Files e do projeto. Se o evento QueryRemoveFile retornar false (.F.), o arquivo não é removido de sua coleção Files e do projeto e o método Remove retorna false (.F.). Se o método QueryRemoveFile retornar true (.T.), o arquivo é removido de sua coleção Files e do projeto e o método Remove retorna true (.T.).
