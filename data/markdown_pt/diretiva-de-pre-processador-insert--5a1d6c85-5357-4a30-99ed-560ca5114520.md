# Diretiva de pré-processador #INSERT

Coloca texto de um arquivo de texto em um arquivo de menu gerado.

```foxpro
#INSERT FileName
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo de cabeçalho que é mesclado no programa durante a geração do menu.

# Observações

A diretiva de gerador de menu #INSERT insere o conteúdo de FileName no código de menu gerado.

Use #INSERT para incluir um arquivo em um programa de menu gerado. Por exemplo, use #INSERT para colocar instruções #DEFINE ... #UNDEF de um arquivo no início de um programa de menu gerado.

Esta diretiva pode aparecer em qualquer procedimento; não precisa estar em um procedimento específico, como o código de configuração. Além disso, a diretiva pode aparecer em qualquer lugar de um procedimento.

FileName deve ser um arquivo de texto. O gerador procura o arquivo no diretório atual, no diretório FoxPro e subdiretórios e ao longo do caminho MS-DOS. Se o arquivo não puder ser encontrado, o gerador de menu comenta seu código — indicando que o arquivo não pôde ser encontrado — e continua o processo de geração.
