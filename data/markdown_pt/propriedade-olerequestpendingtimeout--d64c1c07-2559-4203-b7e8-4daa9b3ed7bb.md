# Propriedade OLERequestPendingTimeout

Especifica quanto tempo após uma solicitação Automation ser feita antes que uma mensagem de ocupado seja exibida. Leitura/gravação em tempo de execução.

```foxpro
ApplicationObject.OLERequestPendingTimeout[ = nMilliseconds]
```

# Valor de retorno
 **nMilliseconds**
Especifica o número de milissegundos que devem decorrer antes que uma mensagem de ocupado seja exibida quando uma solicitação Automation está pendente. A mensagem de ocupado é exibida quando ocorre um evento de mouse ou teclado. O valor padrão de nMilliseconds é 5.000 milissegundos. Se nMilliseconds for 0, uma mensagem de ocupado não é exibida quando uma solicitação Automation está pendente e ocorre um evento de mouse ou teclado.

# Observações

Aplica-se a: Application Object | _VFP System Variable
