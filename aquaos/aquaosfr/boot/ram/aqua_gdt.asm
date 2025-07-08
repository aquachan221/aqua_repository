global gdt_descriptor
[bits 16]
gdt_start:
    dq 0x0000000000000000
    dq 0x00CF9A000000FFFF  ; 32-bit code
    dq 0x00CF92000000FFFF  ; 32-bit data
    dq 0x00AF9A000000FFFF  ; 64-bit code

gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start