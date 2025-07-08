import os
import subprocess
import sys
import time
# === 🛠 Toolchain Paths ===
TOOLS = {
    "NASM": r"F:\aqua\aqua.os\nasm\nasm.exe",
    "LD":   r"F:\aqua\aqua.os\x86_64-elf-binutils\bin\x86_64-elf-ld.exe",
    "GCC":  r"F:\aqua\aqua.os\i386-elf-gcc-windows-x86_64\i386-elf-gcc\bin\i386-elf-gcc.exe",
    "QEMU": r"F:\aqua\aqua.os\qemu-portable-20241220\qemu-portable-20241220\qemu-system-x86_64.exe"
}

# === 📄 Input Files ===
FILES = {
    "BOOT_ASM":       r"F:\aqua\aqua.os\aquaosfr\boot\aqua_boot.asm",
    "STAGE_ASM": [
        r"F:\aqua\aqua.os\aquaosfr\boot\ram\aqua_gdt.asm",
        r"F:\aqua\aqua.os\aquaosfr\boot\modes\aqua_pmode.asm",
        r"F:\aqua\aqua.os\aquaosfr\boot\ram\aqua_paging.asm",
        r"F:\aqua\aqua.os\aquaosfr\boot\modes\aqua_longmode.asm",
        r"F:\aqua\aqua.os\aquaosfr\boot\aqua_kernel64.asm"
    ],
    "LINKER_SCRIPT":  r"F:\aqua\aqua.os\aquaosfr\aqua_linker.ld"
}

# === 📦 Output Files ===
OUTPUT = {
    "BOOT_BIN":   r"F:\aqua\aqua.os\build\aqua_boot.bin",
    "KERNEL_ELF": r"F:\aqua\aqua.os\build\kernel.elf",
    "FULL_IMAGE": r"F:\aqua\aqua.os\build\aquaos.img"
}

# === 🧼 Make sure output dir exists ===
os.makedirs(os.path.dirname(OUTPUT["BOOT_BIN"]), exist_ok=True)

# === 🔧 Assemble bootloader ===
print("🔧 Assembling bootloader...")
subprocess.run([
    TOOLS["NASM"], "-f", "bin", FILES["BOOT_ASM"], "-o", OUTPUT["BOOT_BIN"]
], check=True)

# === 🔧 Assemble stage .asm files with proper format ===
obj_files = []
for src_path in FILES["STAGE_ASM"]:
    name = os.path.basename(src_path).replace(".asm", ".o")
    out_path = f"F:\\aqua\\aqua.os\\build\\{name}"
    print(f"🔧 Assembling {os.path.basename(src_path)}...")

    # Use elf64 for longmode and kernel64, elf for others
    format = "elf64" if "longmode" in name or "kernel64" in name else "elf"
    subprocess.run([TOOLS["NASM"], "-f", format, src_path, "-o", out_path], check=True)

    obj_files.append(out_path)

# === 🔗 Link kernel ELF ===
print("🔗 Linking kernel ELF...")
subprocess.run([
    TOOLS["LD"], "-n", "-T", FILES["LINKER_SCRIPT"], "-o", OUTPUT["KERNEL_ELF"]
] + obj_files, check=True)

print("creating image")
with open(OUTPUT["FULL_IMAGE"], "wb") as img:
    with open(OUTPUT["BOOT_BIN"], "rb") as boot:
        img.write(boot.read())
    with open(OUTPUT["KERNEL_ELF"], "rb") as kernel:
        img.write(kernel.read())

print(f"build complete: {OUTPUT['FULL_IMAGE']}")

print("qemu")
subprocess.run([
    TOOLS["QEMU"],
    "-drive", f"format=raw,file={OUTPUT['FULL_IMAGE']}",
    "-m", "128M",
    "-no-reboot",
    "-serial", "stdio"
])

def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

time.sleep(10)
clear()