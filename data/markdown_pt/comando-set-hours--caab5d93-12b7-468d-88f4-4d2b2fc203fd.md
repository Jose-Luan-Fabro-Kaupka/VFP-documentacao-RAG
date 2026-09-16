# Comando SET HOURS

Define o relógio do sistema para um formato de hora de 12 ou 24 horas.

```foxpro
SET HOURS TO [12 | 24]
```

#### Parâmetros
 **TO 12**
(Padrão) Especifica um formato de 12 horas.
**TO 24**
Especifica um formato de 24 horas.

# Observações

Use SET HOURS TO sem 12 ou 24 para retornar ao formato padrão de 12 horas.

TIME( ) sempre retorna um valor no formato de 24 horas e não é afetado por SET HOURS. O valor retornado por DATETIME( ) é determinado pela configuração atual de SET HOURS.

SET HOURS tem escopo na sessão de dados atual.
