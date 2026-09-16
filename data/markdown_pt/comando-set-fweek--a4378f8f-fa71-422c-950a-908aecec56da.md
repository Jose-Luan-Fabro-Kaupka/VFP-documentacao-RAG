# Comando SET FWEEK

Especifica os requisitos para a primeira semana do ano.

```foxpro
SET FWEEK TO [nExpression]
```

#### Parâmetros
 **nExpression**
Especifica um valor que determina os requisitos para a primeira semana do ano. A tabela a seguir lista os valores que nExpression pode assumir e os requisitos correspondentes para a primeira semana do ano: nExpression Requisito da primeira semana 1 (Padrão) A primeira semana contém 1 de janeiro. 2 A maior metade (quatro dias) da primeira semana está no ano atual. 3 A primeira semana tem sete dias. Se você omitir nExpression , a primeira semana do ano é redefinida para 1 (a primeira semana contém 1 de janeiro).

# Observações

A primeira semana do ano também pode ser definida com a caixa de listagem First Week of Year na guia Regional da caixa de diálogo Options.

# Exemplo

```foxpro
STORE SET('FWEEK') TO gnFweek  && Save current value
SET FWEEK TO 1  && First week contains January 1st
SET FWEEK TO 3  && First week has seven days
SET FWEEK TO &gnFweek  && Restore original setting
```
