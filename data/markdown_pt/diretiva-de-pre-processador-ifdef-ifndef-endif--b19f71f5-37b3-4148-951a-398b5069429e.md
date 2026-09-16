# Diretiva de pré-processador #IFDEF | #IFNDEF ... #ENDIF

Inclui condicionalmente um conjunto de comandos em tempo de compilação se uma constante de tempo de compilação estiver definida.

```foxpro
#IFDEF | #IFNDEF ConstantName
      Commands
[#ELSE
      Commands]
#ENDIF
```

#### Parâmetros
 **#IFDEF**
Especifica que um conjunto de comandos é incluído em tempo de compilação quando ConstantName está definido. Os itens a seguir descrevem como um conjunto de comandos é incluído em tempo de compilação quando você inclui #IFDEF: Se ConstantName estiver definido, o conjunto de comandos após #IFDEF e antes de #ELSE ou #ENDIF (o que ocorrer primeiro) é incluído em tempo de compilação. Se ConstantName não estiver definido e #ELSE estiver incluído, o conjunto de comandos após #ELSE e antes de #ENDIF é incluído em tempo de compilação. Se ConstantName não estiver definido e #ELSE não estiver incluído, nenhum comando dentro da estrutura #IFDEF ... #ENDIF é incluído em tempo de compilação.
**#IFNDEF**
Especifica que um conjunto de comandos é incluído em tempo de compilação quando ConstantName não está definido. Os itens a seguir descrevem como um conjunto de comandos é incluído em tempo de compilação quando você inclui #IFNDEF: Se ConstantName não estiver definido, o conjunto de comandos após #IFNDEF e antes de #ELSE ou #ENDIF (o que ocorrer primeiro) é incluído em tempo de compilação. Se ConstantName estiver definido e #ELSE estiver incluído, o conjunto de comandos após #ELSE e antes de #ENDIF é incluído em tempo de compilação. Se ConstantName estiver definido e #ELSE não estiver incluído, nenhum comando dentro da estrutura #IFNDEF ... #ENDIF é incluído em tempo de compilação.
**ConstantName**
Especifica a constante de tempo de compilação cuja existência determina se um conjunto de comandos é incluído em tempo de compilação. As constantes de tempo de compilação são definidas com #DEFINE.
**Commands**
Especifica o conjunto de comandos que é incluído em tempo de compilação.

# Observações

Você pode aninhar uma estrutura #IFDEF | #IFNDEF ... #ENDIF dentro de outra estrutura #IFDEF | #IFNDEF ... #ENDIF.

Comentários podem ser colocados na mesma linha após #IFDEF, #IFNDEF, #ELSE e #ENDIF. Esses comentários são ignorados durante a compilação e a execução do programa.

# Exemplo

O exemplo a seguir cria uma constante de tempo de compilação chamada MYDEFINE. #IFDEF ... #ENDIF exibe uma mensagem se a constante de tempo de compilação foi definida.

```foxpro
#DEFINE MYDEFINE 1
#IFDEF MYDEFINE
   WAIT WINDOW "MYDEFINE exists"
#ELSE
   WAIT WINDOW "MYDEFINE does not exist"
#ENDIF
```
