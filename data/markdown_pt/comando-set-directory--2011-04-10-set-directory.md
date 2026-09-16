# Comando SET DIRECTORY

Especifica a unidade e o diretório padrão.

```foxpro
SET DIRECTORY TO [cPath]
```

#### Parâmetros
**cPath**
Especifica um dos seguintes: um designador de unidade; um designador de unidade com nome de diretório; o nome de um diretório filho; qualquer uma dessas opções usando a notação abreviada do Microsoft MS-DOS ( \ ou ..).

# Observações

SET DIRECTORY altera o diretório padrão para o diretório especificado.

> **Dica:** SET("DIRECTORY") retorna a unidade e o diretório padrão. SYS(5) retorna a unidade padrão. SYS(2003) retorna o diretório padrão sem designador de unidade. SYS(5) + SYS(2003) retorna a unidade e o diretório padrão.
