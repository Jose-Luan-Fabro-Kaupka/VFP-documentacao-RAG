# Trabalhando com dados remotos usando SQL pass-through

Depois de recuperar um conjunto de resultados usando SQL pass-through, você pode visualizar e controlar as propriedades do cursor do conjunto de resultados usando as funções CURSORGETPROP( ) e CURSORSETPROP( ) do Visual FoxPro. Estas são as mesmas funções que você usa para definir propriedades em um cursor de view ativo.

> **Observação:** Cursors não são objetos e, portanto, não estão vinculados ao modelo de objetos. No entanto, você pode visualizar suas propriedades, ou atributos, com CURSORGETPROP() e definir suas propriedades com CURSORSETPROP().

# Nesta seção
 **Definindo propriedades de cursor para dados remotos**
Descreve a finalidade das propriedades de cursor de dados remotos e como defini-las usando SQL pass-through e a guia Remote Data da caixa de diálogo Options.
**Como: atualizar dados remotos com SQL pass-through**
Descreve como atualizar dados remotos, incluindo detalhes específicos sobre as atualizações, como controlar o momento das atualizações remotas, usar buffer de linha e tabela otimista, detectar alterações por outros usuários, forçar atualizações e como solucionar mensagens de erro de atualização.
**Selecionando um modo de processamento SQL pass-through eficiente**
Compara e contrasta os dois tipos de modos de processamento para recuperar e atualizar dados remotos usando SQL pass-through: síncrono e assíncrono.
**Como: usar SQL pass-through de forma assíncrona**
Explica como configurar seu aplicativo cliente/servidor para usar processamento assíncrono para SQL pass-through.
**Processando vários conjuntos de resultados**
Descreve como processar vários conjuntos de resultados usando processamento em modo batch síncrono ou assíncrono e em modo não batch.
**Controle de conversão de tipos de dados**
Explica como os tipos de dados são mapeados entre ODBC ou ADO e Visual FoxPro para que você possa prever como os dados do servidor remoto serão tratados por seu aplicativo Visual FoxPro.

# Seções relacionadas
 **Aprimorando aplicativos usando tecnologia SQL pass-through**
Explica como seu aplicativo pode usar a tecnologia SQL pass-through para acessar dados remotos, executar procedimentos armazenados no servidor, executar comandos usando sintaxe nativa do servidor e criar objetos no servidor.
**Como: configurar uma fonte de dados ODBC**
Descreve como instalar um driver ODBC para que você possa usar uma fonte de dados ODBC com views remotas e SQL pass-through.
**Tratando erros de SQL pass-through**
Explica como recuperar informações sobre o erro para examinar o erro e determinar sua causa.
