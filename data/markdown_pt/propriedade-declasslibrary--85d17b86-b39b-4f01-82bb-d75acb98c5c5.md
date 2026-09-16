# Propriedade DEClassLibrary

Especifica o nome de um arquivo de programa (.prg) ou de biblioteca de classes visuais (.vcx) que contém a classe DataEnvironment especificada pela propriedade DEClass. Leitura/gravação em tempo de design e somente leitura em tempo de execução.

```foxpro
Form.DEClassLibrary [= cClassLibraryName]
```

# Valor de retorno
 **cClassLibraryName**
Tipo de dados Character. O parâmetro cClassLibraryName especifica um dos seguintes: Nome de um arquivo de programa (.prg) Nome de um arquivo de biblioteca de classes visuais (.vcx)

# Observações

Aplica-se a: Objeto Form

Para obter detalhes, consulte Propriedade DEClass.

# Exemplo

O exemplo a seguir cria uma classe Form e define as propriedades DEClassLibrary e DEClass para especificar uma classe DataEnvironment externa e sua biblioteca de classes.

```foxpro
DEFINE CLASS form1 as Form
   DEClassLibrary="MyProgram.prg"
   DEClass="MyDE"
ENDDEFINE
```
