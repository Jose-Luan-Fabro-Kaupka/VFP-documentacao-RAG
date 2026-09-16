# Propriedade AutoActivate

Determina como um controle OLE Container pode ser ativado. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.AutoActivate[ = nValue]
```

# Valor de retorno
 **nValue**
As configurações da propriedade AutoActivate são: Configuração Descrição 0 Manual. O controle não é ativado automaticamente. Você pode ativar um controle programaticamente usando o método DoVerb. 1 GotFocus. Se o controle contém um objeto, o aplicativo que fornece o objeto é ativado quando o controle recebe o foco. 2 (Padrão) DoubleClick. Se o controle contém um objeto, o aplicativo que fornece o objeto é ativado quando o usuário clica duas vezes no controle ou pressiona ENTER quando o controle tem o foco. 3 Automatic. Se o controle contém um objeto, o aplicativo que fornece o objeto é ativado com base no método normal de ativação do objeto (quando o controle recebe o foco ou quando o usuário clica duas vezes no controle).

# Observações

Aplica-se a: controle OLE Bound | controle OLE Container

Se um objeto incorporado suporta ativação no local, você pode definir AutoActivate como 1 (GotFocus) para ativar um objeto quando o controle recebe o foco.

> **Observação:** Quando AutoActivate é definido como 2 (Double-Click), o evento DblClick não ocorre.
