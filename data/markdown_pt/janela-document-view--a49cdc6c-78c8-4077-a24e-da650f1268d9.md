# Janela Document View

Permite visualizar e navegar até qualquer procedimento, função ou definição #DEFINE, classe ou diretiva de pré-processador em seu programa.

Você pode ativar esta janela no menu Tools ou quando escolhe Document View no menu de atalho de um programa em uma janela de edição.

> **Observação:** Quando a janela Document View está aberta para um arquivo .prg, você pode usar Ctrl-PgUp e Cltr-PgDn para navegar até o procedimento anterior/seguinte.

Clique com o botão direito nesta janela para acessar as seguintes opções.
 **Sort by Name**
Especifica que os itens da lista são classificados por nome.
**Sort by Location**
Especifica que os itens da lista são classificados por localização no programa. Quando você seleciona esta opção, pode usar Ctrl+PageUp ou Ctrl+PageDown para navegar pelos itens listados. Além disso, a janela Document View seleciona automaticamente o procedimento que contém o ponto de inserção no editor.
**Sort by Type**
Especifica que os itens da lista são classificados alfabeticamente por tipo de item.
**Display #define definitions**
Alterna a exibição de definições #DEFINE na lista.
**Display preprocessor directives**
Alterna a exibição de diretivas de pré-processador. A exibição relata os seguintes itens: #INCLUDE #IF...#ELIF...#ELSE...#ENDIF #IFDEF...#ELSE...#ENDIF #IFNDEF...#ELSE...#ENDIF
**Font**
Abre a caixa de diálogo Font para que você possa alterar a fonte usada na janela Document View

A janela Document View indica visualmente cada procedimento ou função, definição de pré-processador, classe e diretiva de pré-processador com os seguintes símbolos:
 - Um # (sinal de número) vermelho representa uma definição de pré-processador.
- Um # (sinal de número) amarelo representa uma diretiva de pré-processador.
- Uma caixa azul representa uma função ou procedimento.
- Um conjunto de caixas multicoloridas representa uma classe.
