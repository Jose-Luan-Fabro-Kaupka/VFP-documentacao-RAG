# Convenções de nomenclatura de variáveis

Ao nomear variáveis, use o seguinte formato recomendado.

```foxpro
[Scope]TypeVariableName
```

#### Parâmetros
 **[ Scope ]**
Especifica um caractere que indica o escopo de referência da variável. A tabela a seguir lista os valores sugeridos para Scope . Scope Descrição l Local t Parameter g Public (Global) p Private (Padrão) Observação Em alguns casos, o escopo explícito não se aplica. Por exemplo, no programa principal de uma aplicação autônoma, não há diferença na visibilidade para variáveis com escopo PUBLIC ou PRIVATE . Em programas de exemplo, o prefixo de tipo é sempre relevante e obrigatório.
**Type**
Especifica um caractere que indica o tipo de dados da variável. A tabela a seguir lista os valores sugeridos para Type . Type Descrição a Array c Character , Varchar , Varchar (Binary) y Currency d Date t DateTime b Double f Float l Logical n Numeric o Object q Varbinary , Blob u Unknown
**VariableName**
Especifica o nome da variável.

# Exemplo

O exemplo a seguir ilustra como a letra "n" indica que a variável Counter tem tipo Numeric e escopo local:

```foxpro
nCounter
lnCounter
```
