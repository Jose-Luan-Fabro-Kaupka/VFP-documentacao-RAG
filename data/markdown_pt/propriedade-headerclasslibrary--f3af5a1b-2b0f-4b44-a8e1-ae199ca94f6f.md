# Propriedade HeaderClassLibrary

Especifica a biblioteca de classes que contém a classe membro associada à propriedade HeaderClass. Leitura/gravação em tempo de design e em tempo de execução.

HeaderClassLibrary é usada em vez de MemberClassLibrary para um contêiner pai Column. Para obter mais informações, consulte Propriedade MemberClassLibrary.

```foxpro
Column.HeaderClassLibrary [= cClassFile]
```

# Valor de retorno

Cadeia de caracteres. O parâmetro cClassFile especifica o nome do arquivo de programa (.prg) que contém a definição da classe membro especificada por HeaderClass.

# Observações

Aplica-se a: objeto Column

O Visual FoxPro inclui o programa HeaderClassLibrary (.prg) no projeto durante a compilação do projeto.

Se você definir HeaderClassLibrary em tempo de execução, deve usar o nome completo do arquivo, incluindo sua extensão.
