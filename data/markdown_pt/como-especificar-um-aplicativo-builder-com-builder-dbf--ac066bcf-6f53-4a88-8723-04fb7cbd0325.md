# Como: especificar um aplicativo builder com Builder.dbf

Você pode usar a tabela Builder.dbf para especificar um aplicativo builder. Cada registro contém campos que representam o nome de um builder, opcionalmente uma descrição do builder e um campo chamado Type que identifica a propriedade Class ou Base Class que invoca o builder personalizado. Por exemplo, a entrada Type para um Command Button é Commandbutton e a entrada Type para o builder Autoformat é Multiselect porque ele é executado em vários controles selecionados.

A tabela a seguir descreve um registro da tabela BUILDER.

| Nome do campo | Tipo de campo | Largura (comentário) |
| --- | --- | --- |
| NAME | Character | 45 (Nome do builder) |
| DESCRIPT | Memo | 4 |
| BITMAP (não usado) | Memo | 4 |
| TYPE | Character | 20 |
| PROGRAM | Memo | 4 (Aplicativo builder) |
| CLASSLIB | Memo | 4 (Nome da biblioteca de classes) |
| CLASSNAME | Memo | 4 (Classe do builder) |
| PARMS | Memo | 4 (lista de parâmetros passados) |

O aplicativo builder nomeado compara o valor no campo Type e a Class do objeto e inicia se houver correspondência. Se mais de uma correspondência for encontrada, uma caixa de diálogo de seleção é exibida.

Por padrão, o aplicativo Builder.app passa três parâmetros, listados no campo PARMS de Builder.dbf, para um programa builder:

| Entrada PARMS | Descrição |
| --- | --- |
| wbReturnValue | Variável que contém um valor a ser retornado ao Builder.app. |
| <cadeia de caracteres> | Uma cadeia literal a passar para a tabela Register. |
| <valor opcional> | Uma palavra-chave ou outro valor a passar ao Builder.app |

### Para criar um builder personalizado
- Escreva um aplicativo que forneça uma interface e modifique o controle ou controles selecionados.
- Salve o aplicativo na pasta Wizards.
- Abra a tabela Builders.dbf e acrescente um novo registro.
- Insira valores nos campos Name, Descript, Type e Program. Se seu builder personalizado usa valores adicionais, você também pode inserir valores nos campos restantes.

Depois de concluir todas as entradas e fechar o Browse, o novo builder é registrado. Por exemplo, se você criar um programa que altera as fontes dos controles selecionados e salvar o programa em um arquivo chamado Chgfont.prg, a tabela a seguir mostra as entradas para Builder.dbf.

| Nome do campo | Valor |
| --- | --- |
| NAME | The Builder That Changes Fonts |
| DESCRIPT | This builder modifies the font of all selected controls |
| TYPE | MULTISELECT |
| PROGRAM | Chgfont.prg |

Ao usar o builder, o Visual FoxPro exibe a caixa de diálogo Builder Selection porque agora existem dois builders do tipo Multiselect. Ao escolher The Builder that Changes Fonts , o Builder.app executa o programa que você salvou como Chgfont.prg.
