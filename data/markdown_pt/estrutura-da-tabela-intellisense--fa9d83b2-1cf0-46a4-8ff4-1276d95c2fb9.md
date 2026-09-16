# Estrutura da tabela IntelliSense

A tabela IntelliSense contém registros que especificam a funcionalidade IntelliSense para elementos de linguagem nativos do Visual FoxPro e definidos pelo usuário. Por padrão, a tabela IntelliSense é nomeada FoxCode e é armazenada no arquivo FoxCode.dbf, que está localizado no diretório principal do Microsoft Visual FoxPro e é especificado pela variável de sistema _FOXCODE. Para obter mais informações, consulte Variável de sistema _FOXCODE.

> **Observação:** A tabela IntelliSense contém suporte limitado para a janela Watch no Visual FoxPro Debugger e depende de uma expressão ser válida para a janela Watch.

O suporte para a janela Watch existe na tabela IntelliSense para as seguintes áreas:
 - List Members para objetos instanciados.
- Quick Info para objetos instanciados.
- Itens de função.
- Expansão de variável de memória digitando m.

A funcionalidade IntelliSense não é suportada na janela Watch para o seguinte:
 - List Values para objetos instanciados.
- Itens de comando.
- Manipuladores de script padrão.
- Editores de valor de propriedade.
- Comandos definidos pelo usuário.
- Arquivos usados recentemente (MRU).

A tabela a seguir descreve a estrutura da tabela IntelliSense.

| Field name | Type (size) | Description |
| --- | --- | --- |
| Type | C (1) | Especifica o tipo de item no registro. Para obter mais informações, consulte Tipos de item válidos para o campo Type. |
| Abbrev | C (24) | Representa o conjunto mínimo de caracteres digitados para ativar a funcionalidade IntelliSense para este item. O texto que você digita a partir do campo Abbrev é substituído pelo texto no campo Expanded. |
| Expanded | C (26) | Especifica o texto que o IntelliSense usa para substituir o texto digitado na posição atual do cursor. O texto no campo Expanded substitui o texto que você digita a partir do campo Abbrev. |
| Cmd | C (15) | Especifica a referência de script para este item. |
| Tip | M | Especifica o texto a exibir na janela Quick Info Tip. |
| Data | M | Especifica conteúdo para a funcionalidade IntelliSense List Values, código Visual FoxPro específico para este item ou outro texto de script. |
| Case | C (1) | Especifica capitalização de letras para texto de substituição. U = Maiúsculas L = Minúsculas M ou <empty> = Misto P = Proper case X = Inalterado Qualquer valor que você especificar no campo do registro de versão define um padrão global para registros individuais que não têm uma configuração Case. |
| Save | L | Especifica se o registro é salvo quando o campo é atualizado. |
| TimeStamp | T | Representa um carimbo de data/hora exclusivo para este item. |
| Source | M | Especifica a origem do conteúdo do registro. A palavra RESERVED especifica conteúdo principal fornecido com esta versão do Visual FoxPro. Este campo pode conter informações de caminho e nome de arquivo para registros fornecidos pelo usuário. |
| UniqueID | C (10) | Especifica um identificador exclusivo para este registro. |
| User | M | Especifica informações do usuário. |

# Tipos de item válidos para o campo Type

A tabela a seguir descreve valores válidos e tipos de item para o campo Type na tabela IntelliSense.

| Type field | Item type | Description |
| --- | --- | --- |
| O | COM Component | Especifica a referência de biblioteca de tipos COM a exibir em listas IntelliSense de cláusula AS. Para obter mais informações, consulte Tipo de item COM Component. |
| C | Command | Especifica itens de conclusão de sintaxe para comandos do Visual FoxPro. Para obter mais informações, consulte Tipo de item Command. |
| E | XML | Especifica que o item é uma propriedade ou método que possui metadados de membro. Para obter mais informações, consulte MemberData Extensibility. |
| F | Function | Especifica itens de conclusão de sintaxe para funções, procedimentos e funções definidas pelo usuário do Visual FoxPro. Para obter mais informações, consulte Tipo de item Function. |
| P | Property | Especifica referências de script para exibir editores de valor para certas propriedades do Visual FoxPro. Para obter mais informações, consulte Tipo de item Property. |
| S | Script | Especifica os scripts do Visual FoxPro a executar. Para obter mais informações, consulte Tipo de item Script. |
| T | Typing | Especifica itens que aparecem em listas IntelliSense de cláusula AS ou ao referenciar objetos. Para obter mais informações, consulte Tipo de item Typing. |
| U | User | Especifica itens de autoexpansão definidos pelo usuário. Diferente dos itens Command, os itens User não requerem correspondências exatas de padrão. Para obter mais informações, consulte Tipo de item User. |
| V | Version | Especifica um registro especial para informações de versão e rastreamento (reservado). Para obter mais informações, consulte Tipo de item Version. |

### Tipo de item COM Component

O tipo de item COM Component especifica um registro da tabela IntelliSense cujo conteúdo aparece em listas IntelliSense de cláusula AS, semelhante a itens Typing. Um item COM Component especifica o nome de uma biblioteca de tipos COM que contém uma coleção de classes (ProgIDs) das quais o Visual FoxPro pode criar instâncias usando a função CREATEOBJECT( ). O campo Data para um item COM Component contém o GUID e a versão da biblioteca de tipos.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item COM Component.

| Field Name | Example |
| --- | --- |
| Type | O |
| Abbrev | Excel |
| Cmd | {} |
| Tip | Microsoft Excel 9.0 Object Library |
| Data | {00020813-0000-0000-C000-000000000046}#1.3 |

