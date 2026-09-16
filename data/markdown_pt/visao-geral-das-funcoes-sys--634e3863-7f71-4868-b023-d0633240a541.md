# Visão geral das funções SYS( )

Retorna informações do sistema do Microsoft Visual FoxPro ou define seu comportamento.

```foxpro
SYS()
```

# Valor de retorno

Character, Numeric ou referência de objeto

# Observações

As funções SYS( ) do Visual FoxPro retornam valores de caracteres ou numéricos ou referências de objeto que contêm informações úteis do sistema.

Essas funções também são usadas para definir várias configurações do sistema Visual FoxPro.

A tabela a seguir mostra o que cada função SYS( ) retorna:

| Função | Informação retornada |
| --- | --- |
| SYS(0) | Informações da máquina de rede. |
| SYS(1) | Data juliana do sistema. |
| SYS(2) | Segundos desde a meia-noite. |
| SYS(3) | Nome de arquivo válido. |
| SYS(5) | Unidade ou volume padrão. |
| SYS(6) | Dispositivo de impressora atual. |
| SYS(7) | Arquivo de formato atual. |
| SYS(9) | Número de série do Visual FoxPro. |
| SYS(10) | Cadeia de caracteres do número do dia juliano. |
| SYS(11) | Número do dia juliano. |
| SYS(12) | Memória disponível em bytes. |
| SYS(13) | Status da impressora. |
| SYS(14) | Expressão de índice. |
| SYS(15) | Tradução de caracteres. |
| SYS(16) | Nome do arquivo de programa em execução. |
| SYS(17) | Processador em uso. |
| SYS(18) | Controle atual. |
| SYS(20) | Transformar texto alemão. |
| SYS(21) | Número do índice controlador. |
| SYS(22) | Nome da tag ou índice controlador. |
| SYS(23) | Uso de memória EMS do FoxPro. |
| SYS(24) | Limite de memória EMS. |
| SYS(100) | Configuração do console. Incluída para compatibilidade com versões anteriores. Use SET("CONSOLE") em vez disso. |
| SYS(101) | Configuração de dispositivo. Incluída para compatibilidade com versões anteriores. Use SET("DEVICE") em vez disso. |
| SYS(102) | Configuração de impressora. Incluída para compatibilidade com versões anteriores. Use SET("PRINTER") em vez disso. |
| SYS(103) | Configuração de talk. Incluída para compatibilidade com versões anteriores. Use SET("TALK") em vez disso. |
| SYS(602) | Configuração de Bitmap. |
| SYS(987) | Mapear Dados Remotos para ANSI. |
| SYS(1001) | Memória do Visual FoxPro. |
| SYS(1011) | Número de Handles de Memória. |
| SYS(1016) | Uso de memória de objeto do usuário. |
| SYS(1023) | Habilitar modo de diagnóstico da Ajuda. |
| SYS(1024) | Desabilitar modo de diagnóstico da Ajuda. |
| SYS(1037) | Caixa de Diálogo Configuração de Página. |
| SYS(1104) | Limpar Memória em Cache. |
| SYS(1269) | Informações de Propriedade. |
| SYS(1270) | Localização do Objeto. |
| SYS(1271) | Arquivo .SCX do Objeto. |
| SYS(1272) | Hierarquia do Objeto. |
| SYS(1500) | Ativar um item de menu. |
| SYS(2000) | Correspondência de curinga de nome de arquivo. |
| SYS(2001) | Status do comando SET. |
| SYS(2002) | Ativar ou desativar ponto de inserção. |
| SYS(2003) | Diretório atual. |
| SYS(2004) | Diretório de inicialização do Visual FoxPro. |
| SYS(2005) | Arquivo de recursos atual. |
| SYS(2006) | Placa gráfica atual. |
| SYS(2007) | Valor de checksum. |
| SYS(2010) | Configurações do arquivo CONFIG.SYS. |
| SYS(2011) | Status de bloqueio atual. |
| SYS(2012) | Tamanho do bloco de campo memo. |
| SYS(2013) | Cadeia de caracteres de nome do menu do sistema. |
| SYS(2014) | Caminho mínimo. |
| SYS(2015) | Nome de procedimento exclusivo. |
| SYS(2016) | Nome da janela SHOW GETS. |
| SYS(2017) | Valor de checksum baseado no registro atual na área de trabalho atual. |
| SYS(2018) | Parâmetro de mensagem de erro. |
| SYS(2019) | Nome e localização do arquivo de configuração. |
| SYS(2020) | Espaço livre em disco padrão. |
| SYS(2021) | Expressão de índice filtrado. |
| SYS(2022) | Tamanho do cluster (bloco) do disco. |
| SYS(2023) | Caminho Temporário. |
| SYS(2024) | Detectar cancelamento de relatório |
| SYS(2029) | Tipo de tabela. |
| SYS(2030) | Depuração. |
| SYS(2040) | Detectar Status do Relatório. |
| SYS(2060) | Configuração de tratamento de evento da roda do mouse. |
| SYS(2300) | Adicionar ou Remover Página de Código. |
| SYS(2325) | Retorna o WHANDLE de uma janela cliente a partir do WHANDLE da janela pai. |
| SYS(2326) | Retorna um WHANDLE Visual FoxPro a partir do hWnd de uma janela. |
| SYS(2327) | Retorna o hWnd de uma janela a partir do WHANDLE de uma janela Visual FoxPro. |
| SYS(2333) | Suporte a Interface Dupla ActiveX. |
| SYS(2334) | Modo de Invocação do Servidor de Automação. |
| SYS(2335) | Modo de Servidor Não Assistido. |
| SYS(2336) | Suporte a Seção Crítica. |
| SYS(2339) | Chamar CoFreeUnusedLibraries quando o objeto COM é liberado. |
| SYS(2340) | Suporte a Serviço NT. |
| SYS(2410) | Tipo de manipulador de erros para um erro. |
| SYS(2450) | Ordem do Caminho de Pesquisa do Aplicativo. |
| SYS(2600) | Retornar Ponteiro Como Cadeia de Caracteres. |
| SYS(2700) | Habilita Temas do Windows XP. |
| SYS(2800) | Suporte de Acessibilidade. |
| SYS(2801) | Suporte de Rastreamento de Eventos. |
| SYS(2910) | Define ou retorna o número de itens a exibir em caixas de listagem suspensa. |
| SYS(3004) | Retornar ID de Localidade. |
| SYS(3005) | Definir ID de Localidade. |
| SYS(3006) | Definir IDs de Idioma e Localidade. |
| SYS(3007) | Especifica um script de idioma de fonte para ToolTips. |
| SYS(3008) | ToolTips de Hiperlink. |
| SYS(3009) | Justificação de texto bidirecional para ToolTips. |
| SYS(3050) | Definir Tamanho da Memória Buffer. |
| SYS(3051) | Definir Intervalo de Repetição de Bloqueio. |
| SYS(3052) | Substituir Bloqueio SET REPROCESS. |
| SYS(3053) | Handle de Ambiente ODBC. |
| SYS(3054) | Nível de Otimização de Consulta Rushmore. |
| SYS(3055) | Complexidade de Cláusula FOR e WHERE. |
| SYS(3056) | Ler Configurações do Registro. |
| SYS(3065) | Cache Interno de Programa. |
| SYS(3092) | Nível de Otimização de Consulta Rushmore de Saída |
| SYS(3095) | Ponteiro IDispatch. |
| SYS(3096) | Referência de Objeto IDispatch. |
| SYS(3097) | Adicionar Referência ao Objeto. |
| SYS(3098) | Liberar Referência de Objeto. |
| SYS(3099) | Modo de Compatibilidade do Mecanismo de Dados SQL. |
| SYS(3101) | Tradução de Página de Código COM |
