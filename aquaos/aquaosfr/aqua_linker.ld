ENTRY(_start)

SECTIONS
{
    /* Load the kernel at 1 MiB */
    . = 0x100000;

    /* Text (code) section */
    .text :
    {
        *(.text)
    }

    /* Read-only data */
    .rodata :
    {
        *(.rodata)
    }

    /* Initialized data */
    .data :
    {
        *(.data)
    }

    /* Uninitialized data (zeroed at runtime) */
    .bss :
    {
        *(.bss)
        *(COMMON)
    }
}