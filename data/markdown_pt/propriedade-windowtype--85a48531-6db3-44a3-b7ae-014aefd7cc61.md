# Propriedade WindowType

Especifica como um form set ou formulário se comporta quando é exibido ou executado com DO FORM. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.WindowType[ = nType]
```

# Valor de retorno
 **nType**
Para um form set, as configurações para a propriedade WindowType são as seguintes: Configuração Descrição 0 Modeless. 1 Modal. Nenhum outro formulário pode se tornar ativo e o menu pode estar ativo. Todos os formulários no form set estão ativos. 2 Read. O form set se comporta como se fosse ativado pelo comando READ. A execução para no método Show ou no comando DO FORM. Quando o Form é desativado, a execução continua. (Incluído para compatibilidade com versões anteriores, e disponível apenas para Forms convertidos de versões anteriores do FoxPro.) 3 Read Modal. O form set se comporta como se fosse ativado pela cláusula MODAL de um comando READ. A execução do programa para no método Show ou no comando DO FORM. Quaisquer formulários especificados na propriedade WindowList estão disponíveis, mas outros formulários e o menu não estão disponíveis. (Incluído para compatibilidade com versões anteriores, e disponível apenas para formulários convertidos de versões anteriores do FoxPro.) Para um formulário, as configurações para a propriedade WindowType são as seguintes: Configuração Descrição 0 Modeless. 1 Modal. Nenhum outro formulário pode se tornar ativo e o menu está inativo. Todos os formulários no form set estão ativos.

# Observações

Aplica-se a: Form Object | FormSet Object | _SCREEN System Variable

Você não pode alterar a configuração WindowType depois que a janela foi exibida.

O método Show recebe um parâmetro que pode substituir a configuração WindowType.

> **Observação:** A configuração WindowType de um form set substitui as configurações WindowType individuais dos formulários que ele contém. Por exemplo, se a propriedade WindowType para um form set estiver definida como 0, todos os formulários contidos nele são modeless, independentemente de suas configurações individuais da propriedade WindowType.
