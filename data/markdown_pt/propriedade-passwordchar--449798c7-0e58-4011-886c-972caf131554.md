# Propriedade PasswordChar

Determina se os caracteres digitados por um usuário ou caracteres substitutos são exibidos em um controle TextBox; determina o caractere usado como substituto. Disponível em tempo de design e em tempo de execução.

```foxpro
TextBox.PasswordChar[ = cCharString]
```

# Valor de retorno
 **cCharString**
Especifica os caracteres exibidos em uma caixa de texto.

# Observações

Aplica-se a: EditBox Control, TextBox Control (Visual FoxPro)

Use esta propriedade para criar um campo de senha em uma caixa de diálogo. Embora você possa usar qualquer caractere, a maioria das aplicações usa o asterisco (*), caractere ANSI 42.

Esta propriedade não afeta a configuração da propriedade Value; ela contém exatamente o que o usuário digita ou o que foi definido pelo código. Defina PasswordChar como uma cadeia de caracteres vazia ("") para exibir o texto real. A configuração padrão é uma cadeia de caracteres vazia.

Você pode atribuir qualquer cadeia de caracteres a esta propriedade, mas somente o primeiro caractere é significativo; todos os outros são ignorados.
