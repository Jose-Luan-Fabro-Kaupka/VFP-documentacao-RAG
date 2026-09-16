# Comando SET DEFAULT

Especifica a unidade e o diretório padrão.

```foxpro
SET DEFAULT TO [cPath]
```

#### Parâmetros
 **cPath**
Especifica um dos seguintes: Um designador de unidade Um designador de unidade com um nome de diretório Um nome de diretório filho Qualquer um dos itens acima usando a notação abreviada do Microsoft MS-DOS ( \ ou ..)

# Observações

SET DEFAULT altera o diretório padrão para o diretório que você especificar.

O Microsoft® Visual FoxPro® procura um arquivo no diretório padrão do Visual FoxPro. O diretório padrão é aquele a partir do qual você inicia o Visual FoxPro. No entanto, você pode especificar um diretório padrão diferente no arquivo de configuração do Visual FoxPro ou em um programa de inicialização. Se o Visual FoxPro não encontrar um arquivo no diretório padrão, ele então procura no caminho do Visual FoxPro, se um foi especificado. Use SET PATH para especificar o caminho do Visual FoxPro.

Se você criar um arquivo e não especificar onde colocá-lo, o arquivo é colocado no diretório padrão do Visual FoxPro.

O comando SET DEFAULT não é suportado em servidores DLL de thread única ou multithread. Esse comando altera o diretório padrão de todo o processo, de modo que todas as threads que fazem parte do processo são afetadas. Use o Comando SET PATH em servidores DLL, no lugar de CD e CHDIR.

> **Dica:** SYS(5) retorna a unidade padrão. SYS(2003) retorna o diretório padrão sem designador de unidade. SYS(5) + SYS(2003) retorna a unidade e o diretório padrão.

Você pode alterar a unidade padrão para a unidade A usando um dos seguintes comandos:

```foxpro
SET DEFAULT TO A
SET DEFAULT TO A:
```

Você pode especificar um diretório específico:

```foxpro
SET DEFAULT TO A:\sales
SET DEFAULT TO C:\sales\data
```

Você pode especificar um diretório filho. Se o diretório raiz na unidade C é o diretório padrão do Visual FoxPro, emita o seguinte comando para alterar o diretório padrão para C:\Sales:

```foxpro
SET DEFAULT TO sales
```

Você pode usar a notação abreviada do MS-DOS. Se o diretório atual é C:\Sales\Data, emita o seguinte comando para tornar o diretório raiz o diretório padrão:

```foxpro
SET DEFAULT TO \
```

Você também pode mover o diretório padrão um diretório em direção ao diretório raiz com o seguinte comando:

```foxpro
SET DEFAULT TO ..
```
