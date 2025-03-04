from memory import Memory
from emulator import CPU

# Load a test ROM
try:
    with open("roms/test.bin", "rb") as f:
        rom_data = f.read()
except FileNotFoundError:
    rom_data = bytearray([0xA9, 0x10, 0xE8, 0x00])  # LDA #$10, INX, BRK

# Initialize memory and CPU
memory = Memory()
memory.load_program(rom_data)
cpu = CPU(memory)

# Reset and run with debugging
cpu.reset()
cpu.run(debug=True)

# Print final register state
print(f"A: {cpu.a}, X: {cpu.x}, Y: {cpu.y}, PC: {hex(cpu.pc)}")
