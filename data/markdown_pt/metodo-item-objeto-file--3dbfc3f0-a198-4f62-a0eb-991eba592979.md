# Método Item (objeto File)

Retorna uma referência de objeto a um arquivo, projeto ou servidor especificado em uma coleção files, projects ou servers.

```foxpro
Object.Item(nIndex)
```

# Observações
 **nIndex**
Um número que especifica um arquivo, projeto ou servidor em uma coleção files, projects ou servers. Um erro "Invalid subscript reference" é gerado se nIndex for maior que o número de arquivos, projetos ou servidores em uma coleção.

# Observações

Aplica-se a: Files Collection (Visual FoxPro) | Projects Collection (Visual FoxPro) | Servers Collection

Use a propriedade Name (Visual FoxPro) com a propriedade Item para determinar o nome de um arquivo, projeto ou servidor e o diretório no qual ele está contido.
