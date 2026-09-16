# Função EXECSCRIPT( )

Permite executar várias linhas de código de variáveis, tabelas e outro texto em tempo de execução.

```foxpro
ExecScript(cExpression [, eParameter1, eParameter2, ...])
```

#### Parâmetros
 **cExpression**
Representa o texto, uma variável, cadeia de caracteres de tipo ou memo a ser executado como código.
**eParameter1 , eParameter2 , ...**
Opcional. Especifica parâmetros passados a um script que tenha uma instrução PARAMETER na primeira linha.

# Valor de retorno

O valor de retorno é o valor retornado pelo script em cExpression. Se o script não retornar valor, o Visual FoxPro retorna .T.

# Observações

ExecScript( ), diferentemente da expansão de macro, produz o mesmo efeito que selecionar várias linhas de código na janela de comando e pressionar a tecla Enter.

# Exemplo

Este exemplo cria um formulário e exibe o valor da propriedade AutoCenter do novo objeto Form. Observe o uso de CHR(13), que é usado para separar as duas linhas de código.

```foxpro
?EXECSCRIPT("oForm=CREATEOBJECT('Form')"+CHR(13)+"?oForm.AutoCenter")
```
