# O programa é muito grande (Erro 1202)

O programa que o Visual FoxPro está tentando carregar não cabe na memória. Esta mensagem também pode aparecer quando o cache interno de programas fica sem espaço.

> **Observação:** Em versões anteriores ao Visual FoxPro 9.0, o tamanho de um programa ou procedimento único que pode ser carregado é limitado a 65.000 bytes.

O Visual FoxPro 9.0 permite configurar o tamanho do cache de programas. Para evitar este erro, especifique uma configuração PROGCACHE adequada no arquivo de configuração (consulte Termos especiais para arquivos de configuração). Isso é especialmente importante em cenários MTDLL.

Para obter mais informações, consulte Capacidades do sistema Visual FoxPro.
