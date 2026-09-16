# Propriedade AutoIncrement (Visual FoxPro)

Especifica se o número da versão de build de um projeto é incrementado automaticamente cada vez que um .exe distribuível ou um .dll in-process é compilado.

```foxpro
Object.AutoIncrement[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade AutoIncrement são: Configuração Descrição True (.T.) O número da versão de build de um projeto é incrementado automaticamente cada vez que um .exe distribuível ou um .dll in-process é compilado. False (.F.) (Padrão) O número da versão de build não é incrementado automaticamente.

# Observações

Aplica-se a: objeto Project (Visual FoxPro)

O número da versão de build não é incrementado se AutoIncrement estiver definido como false (.F.) ou quando o projeto é recompilado ou um .app distribuível é compilado.

O valor da propriedade AutoIncrement corresponde à caixa de seleção Auto Increment na caixa de diálogo EXE Version Dialog Box. O número da versão de build pode ser determinado ou definido com a propriedade VersionNumber .
