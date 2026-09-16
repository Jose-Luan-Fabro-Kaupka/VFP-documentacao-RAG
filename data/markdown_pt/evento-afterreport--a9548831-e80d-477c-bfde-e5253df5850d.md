# Evento AfterReport

Ocorre diretamente após o Report Engine terminar de processar um formulário de relatório.

```foxpro
PROCEDURE Object.AfterReport
```

#### Parâmetros

Nenhum.

# Observações

Aplica-se a: ReportListener Object.

Ao concluir a execução do relatório, após o evento AfterBand final, o Report Engine dispara o evento AfterReport. Neste momento, a sessão de dados privada especificada pela propriedade FRXDataSession ainda contém sua cópia somente leitura do arquivo de definição de relatório (frx). O trabalho de impressão (se o relatório estiver imprimindo) ainda está aberto.

Quando AfterReport retorna, a saída é finalizada (por exemplo, o trabalho de impressão é fechado) se não houve a palavra-chave NOPAGEEJECT neste comando REPORT FORM.

> **Observação:** Para obter mais informações sobre a ordem dos eventos em uma execução de relatório, consulte Understanding Visual FoxPro Object-Assisted Reporting .
