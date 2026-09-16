# Função ADDPROPERTY( )

Adiciona uma nova propriedade a um objeto em tempo de execução.

Você pode usar ADDPROPERTY( ) para adicionar propriedades e seus valores a objetos válidos do Visual FoxPro, incluindo aqueles criados a partir de classes do Visual FoxPro, classes COM e o comando SCATTER...NAME.

```foxpro
ADDPROPERTY(oObjectName, cPropertyName, [, eNewValue ])
```

#### Parâmetros
 **oObjectName**
Especifica o nome do objeto ao qual a propriedade é adicionada. Se oObjectName não for um objeto válido, o Visual FoxPro gera a mensagem apropriada.
**cPropertyName**
Especifica o nome da nova propriedade a ser adicionada ao objeto. Se a propriedade com o nome que você especificar não existir, a propriedade é criada e adicionada.
**eNewValue**
Especifica o valor a ser definido para a nova propriedade. Se você omitir eNewValue e a propriedade existir, o Visual FoxPro mantém o valor da propriedade inalterado. Se você omitir eNewValue e a propriedade for nova, o Visual FoxPro define o valor da nova propriedade como False (.F.).

# Valor de retorno

Tipo de dados lógico. A tabela a seguir descreve os valores de retorno para ADDPROPERTY( ) e o comportamento quando você tenta adicionar uma propriedade que já existe para um objeto.

| Valor de retorno | Descrição |
| --- | --- |
| True (.T.) | Quando ADDPROPERTY( ) adiciona a propriedade com sucesso. Quando a nova propriedade é uma propriedade de matriz e a matriz já existe, ADDPROPERTY( ) redimensiona a matriz com as dimensões especificadas por cPropertyName. Se você especificar um valor com eNewValue, todos os elementos na matriz são definidos para esse valor. Se você omitir eNewValue, todos os elementos da matriz são definidos como False (.F.). Se a nova propriedade não é uma propriedade de matriz, mas a propriedade existente é uma propriedade de matriz. A propriedade permanece uma propriedade de matriz com as mesmas dimensões. Se você especificar um valor com eNewValue, todos os elementos na matriz são definidos para esse valor. Se você omitir eNewValue, todos os elementos da matriz são definidos como False (.F.). Se a nova propriedade não é uma propriedade de matriz, e a propriedade existente não é uma propriedade de matriz ou não é uma propriedade nativa somente leitura do Visual FoxPro. Se você especificar um valor com eNewValue, a propriedade existente é definida para esse valor. Se você omitir eNewValue, o valor da propriedade existente permanece inalterado. Se a propriedade especificada já é membro do objeto, mas está marcada como Hidden ou Protected. O Visual FoxPro gera um erro, "Property name is not found (Error 1734)", e a propriedade não é definida para o valor passado a ADDPROPERTY( ). |
| False (.F.) | Quando ADDPROPERTY( ) não adicionou a propriedade com sucesso. Se a propriedade é uma propriedade de matriz, e a propriedade existente não é uma propriedade de matriz. A propriedade existente permanece inalterada. |

# Observações

Você pode criar matrizes de propriedades usando ADDPROPERTY( ) para um objeto. Ao fazer isso, cada elemento na matriz é inicializado com eNewValue, se fornecido. Caso contrário, o valor de cada propriedade na matriz é definido como False (.F.). Para obter mais informações sobre como criar uma matriz de propriedades para um objeto, consulte a seção Exemplos.

O Visual FoxPro adiciona a nova propriedade como uma propriedade Public. Você não pode especificar a propriedade como Protected ou Hidden.

Se a propriedade existente é uma propriedade nativa somente leitura do Visual FoxPro, como a propriedade BaseClass, o Visual FoxPro gera um erro, "Property name is read-only (Error 1743)".

Se o nome da propriedade não é válido, por exemplo, o nome da propriedade contém um espaço ou outros caracteres ilegais, o Visual FoxPro gera um erro, "Incorrect property name (Error 1470)".

Para instâncias de objetos derivadas de classes nativas do Visual FoxPro, ADDPROPERTY( ) respeita a configuração de visibilidade do método intrínseco AddProperty. Se AddProperty estiver marcado como Hidden ou Protected, ADDPROPERTY( ) não cria a nova propriedade e retorna False (.F.). Se o método AddProperty estiver marcado como Public (padrão), ADDPROPERTY( ) cria a propriedade e retorna True (.T.). Isso protege o design original da classe.

> **Observação:** Isso não se aplica a objetos COM criados com classes Visual FoxPro OLEPUBLIC.

ADDPROPERTY( ) não funciona ao usar o comando FOR EACH com referências de objeto. No entanto, você pode usar o método AddProperty.

# Exemplos

Exemplo 1

O exemplo a seguir adiciona uma nova propriedade a um objeto criado com o comando SCATTER.

```foxpro
USE customers
SCATTER NAME oCust
ADDPROPERTY(oCust,"MyProperty")
```

Exemplo 2

O exemplo a seguir cria uma matriz de propriedades para o objeto `oMyForm` e exibe seu conteúdo, `1` e `"Two"`.

```foxpro
oMyForm = CREATEOBJECT('Form')
ADDPROPERTY(oMyForm, 'MyArray(2)', 1)
oMyForm.MyArray(2) = "Two"
CLEAR
? oMyForm.MyArray(1)
? oMyForm.MyArray(2)
```
