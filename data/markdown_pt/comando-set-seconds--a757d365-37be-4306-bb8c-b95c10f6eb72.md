# Comando SET SECONDS

Especifica se os segundos são exibidos na parte de hora de um valor DateTime.

```foxpro
SET SECONDS ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Especifica que os segundos são exibidos em valores DateTime.
**OFF**
Especifica que os segundos não são exibidos em valores DateTime.

# Observações

SET SECONDS tem escopo na sessão de dados atual.

# Exemplo

O exemplo a seguir demonstra o efeito da configuração SET SECONDS no valor de hora retornado por DATETIME( ). Quando SET SECONDS está ON, o valor de hora é exibido com a parte de segundos. Quando SET SECONDS está OFF, o valor de hora é exibido sem a parte de segundos.

```foxpro
SET SECONDS ON
CLEAR
? DATETIME()  && Displays time value with the seconds portion
SET SECONDS OFF  && Displays time value without the seconds portion
? DATETIME()
```
