# Comando NODEFAULT

Impede que o Visual FoxPro execute seu processamento padrão de evento ou método para eventos e métodos do Visual FoxPro.

```foxpro
NODEFAULT
```

# Observações

Você pode usar NODEFAULT em qualquer lugar dentro do procedimento de evento ou método. Você também pode usar NODEFAULT em um procedimento de evento ou método no Form Designer. Por exemplo, incluir NODEFAULT no procedimento ou função do evento KeyPress impede que o Visual FoxPro insira a tecla pressionada no buffer de teclado do Visual FoxPro. Portanto, você pode criar um procedimento KeyPress para testar qual tecla é pressionada antes que a tecla seja enviada ao buffer de teclado.
