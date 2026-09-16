# Função DRIVETYPE( )

Retorna o tipo da unidade especificada.

```foxpro
DRIVETYPE(cDrive)
```

#### Parâmetros
**cDrive**
O designador da unidade. Os dois-pontos nos nomes de unidade (por exemplo, "C:") são opcionais.

# Valor de retorno

Numérico

# Observações

A tabela a seguir explica o número retornado por DRIVETYPE( ) e a descrição do tipo de unidade correspondente.

| Número | Tipo de unidade |
| --- | --- |
| 1 | Sem tipo |
| 2 | Disquete |
| 3 | Disco rígido |
| 4 | Unidade removível ou unidade de rede |
| 5 | CD-ROM |
| 6 | Disco RAM1 |

1 Como há muitos tipos diferentes de discos RAM, os resultados retornados podem ser inconsistentes.
