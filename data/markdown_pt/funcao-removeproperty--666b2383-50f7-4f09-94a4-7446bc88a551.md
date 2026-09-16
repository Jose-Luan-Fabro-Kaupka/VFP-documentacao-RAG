# Função REMOVEPROPERTY( )

Remove uma propriedade de um objeto em tempo de execução.

```foxpro
REMOVEPROPERTY(oObjectName, cPropertyName)
```

#### Parâmetros
 **oObjectName**
Especifica o nome do objeto do qual remover a propriedade.
**cPropertyName**
Especifica o nome da propriedade existente a ser removida do objeto. Você pode especificar somente um nome de propriedade, não um nome de evento ou método.

# Valor de retorno

Tipo de dados lógico. REMOVEPROPERTY( ) retorna True (.T.) se remover a propriedade com sucesso; caso contrário, retorna False (.F.).

# Observações

Você pode usar REMOVEPROPERTY( ) para remover propriedades, mas não métodos ou eventos. Você pode usar REMOVEPROPERTY( ) com instâncias de objetos criadas a partir de classes do Visual FoxPro, classes COM, comando SCATTER...NAME, _VFP e _SCREEN.

As propriedades devem ser visivelmente Public, não Hidden ou Protected, e ter sido adicionadas a uma instância de um objeto, normalmente usando a função ADDPROPERTY( ), o método AddProperty ou o comando SCATTER...NAME, para que possam ser removidas usando REMOVEPROPERTY( ).

Você não pode remover uma propriedade se ela é membro da definição de classe usada para criar a instância do objeto.

A função REMOVEPROPERTY( ) não remove propriedades que são elementos específicos de array. Para remover um array, forneça somente o nome do array.

# Exemplos

Exemplo 1

O exemplo a seguir adiciona uma nova propriedade a um objeto criado com o comando SCATTER e depois a remove.

```foxpro
USE customers
SCATTER NAME oCust
ADDPROPERTY(oCust,"MyProperty")
REMOVEPROPERTY(oCust,"MyProperty")
```

Exemplo 2

O exemplo a seguir cria um array de propriedades para o objeto `oMyForm`, exibe seu conteúdo, `1` e `"Two"`, e depois o remove.

```foxpro
oMyForm = CREATEOBJECT('Form')
ADDPROPERTY(oMyForm, 'MyArray(2)', 1)
oMyForm.MyArray(2) = "Two"
CLEAR
? oMyForm.MyArray(1)
? oMyForm.MyArray(2)
REMOVEPROPERTY(oMyForm, 'MyArray')
RELEASE oMyForm
CLEAR
```
