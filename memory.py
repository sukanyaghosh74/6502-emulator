class Memory:
    def __init__(self, size=0x10000):
        """Initialize 6502 memory (64KB)"""
        self.memory = bytearray(size)

    def read(self, address):
        """Read a byte from memory"""
        return self.memory[address]

    def write(self, address, value):
        """Write a byte to memory"""
        self.memory[address] = value

    def load_program(self, program, start_address=0x8000):
        """Load a program into memory"""
        self.memory[start_address:start_address + len(program)] = program
        self.memory[0xFFFC] = start_address & 0xFF
        self.memory[0xFFFD] = (start_address >> 8) & 0xFF
