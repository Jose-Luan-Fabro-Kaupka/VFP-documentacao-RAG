# Propriedade BindControls

Especifica quando a vinculação de dados ocorre para controles vinculados a dados.

O Visual FoxPro geralmente vincula os controles à fonte de dados quando o formulário é carregado. No entanto, você pode usar BindControls para especificar quando a vinculação de dados ocorre por vários motivos, como melhorar o desempenho ou atrasar a vinculação de controles à fonte de dados até que o usuário execute uma ação, após o formulário ser carregado, ou até que os dados sejam necessários.

> **Observação:** BindControls é destinado ao uso na exibição inicial de um formulário e para vincular controles após exibir o formulário. Embora você possa definir BindControls como False (.F.) e voltar para True (.T.), BindControls não é destinado a desvincular e revincular controles em tempo de execução.

```foxpro
Form.BindControls [= lValue]
```

# Valor de retorno

Tipo de dados Logical. A tabela a seguir lista os valores para lValue.

| lValue | Descrição |
| --- | --- |
| True (.T.) | O Control .ControlSource ou Grid .RecordSource vincula aos dados quando o formulário é carregado. (Padrão) Se Form .BindControls = .T. e Control .ControlSource ou Grid .RecordSource é alterado, o controle é revinculado. Se Form. BindControls é alterado de .T. para .F., as vinculações atuais não são alteradas. |
| False (.F.) | O Control .ControlSource ou Grid .RecordSource não vincula aos dados quando o formulário é carregado. Se Form .BindControls = .F. e Control .ControlSource ou Grid .RecordSource é alterado, o controle não é revinculado, mas a propriedade ControlSource ou Recordsource é alterada. Se Form. BindControls é alterado de .F. para .T., todos os controles no formulário são revinculados de acordo com o valor atual de Control. ControlSource ou Grid. RecordSource. |

# Observações

Aplica-se a: Form Object

# Exemplo

Suponha que um formulário precise carregar um grande número de tabelas ou tenha uma grade ou outros controles que vinculam a um cursor produzido por uma instrução SQL que demora muito para executar. Quando o usuário inicia o formulário, o formulário não aparece até carregar completamente todos os dados.

Ao definir BindControls como False (.F.), o formulário aparece imediatamente. Você pode então alterar BindControls para True (.T.) quando o formulário é ativado, como quando o evento Form Activate ocorre, e exibir uma mensagem como "Please wait while loading data." O usuário então vê o formulário imediatamente junto com uma mensagem que explica o atraso no carregamento dos dados, em vez de esperar o formulário aparecer.
