# Comando SET PATH

Especifica um caminho para pesquisas de arquivos.

```foxpro
SET PATH TO [Path] [ADDITIVE]
```

#### Parâmetros
 **TO [ Path ]**
Especifica os diretórios que o Visual FoxPro deve pesquisar. Use vírgulas ou pontos e vírgulas para separá-los. Observação: o Visual FoxPro não reconhecerá corretamente um caminho se o nome de um disco ou diretório contiver um ponto de exclamação (!). Em todas as plataformas FoxPro, as funções que retornam informações de caminho, como CURDIR( ), DBF( ) e SYS(2003), usam as convenções de nomenclatura de caminhos do Microsoft MS-DOS nos valores retornados.
**ADDITIVE**
Acrescenta caminhos ao final do caminho atual.

# Observações

Emita SET PATH TO sem Path para restaurar o caminho para o diretório padrão. Use SET DEFAULT para especificar o diretório padrão e CURDIR( ) para retornar o diretório padrão atual.

SET PATH não tem escopo limitado à sessão de dados atual; as alterações feitas com SET PATH afetam todas as sessões de dados.

SET PATH é limitado a no máximo 4095 caracteres.

Ao usar ADDITIVE, os caminhos devem ser incluídos como uma cadeia entre aspas ou uma expressão válida. Se usar substituição por macro, ela deve estar corretamente entre aspas, como nos exemplos:

```foxpro
xx = ["Folder2"]
SET PATH TO &xx ADDITIVE
** or **
xx = "Folder2"
SET PATH TO '&xx' ADDITIVE
```
