# Propriedade DateMark

Especifica o delimitador para valores Date e DateTime exibidos em uma caixa de texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.DateMark[ = cDateMarkCharacter]
```

# Valor de retorno
 **cDateMarkCharacter**
Especifica o delimitador de valores Date e DateTime. Se cDateMarkCharacter for a cadeia de caracteres vazia, o delimitador é determinado pela configuração de SET MARK. Se cDateMarkCharacter for um espaço, o delimitador da configuração atual da propriedade DateFormat da caixa de texto é usado. Na janela Properties, use o comando = para especificar a cadeia de caracteres vazia (= "") ou um espaço (= " ") para a propriedade DateMark.

# Observações

Aplica-se a: TextBox Control (Visual FoxPro)

A configuração da propriedade DateMark é ignorada se a propriedade DateFormat estiver definida como Short ou Long.
