# Método SetVar

Cria uma variável e armazena um valor nela para uma instância do servidor de automação do aplicativo Visual FoxPro.

```foxpro
ApplicationObject.SetVar(cVariableName, eValue)
```

# Valor de retorno
 **cVariableName**
Especifica o nome da variável a criar.
**eValue**
Especifica o valor armazenado na variável. Se a variável especificada com cVariableName já existir, o novo valor é armazenado na variável.

# Observações

Aplica-se a: Application Object | _VFP System Variable

Embora o método DoCmd possa ser usado para definir uma variável como um valor de caractere, o método SetVar deve ser usado para definir uma variável para outros tipos de dados.
