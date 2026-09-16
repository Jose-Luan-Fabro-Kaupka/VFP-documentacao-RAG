# Método DoStatus

Fornece a interface para feedback ao usuário não modal, como mensagens de status durante uma execução de relatório.

```foxpro
oReportListener.DoStatus(cMessage)
```

#### Parâmetros
 **cMessage**
Especifica a mensagem exibida pelo mecanismo de feedback ao usuário do objeto ReportListener.

# Valor de retorno

None.

# Observações

Aplica-se a: Objeto ReportListener.

Como o método DoMessage fornecido para feedback ao usuário modal na classe ReportListener, DoStatus respeita a configuração da propriedade QuietMode Property ao avaliar se o feedback ao usuário é apropriado no ambiente atual. Para obter mais informações, consulte Propriedade QuietMode.

A classe base ReportListener usa um mecanismo WAIT NOWAIT para implementar DoStatus, mas você pode substituir por uma forma diferente de feedback ao usuário não modal, conforme mostrado pela Classe Foundation ReportListener User Feedback. Certifique-se de combinar sua implementação de DoStatus com uma implementação apropriada de ClearStatus, para remover seu feedback não modal quando ele não se aplica mais (por exemplo, no final de uma execução de relatório). Para obter mais informações, consulte Método ClearStatus.