### Tipo de item Command

O item Command especifica um registro da tabela IntelliSense cujo conteúdo completa ou substitui sintaxe ou exibe uma janela Tip para comandos do Visual FoxPro.

> **Observação:** Os caracteres no campo Abbrev de registros de item Command devem corresponder às iniciais do texto no campo Expanded. Por exemplo, se o campo Expanded contiver o comando MODIFY COMMAND, o campo Abbrev deve conter as iniciais MC.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item Command.

| Field Name | Example |
| --- | --- |
| Type | C |
| Abbrev | MC |
| Expanded | MODIFY COMMAND |

### Tipo de propriedade _MemberData

O registro _MemberData suporta os hooks de builder de design-time GetMemberData.

| Field Name | Example |
| --- | --- |
| Type | E - Indica que o item é propriedade ou método com metadados |
| Abbrev | _GETMEMBERDATA - Nome de uma propriedade ou método de membro |
| Data | Conteúdo do script a executar para a propriedade ou método |

### Tipo de item Function

O item Function especifica um registro da tabela IntelliSense cujo conteúdo completa ou substitui sintaxe ou exibe uma janela Tip para funções e procedimentos do Visual FoxPro e definidos pelo usuário.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item Function.

| Field Name | Example |
| --- | --- |
| Type | F |
| Abbrev | FCOU |
| Expanded | FCOUNT |
| Tip | [ nWorkArea | cTableAlias ] |

### Tipo de item Property

O item Property especifica um registro da tabela IntelliSense cujo conteúdo pode especificar código em seu campo Data ou uma referência de script em seu campo Data a um item Script. O código ou referência de script pode executar para exibir um editor de valor personalizado quando você atribui valores para a propriedade à qual o item Property corresponde.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item Property.

| Field Name | Example |
| --- | --- |
| Type | P |
| Abbrev | .Picture |
| Cmd | {picture} |

Neste exemplo, o campo Cmd contém a referência de script "{picture}" para um script armazenado por um item Script separado. O campo Abbrev no registro Script contém a cadeia de caracteres "Picture" e o código no campo Data do registro Script é executado quando você digita a seguinte linha de código ou usa IntelliSense para completar a seguinte sintaxe:

```foxpro
Object.Picture=
```

Para obter mais informações, consulte Tipo de item Script.

### Tipo de item Script

O item Script especifica um registro da tabela IntelliSense que contém código ou dados em seu campo Data. Quando você armazena código em um item Script separado, outros registros da tabela IntelliSense podem referenciar e executar esse código armazenando uma referência de script no campo Cmd.

> **Observação:** Uma referência de script é uma palavra-chave opcional que aparece no campo Abbrev do registro Script e é delimitada por um par de chaves de abertura e fechamento ({}).

O código que o IntelliSense executa deve conter um parâmetro a passar para o objeto de parâmetro FoxCode. O objeto de parâmetro FoxCode contém metadados descrevendo como o script foi chamado, incluindo o registro de origem na tabela IntelliSense. Portanto, o código em um campo Data deve conter uma instrução PARAMETERS ou LPARAMETERS para acomodar a referência do objeto. Para obter mais informações sobre o objeto de parâmetro FoxCode, consulte Referência do objeto FoxCode.

O valor retornado pelo código substitui qualquer texto digitado na posição atual do cursor. No entanto, se o valor de retorno for avaliado como uma cadeia de caracteres vazia (""), o Visual FoxPro deixa o texto digitado inalterado.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item Script.

| Field Name | Example |
| --- | --- |
| Type | S |
| Abbrev | Picture |
| Data | (Stored in a memo field) LPARAMETERS oFoxcode LOCAL lcPicture oFoxcode.ValueType="V" lcPicture = GETPICT() IF LEN(lcPicture) > 0 lcPicture = ['] + lcPicture + ['] ENDIF RETURN lcPicture |

Para este exemplo, suponha que o campo Cmd em um item Property para a propriedade Picture contenha a referência de script "{picture}" para o item Script de exemplo. Quando você seleciona a propriedade Picture para um objeto digitando `.Picture` seguido de um sinal de igual (=) e seleciona o seletor de imagem, o código no campo Data do item Script é executado e exibe a caixa de diálogo Open Picture.

Para obter mais informações sobre o uso de scripts, consulte Como: criar scripts IntelliSense.

### Tipo de item Typing

O item Typing especifica um registro da tabela IntelliSense cujo conteúdo descreve um item que aparece na lista IntelliSense para cláusulas AS. O campo Data para um item Typing pode opcionalmente conter código que retorna um valor que o IntelliSense insere na posição atual do cursor.

> **Dica:** Se você incluir código no campo Data, termine-o com uma instrução RETURN.

A tabela a seguir ilustra um exemplo de registro IntelliSense para um item Typing.

| Field Name | Example |
| --- | --- |
| Type | T |
| Abbrev | CommandButton |
| Data | CommandButton |

### Tipo de item User

O item User especifica um registro da tabela IntelliSense cujo conteúdo completa ou substitui abreviações definidas pelo usuário. Diferente do campo Abbrev em itens Command, a abreviação do item User não precisa corresponder às iniciais do texto no campo Expanded.

| Field Name | Example |
| --- | --- |
| Type | U |
| Abbrev | MYADDRESS |
| Expanded | 101 Main Street |

### Tipo de item Version

O tipo de item Version especifica um registro da tabela IntelliSense que contém configurações padrão e rastreia informações de versão. O tipo de item Version é reservado para uso interno.

| Field Name | Example |
| --- | --- |
| Type | V |
| Expanded | Identifies latest version of IntelliSense. For internal use. |
