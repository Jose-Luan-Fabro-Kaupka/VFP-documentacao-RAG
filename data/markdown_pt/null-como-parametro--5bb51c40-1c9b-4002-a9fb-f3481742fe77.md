# NULL como parâmetro

Passar um valor nulo como parâmetro afeta o comportamento de muitos comandos e funções no Visual FoxPro. As regras gerais a seguir se aplicam a valores nulos passados a comandos e funções:
 - Comandos geram erros quando recebem um valor nulo.
- Funções que aceitam .NULL. como valor válido propagam .NULL. para o resultado.
- Funções que aceitam parâmetros que podem ser valores numéricos geram um erro se você fornecer .NULL. para esses parâmetros. STORE .NULL. TO n USE Mytable ALIAS &n && Expected a workarea && name or number ? SUBSTR("Hello, world",n,5) && Expected a position && in the string
- ISBLANK( ), ISDIGIT( ), ISLOWER( ), ISUPPER( ), ISALPHA( ) e EMPTY retornam false (.F.) quando recebem um valor nulo. ISNULL( ) retorna true (.T.) quando recebe um valor nulo.
- Os comandos INSERT - SQL e SELECT - SQL processam valores nulos por meio das cláusulas IS NULL e IS NOT NULL e, no caso de INSERT, UPDATE e REPLACE, colocam valores nulos em registros.
- Funções de agregação SQL ignoram em vez de propagar valores nulos.
- Funções de agregação do Visual FoxPro só propagam .NULL. se todos os valores fornecidos são valores nulos; caso contrário, qualquer valor nulo é ignorado.

Para obter mais informações sobre o uso de valores nulos na sua aplicação, consulte Trabalhando com tabelas (Visual FoxPro).
