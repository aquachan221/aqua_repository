%include "F:/aqua/aqua.os/aquaosfr/boot/ram/aqua_gdt.asm"
extern setup_paging

[bits 16]
    cli
    lgdt [gdt_descriptor]

    mov eax, cr0
    or eax, 0x1
    mov cr0, eax

    jmp 0x08:pm_label

[bits 32]
pm_label:
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax

    mov esp, 0x90000

    call setup_paging