# Propriedade IMEMode

Especifica a configuração da janela do Input Method Editor (IME) para um controle individual. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.IMEMode[ = nExpression]
```

# Valor de retorno
 **nExpression**
Uma das configurações a seguir: nExpression Ação da janela IME 0 (Padrão) No Control. O sistema operacional determina se a janela IME é aberta quando o controle tem o foco. Se a janela IME estiver fechada quando o controle tem o foco, a janela IME pode ser aberta pressionando a combinação de teclas que ativa a janela IME. 1 Open IME. A janela IME é aberta quando o controle tem o foco. 2 Close IME. A janela IME é fechada quando o controle tem o foco. A janela IME pode ser aberta pressionando a combinação de teclas que ativa a janela IME.

# Observações

Aplica-se a: ComboBox Control | EditBox Control | TextBox Control (Visual FoxPro)

Esta propriedade é ignorada, a menos que você esteja executando uma versão do Leste Asiático de uma versão suportada do Microsoft Windows.
