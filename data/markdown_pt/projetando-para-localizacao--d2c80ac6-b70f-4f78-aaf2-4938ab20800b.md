# Projetando para localização

Como o texto tende a aumentar quando você localiza uma aplicação, tenha cuidado ao projetar os seguintes componentes da interface do usuário:
 - Mensagens da aplicação
- Menus e formulários
- Ícones e bitmaps

# Criando mensagens da aplicação

Quando você cria mensagens em sua aplicação, cadeias de caracteres de texto em inglês geralmente são mais curtas que cadeias de caracteres equivalentes em outros idiomas. A tabela a seguir mostra o crescimento adicional médio para cadeias de caracteres, baseado em seu comprimento inicial.

| English length (in characters) | Additional growth for localized strings |
| --- | --- |
| 1 to 4 | 100% |
| 5 to 10 | 80% |
| 11 to 20 | 60% |
| 21 to 30 | 40% |
| 31 to 50 | 20% |
| over 50 | 10% |

### Projetando menus e formulários

Como nas mensagens, menus e formulários podem crescer quando a aplicação é localizada. Por exemplo, considere os seguintes formulários, que fazem parte de uma aplicação de exemplo de Caixa Eletrônico Automatizado. A primeira figura mostra o formulário em inglês, e a segunda figura mostra o equivalente em espanhol. Você pode ver que espaço extra foi alocado para o texto aumentar no formulário.

> **Dica:** Se você reservar espaço para o texto aumentar em uma interface, os localizadores precisam de menos tempo para redimensionar controles e redesenhar a interface.
 O texto precisa de mais espaço quando localizado

Em menus e formulários, evite sobrecarregar barras de status. Além disso, evite abreviações, pois elas podem não existir em outros idiomas.

# Usando ícones e bitmaps

Usados adequadamente, ícones e bitmaps podem ser uma parte importante de uma interface do usuário. No entanto, o significado de ícones e bitmaps pode ser mais ambíguo que o significado de palavras. Portanto, considere as seguintes diretrizes ao usar ícones e bitmaps:
 - Use imagens que são universalmente reconhecidas. Por exemplo, use um envelope para representar correio, mas não use uma caixa de correio porque não é um símbolo universal.
- Use imagens culturalmente sensíveis. Por exemplo, evite usar imagens de símbolos religiosos e animais.
- Evite usar texto em bitmaps, pois o crescimento de texto pode se tornar um problema, assim como em outras partes da interface.
- Evite jargão, gírias, humor, linguagem extravagante e estereótipos étnicos.
- Use ToolTips para ajudar a explicar ícones, que têm a vantagem adicional de se expandir automaticamente ao tamanho do texto que exibem.
- Se você retratar homens e mulheres, certifique-se de que seus papéis de gênero são adequados e que gestos e imagens do corpo humano são apropriados na cultura de destino.
- Use cores adequadamente. Por exemplo, evite usar combinações de cores associadas a bandeiras nacionais ou movimentos políticos.

Se você não tem certeza se um ícone ou bitmap é apropriado, consulte alguém no local para o qual você está projetando a aplicação.
