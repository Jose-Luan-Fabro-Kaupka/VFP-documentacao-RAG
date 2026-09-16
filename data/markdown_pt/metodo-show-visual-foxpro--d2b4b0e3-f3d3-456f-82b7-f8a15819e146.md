# Método Show (Visual FoxPro)

Exibe um formulário e determina se o formulário é modal ou modeless.

```foxpro
 [FormSet.]Object.Show([nStyle])
```

#### Parâmetros
 **nStyle**
Determina como um formulário é exibido. Os seguintes valores são válidos: Value Description 1 Modal. Nenhuma entrada do usuário (teclado ou mouse) pode ocorrer em qualquer outro formulário ou no menu até que o formulário modal seja ocultado ou liberado. O programa deve ocultar ou liberar um formulário modal (geralmente em resposta a alguma ação do usuário) antes que mais entrada do usuário possa ocorrer. Embora outros formulários em sua aplicação sejam desabilitados quando um formulário modal é exibido, outras aplicações não são. 2 (Padrão) Modeless. O código que ocorre após a execução do método Show é executado conforme encontrado. Se você omitir nStyle, o formulário é exibido no estilo especificado pela propriedade WindowType.

# Observações

Aplica-se a: Form Object | FormSet Object | _SCREEN System Variable | ToolBar Object

O método Show define a propriedade Visible de um formulário ou form set como true (.T.) e torna o formulário o objeto ativo. Se a propriedade Visible de um formulário já estiver definida como true (.T.), o método Show torna-o o objeto ativo.

Se um form set é ativado, o último formulário ativo no form set também se torna ativo. Se nenhum formulário estiver ativo, o formulário que foi adicionado à definição da classe FormSet primeiro é tornado ativo.

Os formulários contidos em um form set mantêm sua configuração de propriedade Visible. Se a propriedade Visible de um formulário estiver definida como false (.F.), o método Show do form set não exibe o formulário.
