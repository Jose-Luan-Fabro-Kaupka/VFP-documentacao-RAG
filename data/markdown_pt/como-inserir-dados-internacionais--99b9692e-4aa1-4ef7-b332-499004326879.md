# Como: inserir dados internacionais

Um aspecto importante do desenvolvimento de aplicações internacionais é saber como inserir dados em sua aplicação. Os dados podem entrar em sua aplicação de duas maneiras:
 - Os usuários inserem os dados.
- Você ou seus usuários importam os dados de arquivos existentes.

As seções a seguir discutem esses dois métodos.

# Inserir caracteres internacionais

Você pode inserir caracteres internacionais no Visual FoxPro usando seu teclado. O método exato que você usa depende do idioma com o qual está trabalhando. Em ambientes de caracteres de byte único, você pode inserir os caracteres diretamente ou pressionando uma combinação de teclas no teclado. Por outro lado, ambientes de conjunto de caracteres de byte duplo (DBCS) frequentemente fornecem um Editor de método de entrada (IME), que é uma aplicação que você pode usar para inserir caracteres.

### Inserir caracteres usando o teclado

Com um teclado internacional, você pode exibir caracteres internacionais simplesmente pressionando as teclas dedicadas a esses caracteres. Se seu teclado não tiver teclas para caracteres internacionais, você pode inserir esses caracteres usando o mapa de caracteres fornecido com o Windows (disponível no menu Acessórios) ou pressionando a tecla ALT em conjunto com teclas no teclado numérico.

Por exemplo, para digitar (código ANSI 246), pressione NUM LOCK no teclado numérico e então pressione ALT+0246. Certifique-se de usar uma fonte padrão do Windows — não FoxFont ou FoxPrint.

> **Dica:** A barra de status no mapa de caracteres mostra a combinação de teclas que corresponde a cada caractere selecionado no mapa.

> **Observação:** Você não pode inserir caracteres internacionais em FoxFont. Por exemplo, se você abrir a janela Comando, mudar para FoxFont e então pressionar uma tecla dedicada, o resultado não é o caractere na tecla. Para obter os melhores resultados, evite FoxFont em aplicações internacionais.

#### Solução de problemas

Se os caracteres não são transportados corretamente, verifique se você está usando FoxFont. Por exemplo, FoxFont é o padrão para janelas definidas pelo usuário criadas com o Comando DEFINE WINDOW (se a cláusula FONT for omitida). Certifique-se de usar a cláusula FONT para especificar uma fonte diferente da fonte padrão do Windows ao criar janelas definidas pelo usuário para que os caracteres internacionais sejam exibidos corretamente.

#### Inserir caracteres usando um IME

Se você estiver trabalhando em um ambiente IME, pode usar um Editor de método de entrada para inserir caracteres no Visual FoxPro. O IME é uma aplicação fornecida com seu ambiente que permite digitar caracteres no teclado para exibir uma seleção de caracteres internacionais e então escolher o caractere específico que deseja. Por exemplo, um IME para chinês pode permitir que você insira uma representação Pinyin de uma palavra chinesa e então exiba uma lista de caracteres que correspondem à representação. Quando você seleciona o caractere desejado, o IME cola no Visual FoxPro.

Você pode controlar quando o Visual FoxPro exibe um IME definindo a propriedade IMEMode ou chamando a Função IMESTATUS( ). Se você ativar a janela IME, o Visual FoxPro exibe automaticamente o IME quando você está editando em uma janela do sistema, como as janelas Browse ou Edit. Se você desativar a janela IME, pode invocar o IME pressionando as teclas apropriadas no teclado.

# Anexar e copiar dados internacionais

Se você estiver importando ou copiando dados de arquivos delimitados usando o Comando APPEND FROM ou Comando COPY TO, pode especificar qual caractere está sendo usado no arquivo para separar campos. Por exemplo, é comum em muitos países europeus usar ponto e vírgula (;) como delimitador de campo, enquanto os delimitadores comuns nos Estados Unidos são vírgula (,), tabulação ou espaço.

Para importar ou copiar arquivos e especificar um delimitador, adicione a cláusula DELIMITED WITH CHARACTER aos comandos APPEND FROM ou COPY TO:

```foxpro
COPY TO mytxt.txt DELIMITED WITH _ WITH CHARACTER ";"
```
