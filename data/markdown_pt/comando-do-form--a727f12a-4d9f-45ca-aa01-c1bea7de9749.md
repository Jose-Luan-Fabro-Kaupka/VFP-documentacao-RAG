# Comando DO FORM

Executa um formulário ou form set compilado criado com o Form Designer.

```foxpro
DO FORM FormName | ? [NAME VarName [LINKED]] [WITH cParameterList]
   [TO VarName] [NOREAD] [NOSHOW]
```

#### Parâmetros
 **FormName**
Especifica o nome do formulário ou form set a executar.
**?**
Exibe a caixa de diálogo Do, na qual você pode escolher um formulário ou form set a executar.
**NAME VarName [LINKED]**
Especifica uma variável ou elemento de matriz com a qual você pode referenciar o formulário ou form set. Se você especificar uma variável que não existe, o Microsoft Visual FoxPro a cria automaticamente. Se você especificar um elemento de matriz, a matriz deve existir antes de emitir DO FORM. Se a variável ou elemento de matriz que você especificar já existir, seu conteúdo é sobrescrito. Se você omitir a cláusula NAME, o Visual FoxPro cria uma variável de tipo objeto com o mesmo nome do arquivo de formulário ou form set. Inclua LINKED para vincular o formulário à variável associada a ele, de modo que o formulário seja liberado quando a variável sair de escopo. Se você não incluir LINKED, um formulário ainda pode estar ativo, mesmo que não haja variável de objeto associada ao formulário.
**WITH cParameterList**
Especifica os parâmetros passados ao formulário ou form set. Se um form set for executado, os parâmetros são passados ao método Init do form set se a propriedade WindowType do form set estiver definida como ModeLess (0) ou Modal (1). Os parâmetros são passados ao método Load se a propriedade WindowType do form set estiver definida como Read (2) ou ReadModal (3).
**TO VarName**
Especifica uma variável para conter um valor retornado do formulário. Se a variável não existir, o Visual FoxPro a cria automaticamente. Use o comando RETURN no procedimento do evento Unload do formulário para especificar o valor de retorno. Se você não incluir um valor de retorno, o valor padrão true (.T.) é retornado. Se você usar TO, a propriedade WindowType do formulário deve estar definida como 1 (Modal). Se o procedimento do evento Init do formulário retornar .F., impedindo a instanciação do formulário, o procedimento do evento Unload não retornará um valor para VarName.
**NOREAD**
Especifica que o form set é criado e exibido, embora os controles não sejam ativados até que READ seja emitido. NOREAD é ignorado se a propriedade WindowType do objeto form set não estiver definida como 2 (Read).
**NOSHOW**
Especifica que o método Show do formulário não é chamado quando o formulário é executado. Quando você inclui NOSHOW e executa o formulário, o formulário não fica visível até que a propriedade Visible do formulário seja definida como true (.T.) ou o método Show do formulário seja chamado.

# Observações

DO FORM executa o método Show do formulário ou form set.

As configurações da propriedade WindowType Read (2) ou ReadModal (3) são incluídas para compatibilidade retroativa e estão disponíveis apenas para formulários convertidos de versões anteriores do FoxPro.

# Exemplo

O exemplo a seguir executa a amostra de controle stop watch (Swatch.scx).

```foxpro
DO FORM (HOME(2) + 'Solution\Controls\Timer\Swatch.scx')
```
