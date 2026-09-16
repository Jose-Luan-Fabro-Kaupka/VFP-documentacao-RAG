# SYS(2005) - Arquivo de recursos atual

Retorna o nome do arquivo de recursos atual do Visual FoxPro.

```foxpro
SYS(2005)
```

# Valor de retorno

Character

# Observações

O arquivo de recursos do Visual FoxPro é uma tabela Visual FoxPro que contém informações sobre recursos do sistema e definidos pelo usuário, como macros de teclado, preferências, localizações e tamanhos de janelas do sistema, entradas de diário e assim por diante.

O arquivo de recursos do Visual FoxPro usa FoxUser.dbf por padrão. Use SET RESOURCE para especificar um arquivo de recursos Visual FoxPro diferente.

# Exemplo

```foxpro
? 'Current resource file: ', SYS(2005)
```
