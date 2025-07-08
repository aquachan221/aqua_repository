[org 0x7C00]
[bits 16]

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00

    mov ah, 0x02
    mov al, 40
    mov ch, 0
    mov cl, 2
    mov dh, 0
    mov dl, 0x80
    mov bx, 0x0000
    mov ax, 0x1000
    mov es, ax
    int 0x13

    jmp 0x1000:0000

times 510 - ($ - $$) db 0
dw 0xAA55