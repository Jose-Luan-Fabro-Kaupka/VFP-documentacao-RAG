# Tipo de campo Double

Quando você precisa de mais precisão, por exemplo, quando tem uma quantidade fixa de armazenamento na tabela ou valores de ponto flutuante verdadeiros, use o tipo de dados Double em vez de Numeric. Diferentemente dos dados numéricos, você determina a posição do ponto decimal ao inserir o valor em uma tabela.

> **Observação:** Quando o tipo de dados Double é usado em uma tabela, o número de decimais especificado quando o campo é criado serve apenas para fins de exibição. O Visual FoxPro armazena o valor real no campo.

Para especificações sobre o tipo de campo Double, consulte Visual FoxPro Data and Field Types.

# Exemplo

O exemplo a seguir cria um cursor com um campo Double e especifica 2 dígitos de precisão para o campo. O campo exibe apenas 2 dígitos de precisão, embora o valor contenha mais de 2 dígitos de precisão.

```foxpro
&& Close any open databases and clear memory.
CLOSE DATABASES ALL
CLEAR
&& Create a cursor with field of Double type.
CREATE CURSOR myCursor (myField B(2))
&& Insert value into cursor.
INSERT INTO myCursor VALUES (1234.561234)
&& Evaluate and display value in myField.
? EVALUATE("myCursor.myField") && Displays 1234.56.
&& Evaluate and compare values to determine actual value.
? EVALUATE("myCursor.myField") = 1234.56 && Displays .F.
? EVALUATE("myCursor.myField") = 1234.561234 && Displays .T.
```
