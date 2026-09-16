# Referência do objeto FoxCode

Fornece metadados para uso por scripts no campo Data de itens IntelliSense na tabela IntelliSense.

```foxpro
FoxCode.PropertyName [= eValue]
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade do objeto FoxCode.
**eValue**
Especifica um valor para a propriedade. A tabela a seguir descreve as propriedades e valores disponíveis. PropertyName eValue Abbrev Especifica o conteúdo do campo Abbrev. Case Especifica o conteúdo do campo Case. Cmd Especifica o conteúdo do campo Cmd. CursorLocChar Especifica um caractere especial que indica o local para posicionar o cursor após a execução do script. (O caractere padrão é til (~).) Data Especifica o conteúdo do campo Data. DefaultCase Especifica a configuração padrão de capitalização de letras na tabela IntelliSense conforme derivada do registro Version, cujo Type está definido como "V". Expanded Especifica o conteúdo do campo Expanded. Filename Especifica o nome do arquivo sendo editado. FullLine Especifica o texto completo da linha atualmente digitada. Icon Especifica o ícone a usar com a matriz Items. Items Especifica uma matriz a usar para preencher uma caixa de listagem exibida após a execução de um script. Requer ValueType definido como "L". Items[1,1] – Texto a exibir na lista Items[1,2] – Dica de valor para o item O único elemento obrigatório é o primeiro elemento de cada linha na matriz Items. Por padrão, a matriz é classificada em ordem ascendente para que operações de busca incremental possam ser realizadas. Os usuários podem usar a propriedade ItemSort para desativar essa funcionalidade e usar uma ordem de classificação natural. ItemScript Especifica o script a usar com a matriz Items. ItemSort Especifica se classificar a matriz Items (o padrão é .T.) Location Especifica o tipo de editor a editar: 0 – Command Window 1 – Program 8 – Menu Editor 10 – Code Editor 12 – Stored Procedure Menuitem Especifica o item de menu selecionado se o usuário estiver executando um script com ValueType definido como "L". Pode ser usado em um script subsequente. ParamNum Especifica o número do parâmetro da função para a chamada de script feita dentro de uma função. Save Especifica o conteúdo do campo Save. Source Especifica o conteúdo do campo Source. Timestamp Especifica o conteúdo do campo Timestamp. Tip Especifica o conteúdo do campo Tip. Type Especifica o conteúdo do campo Type. UniqueId Especifica o conteúdo do campo UniqueId. User Especifica o conteúdo do campo User. UserTyped Especifica o texto digitado pelo usuário. Não inclui a tecla ativadora nem espaços ou tabulações iniciais. Para incluir a tecla ativadora, espaços ou tabulações iniciais, use a propriedade FullLine. ValueTip Especifica a dica Quick Info a exibir quando ValueType está definido como "T". ValueType Especifica o manipulador da ação após a execução do script: L – Exibe uma caixa de listagem suspensa preenchida a partir da matriz Items. V – Exibe uma lista de valores. T – Exibe uma janela Quick Info Tip a partir de ValueTip.

# Observações

O campo Data de registros na tabela IntelliSense, especificado pela variável de sistema _FOXCODE, geralmente contém código de script. Para obter mais informações, consulte IntelliSense Table Structure.

A referência do objeto FoxCode é normalmente armazenada em uma variável chamada oFoxcode em scripts IntelliSense. Para obter mais informações, consulte How to: Create IntelliSense Scripts.
