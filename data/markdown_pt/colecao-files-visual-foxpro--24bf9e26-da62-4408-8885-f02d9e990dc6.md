# Coleção Files (Visual FoxPro)

Uma coleção de objetos de arquivo em um projeto.

```foxpro
Files
```

# Observações

A coleção files consiste em todos os arquivos de um projeto. Cada arquivo é um objeto que pode ser manipulado com as propriedades e métodos do objeto de arquivo.

Arquivos em uma coleção de arquivos podem ser referenciados por número de índice ou por nome. Por exemplo, o código a seguir abre o arquivo que foi adicionado primeiro a um projeto:

```foxpro
_VFP.ActiveProject.Files(1).Modify()
```

O código a seguir abre uma janela de edição para Main.prg:

```foxpro
_VFP.ActiveProject.Files('Main.prg').Modify()
```

Observe que não é necessário incluir o caminho com um nome de arquivo.

Para obter mais informações sobre a coleção files e projetos, consulte Project Manager Hooks em Development Productivity Tools.
