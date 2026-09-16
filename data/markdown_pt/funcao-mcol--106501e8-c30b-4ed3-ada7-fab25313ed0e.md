# Função MCOL( )

Retorna a posição da coluna do ponteiro do mouse na janela principal do Visual FoxPro ou em uma janela ou formulário definido pelo usuário.

```foxpro
MCOL([cWindowName | 0 [, nScaleMode]])
```

#### Parâmetros
 **cWindowName**
Especifica o nome da janela ou formulário cuja posição de coluna do ponteiro do mouse MCOL( ) retorna.
**0**
Especifica que a posição da coluna do ponteiro do mouse seja retornada para a janela ou formulário ativo no momento.
**nScaleMode**
Especifica a unidade de medida do valor retornado por MCOL( ). A tabela a seguir lista as configurações de nScaleMode. nScaleMode Descrição 0 Foxels. Um foxel equivale à altura e largura médias de um caractere com base na fonte atual do formulário que contém o objeto. (Padrão) 3 Pixels. Um pixel é o menor elemento que pode ser exibido em uma tela ou impressora. Os pixels dependem da tela.

# Valor de retorno

Numeric. MCOL( ) retorna a posição da coluna do ponteiro do mouse na janela principal do Visual FoxPro, em uma janela definida pelo usuário ou em um formulário.

Se você omitir cWindowName e não houver uma janela ou formulário definido pelo usuário ativo, MCOL( ) retornará a posição na janela principal do Visual FoxPro. Se houver uma janela ou formulário ativo, retornará a posição nele. MCOL( ) retorna –1 se o ponteiro estiver fora da janela ou formulário, se nenhum driver de mouse estiver carregado ou se não houver janela de saída.

# Observações

Usar MCOL( ) sem o argumento opcional 0 pode afetar o comportamento do código em formulários quando a propriedade AllowOutput de Form está definida como falso (.F.). Por exemplo, um menu de atalho definido no evento RightClick pode não aparecer no local correto se MCOL( ) e MROW( ) forem usados para determinar a posição. Nesse caso, inclua 0 nas funções MCOL( ) e MROW( ).
