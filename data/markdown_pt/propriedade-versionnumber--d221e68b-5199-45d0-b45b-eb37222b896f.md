# Propriedade VersionNumber

O número de build de um projeto.

```foxpro
Object.VersionNumber[ = cBuildNumber]
```

# Valor de retorno
 **cBuildNumber**
Especifica um número de build para um projeto. O formato padrão para um número de build de projeto é "MMMM.mmmm.bbbb", onde MMMM é o número de build principal, mmmm é o número de build secundário e bbbb é o número de build. Separe cada componente de um número de build de projeto com um ponto (.). Cada número de build pode ter de zero a quatro dígitos (números). Não use letras no número de build. Você pode especificar ".." para cBuildNumber para redefinir tanto o número de build secundário quanto o número de build para zero. Se a propriedade AutoIncrement estiver definida como true (.T.) e você gerar um executável (.exe) ou biblioteca de vínculo dinâmico (.dll) a partir do projeto, o número de build terá zeros à esquerda removidos da última porção (".bbbb") do número de build. O valor padrão é a cadeia de caracteres vazia.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

A propriedade VersionNumber corresponde aos valores dos itens Version Number na caixa de diálogo EXE Version Dialog Box.
