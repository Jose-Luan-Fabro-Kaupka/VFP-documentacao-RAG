# Função MROW( )

Retorna a posição de linha do ponteiro do mouse na janela principal do Visual FoxPro ou em uma janela ou formulário definido pelo usuário.

```foxpro
MROW([cWindowName | 0 [, nScaleMode]])
```

#### Parâmetros
 **cWindowName**
Especifica o nome de uma janela cuja posição de linha do ponteiro do mouse MROW( ) retorna.
**0**
Especifica que a posição de linha do ponteiro do mouse é retornada para a janela ou formulário atualmente ativo.
**nScaleMode**
Especifica a unidade de medida para o valor que MROW( ) retorna. As configurações para nScaleMode são: nScaleMode Descrição 0 Foxels. (Padrão) Um foxel é equivalente à altura e largura médias de um caractere baseado na fonte atual do formulário em que um objeto está contido. 3 Pixels. Um pixel é o menor elemento que pode ser exibido em uma tela ou impressora. Pixels dependem da tela.

# Valor de retorno

Numeric. MROW( ) retorna o seguinte sob condições específicas:
 - Se não houver janela definida pelo usuário ativa e você omitir o argumento opcional, MROW( ) retorna a posição de linha do ponteiro do mouse na janela principal do Visual FoxPro.
- Se houver uma janela definida pelo usuário ativa e você omitir o argumento opcional, MROW( ) retorna a coordenada de linha do ponteiro do mouse relativa à janela definida pelo usuário ativa.
- Se o ponteiro do mouse estiver posicionado fora da janela definida pelo usuário ou se nenhum driver de mouse estiver carregado e não houver janela de saída, MROW( ) retorna um valor de -1.

# Observações

Usar a função MROW( ) sem o argumento opcional 0 pode afetar o comportamento do código em formulários quando a propriedade Form AllowOutput está definida como false (.F.). Por exemplo, a posição de um menu de atalho definido no evento RightClick pode não ser exibida no local correto se você usar as funções MROW( ) e MCOL( ) para determinar onde o menu é exibido. Nesse caso, certifique-se de incluir 0 nas funções MROW( ) e MCOL( ).
