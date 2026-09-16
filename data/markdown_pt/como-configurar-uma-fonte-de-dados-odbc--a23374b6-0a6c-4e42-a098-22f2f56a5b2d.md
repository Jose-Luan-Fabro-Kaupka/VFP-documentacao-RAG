# Como: configurar uma fonte de dados ODBC

Antes de criar views remotas ou usar SQL pass-through, você deve instalar um driver ODBC e configurar uma fonte de dados ODBC.

# Escolhendo um driver ODBC

Para instalar os drivers ODBC para esses tipos de dados, use o programa de instalação do Visual FoxPro. Se você escolher a opção Complete install, todos os drivers são instalados.

Depois de escolher um driver, você pode usar a fonte de dados padrão ou adicionar uma fonte de dados ODBC para ele.

### Para adicionar uma fonte de dados ODBC
- Escolha o ícone Administrative Tools no Painel de controle do Windows .
- Escolha o atalho Data Sources.
- Na caixa de diálogo ODBC Data Source Administrator, clique em Add , depois selecione o driver desejado na lista Installed ODBC Driver s e escolha OK .
- Na caixa de diálogo Setup, defina os valores de opção conforme necessário e escolha OK .

Para obter informações sobre como configurar uma fonte de dados específica para o driver escolhido, escolha o botão Help na caixa de diálogo ODBC Setup.

# Instalando fontes de dados ODBC

Você pode obter suporte Open Database Connectivity (ODBC) se escolher a opção de instalação Complete ou Custom. Com ODBC, você pode acessar uma fonte de dados SQL Server a partir do Visual FoxPro; no entanto, antes de acessar a fonte de dados, você deve defini-la.
 Conectando o Visual FoxPro com fontes de dados ODBC

### Para definir uma fonte de dados
- Vá para o Painel de controle do Windows e escolha o ícone ODBC.
- Na caixa de diálogo Data Sources, escolha Add .
- Na caixa de diálogo Add Data Source, selecione o driver SQL Server ODBC e escolha OK .
- Na caixa de diálogo ODBC SQL Server Setup, insira o nome da fonte de dados, a descrição e outras informações apropriadas, e depois escolha OK .
- Na caixa de diálogo Data Sources, escolha Close .
