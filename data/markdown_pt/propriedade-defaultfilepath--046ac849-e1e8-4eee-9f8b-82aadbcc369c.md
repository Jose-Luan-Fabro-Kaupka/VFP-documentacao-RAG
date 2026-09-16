# Propriedade DefaultFilePath

Especifica a unidade e o diretório padrão usados por um objeto Application. Disponível em tempo de execução.

```foxpro
ApplicationObject.DefaultFilePath[ = cPath]
```

# Valor de retorno
 **cPath**
Especifica uma destas opções: um designador de unidade; um designador de unidade com nome de diretório; um nome de diretório filho; qualquer uma das opções anteriores usando a notação abreviada do MS-DOS® ( \ ou ..).

# Observações

Aplica-se a: objeto Application | variável de sistema _VFP

A propriedade DefaultFilePath é semelhante a SET DEFAULT.

O Visual FoxPro pesquisa um arquivo no diretório padrão, que inicialmente é aquele de onde o Visual FoxPro foi iniciado. Você pode usar DefaultFilePath para especificar outro diretório. Se o arquivo não for encontrado no diretório padrão, o Visual FoxPro pesquisará no caminho configurado, se houver. Use SET PATH para especificar esse caminho.
