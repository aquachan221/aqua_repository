extern kernel_main

[bits 32]
    mov eax, cr0
    or eax, 1 << 31  ; Enable paging
    mov cr0, eax

    jmp 0x18:longmode_label

[bits 64]
longmode_label:
    mov ax, 0x10
    mov ds, ax
    mov ss, ax
    mov rsp, 0x80000
    call kernel_main