# SYS(1269) - Informações de propriedade

Retorna um valor que indica se uma configuração de propriedade foi alterada em relação à sua configuração padrão ou se a propriedade é somente leitura.

```foxpro
SYS(1269, oObjectName, cProperty, nPropertyAttribute)
```

#### Parâmetros
 **oObjectName**
Especifica o objeto para o qual as informações de configuração da propriedade são retornadas.
**cProperty**
Especifica a propriedade para a qual SYS(1269) retorna informações.
**nPropertyAttribute**
Especifica um valor numérico que determina o comportamento dos valores de retorno de SYS(1269). A tabela a seguir lista os valores para nPropertyAttribute. nPropertyAttribute Descrição 0 Retorna True (.T.) se a configuração da propriedade foi alterada em relação à sua configuração padrão. Retorna False (.F.) se a configuração da propriedade não foi alterada em relação à sua configuração padrão. 1 Retorna True (.T.) se a configuração da propriedade é somente leitura. Retorna False (.F.) se a propriedade é leitura/gravação.

# Valor de retorno

Character. SYS(1269) retorna True (.T.) ou False (.F.), cujo significado depende do valor de nPropertyAttribfsute.

# Observações

SYS(1269) é útil para determinar se uma configuração de propriedade foi alterada ou se é leitura/gravação antes de tentar definir a propriedade programaticamente.
