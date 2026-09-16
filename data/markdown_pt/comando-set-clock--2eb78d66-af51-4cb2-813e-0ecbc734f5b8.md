# Comando SET CLOCK

Determina se o Visual FoxPro exibe o relógio do sistema e especifica a localização do relógio na janela principal do Visual FoxPro.

```foxpro
SET CLOCK ON | OFF | STATUS
-or-
SET CLOCK TO [nRow, nColumn]
```

#### Parâmetros
 **ON**
Exibe o relógio no canto superior direito da janela principal do Visual FoxPro.
**OFF**
(Padrão) Remove o relógio da barra de status ou da janela principal do Visual FoxPro.
**STATUS**
Exibe o relógio na barra de status gráfica. Emita SET STATUS BAR ON para exibir a barra de status gráfica.
**TO [ nRow , nColumn ]**
Usando coordenadas de linha e coluna, especifica onde o relógio é exibido na janela principal do Visual FoxPro. Use SET CLOCK TO sem as coordenadas para exibir o relógio em sua posição padrão no canto superior direito da janela principal do Visual FoxPro. Se você colocar o relógio na barra de status gráfica com SET CLOCK STATUS e especificar uma localização na janela principal do Visual FoxPro com TO nRow , nColumn , o Visual FoxPro remove o relógio da barra de status gráfica e o coloca na localização que você especificar.
