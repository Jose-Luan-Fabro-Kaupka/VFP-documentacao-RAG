# Comando SET DEBUG

Incluído para compatibilidade retroativa. Torna as janelas Debug e Trace disponíveis ou indisponíveis no sistema de menus Visual FoxPro em versões anteriores à 5.0.

```foxpro
SET DEBUG ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Torna as janelas Debug e Trace disponíveis ou indisponíveis no sistema de menus Visual FoxPro.
**OFF**
Torna as janelas Debug e Trace indisponíveis no menu do sistema Visual FoxPro. No entanto, quando SET DEBUG estiver definido como OFF, você pode abrir a janela Debug com SET ECHO ON ou ACTIVATE WINDOW DEBUG, e pode abrir a janela Trace com SET STEP ON ou ACTIVATE WINDOW TRACE.

# Observações

Para obter mais informações sobre o uso das janelas Trace e Debug, consulte Testing and Debugging Applications.
