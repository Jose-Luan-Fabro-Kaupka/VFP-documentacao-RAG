# Método Modify

Abre um arquivo em um projeto para modificação no designer ou editor apropriado.

```foxpro
Object.Modify([cClassName])
```

#### Parâmetros
 **cClassName**
Especifica o nome da classe visual a ser aberta para modificação quando Object é uma biblioteca de classes visuais .vcx.

# Observações

Aplica-se a: objeto File (Visual FoxPro)

O método Modify retorna true (.T.) se o arquivo for aberto com sucesso para modificação; caso contrário, false (.F.) é retornado.

O evento QueryModifyFile ocorre antes do arquivo ser aberto. Se o evento QueryModifyFile retornar false (.F.), o arquivo não é aberto e o método Modify retorna false (.F.). Se o método QueryModifyFile retornar true (.T.), o arquivo é aberto e o método Modify retorna true (.T.).
