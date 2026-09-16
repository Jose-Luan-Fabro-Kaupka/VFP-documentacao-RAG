# Propriedade OLEServerBusyRaiseError

Especifica se uma mensagem de erro é exibida quando uma solicitação Automation é rejeitada. Leitura/gravação em tempo de execução.

```foxpro
ApplicationObject.OLEServerBusyRaiseError[ = lExpression]
```

# Valor de retorno
 **lExpression**
Uma das seguintes configurações: Configuração Descrição .T. (True) Um erro não ocorre e uma mensagem de ocupado não é exibida quando o número de milissegundos especificado pela propriedade OLEServerBusyTimeout tiver decorrido. .F. (False) (Padrão) Um erro ocorre e uma mensagem de ocupado é exibida quando o número de milissegundos especificado pela propriedade OLEServerBusyTimeout tiver decorrido.

# Observações

Aplica-se a: Application Object | _VFP System Variable
