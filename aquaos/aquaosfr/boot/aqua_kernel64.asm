[bits 64]
global kernel_main
kernel_main:
    ; Simple banner
    mov rsi, banner
.print:
    lodsb
    test al, al
    jz .done
    mov ah, 0x0E
    int 0x10
    jmp .print
.done:
    hlt

banner db "holy god", 0