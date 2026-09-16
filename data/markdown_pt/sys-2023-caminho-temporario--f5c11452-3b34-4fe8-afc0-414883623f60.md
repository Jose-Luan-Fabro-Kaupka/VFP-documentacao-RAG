# SYS(2023) - Caminho temporário

Retorna o caminho no qual o Visual FoxPro armazena seus arquivos temporários.

```foxpro
SYS(2023)
```

# Valor de retorno

Character. SYS(2023) retorna um nome de caminho.

# Observações

SYS(2023) usa a API do Windows GetTempPath para pesquisar o caminho que contém os arquivos temporários. GetTempPath pesquisa uma sequência de variáveis que diferem dependendo do sistema operacional. Para obter mais informações, consulte Otimizando o ambiente operacional.
