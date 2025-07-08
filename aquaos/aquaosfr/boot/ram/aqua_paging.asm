global setup_paging

[bits 32]
setup_paging:
    ; === Enable PAE ===
    mov eax, cr4
    or eax, 1 << 5
    mov cr4, eax

    ; === Enable Long Mode via EFER ===
    mov ecx, 0xC0000080
    rdmsr
    or eax, 1 << 8
    wrmsr

    ; === Load CR3 with address of PML4 table ===
    mov eax, pml4_table
    mov cr3, eax

    ret

; === Paging Structures ===
section .data
align 4096

pml4_table:
    dq pdpt_table            ; Entry 0: address of PDPT
    dq 0                     ; Remaining entries unused

pdpt_table:
    dq pd_table              ; Entry 0: address of PD
    dq 0                     ; Remaining entries unused

pd_table:
    ; Map 1 GiB using 2 MiB pages
    %assign i 0
    %rep 512
        dq (i << 21) + 0x83  ; Present + Writeable + 2 MiB page
        %assign i i + 1
    %endrep