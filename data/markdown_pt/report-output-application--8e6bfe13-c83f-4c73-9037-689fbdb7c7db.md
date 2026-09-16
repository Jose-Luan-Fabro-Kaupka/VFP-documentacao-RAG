# Report Output Application

A Report Output Application fornece referências de objetos ReportListener ao Sistema de Relatórios do Visual FoxPro em tempo de execução. Você designa uma aplicação ou programa para essa finalidade fornecendo seu nome de arquivo na variável de sistema _REPORTOUTPUT. O arquivo ReportOutput.app, localizado no diretório principal do Visual FoxPro, fornece a implementação padrão do Visual FoxPro 9 da Report Output Application.

Os requisitos que uma Report Output Application deve atender são simples. Para uma lista completa desses requisitos e recomendações adicionais, consulte _REPORTOUTPUT System Variable.

ReportOutput.app atende a essa responsabilidade e demonstra a capacidade do Visual FoxPro de fornecer saída aprimorada, das seguintes formas:
 - Gerenciando um cache de referências de objetos Listener.
- Fornecendo novos resultados de saída, fornecendo referências a ReportListener XML Foundation Class e ReportListener HTML Foundation Class. Para obter mais informações, consulte ReportListener Foundation Classes.
- Fornecendo feedback aprimorado em tempo de execução para tipos de saída "tradicionais" de impressão e visualização, fornecendo referências a ReportListener User Feedback Foundation Class.
- Gerenciando um registro de tipos de saída para extensões adicionadas pelo usuário e novos resultados de saída.

Esta seção aborda os recursos da Report Output Application padrão (ReportOutput.app).

# Nesta seção
 **Understanding the Report Output Application**
Discute os recursos da Report Output Application padrão.
**How to: Specify an Alternate Report Output Registry Table**
Descreve como criar a tabela de registro da Report Output Application e como indicar a tabela de registro que você deseja que a Report Output Application use.
**How to: Register Custom ReportListeners and Custom OutputTypes in the Report Output Registry Table**
Descreve como adicionar suas próprias entradas à tabela de registro da Report Output Application.
**How to: Use the Report Output Application's Reference Collection**
Descreve como usar a coleção de referências da Report Output Application a objetos ReportListener.
**How to: Specify and Distribute Report Output Application Components**
Fornece instruções para distribuir a tabela de registro da Report Output Application e outros componentes com suas aplicações.

# Seções relacionadas

_REPORTOUTPUT System Variable

Understanding Visual FoxPro Object-Assisted Reporting

Considerations for Creating New Report Output Types
