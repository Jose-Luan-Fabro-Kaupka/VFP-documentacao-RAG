# Propriedade DockPosition

Indica a posição de encaixe para um objeto ToolBar ou Form definido pelo usuário. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.DockPosition [= nPosition]
```

# Valor de retorno
 **nPosition**
Indica a posição de encaixe para uma barra de ferramentas ou formulário. A tabela a seguir lista os valores para nPosition . nPosition Descrição –1 Não encaixado 0 Superior 1 Esquerda 2 Direita 3 Inferior 4 Em guia (somente formulários) 5 Encaixado por link (somente formulários) Observação Um valor de 5 indica que um formulário faz parte de um contêiner encaixado por link. Você pode encaixar uma janela encaixada em guia com um contêiner encaixado por link; portanto, é recomendado obter informações adicionais de encaixe usando a função ADOCKSTATE( ) e o método GetDockState.

# Observações

Aplica-se a: Form Object | ToolBar Object

Para recuperar informações detalhadas de encaixe, consulte ADOCKSTATE( ) Function e GetDockState Method.
