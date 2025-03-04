import time

STACK_BASE = 0x0100
CPU_CLOCK_HZ = 1_000_000  # 6502 runs at ~1 MHz

CYCLE_TABLE = {
    0xA9: 2,  # LDA Immediate
    0xA2: 2,  # LDX Immediate
    0xA0: 2,  # LDY Immediate
    0x85: 3,  # STA Zero Page
    0x8D: 4,  # STA Absolute
    0xE8: 2,  # INX
    0x69: 2,  # ADC Immediate
    0xE9: 2,  # SBC Immediate
    0x48: 3,  # PHA (Push A)
    0x68: 4,  # PLA (Pull A)
    0x20: 6,  # JSR (Jump to Subroutine)
    0x60: 6,  # RTS (Return from Subroutine)
    0x00: 7,  # BRK (Break)
}

class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.pc = 0x8000  # Program Counter
        self.sp = 0xFD    # Stack Pointer
        self.a = 0        # Accumulator
        self.x = 0        # X Register
        self.y = 0        # Y Register
        self.status = 0x20  # Processor Status

    def reset(self):
        """Reset CPU"""
        self.pc = self.memory.read(0xFFFC) | (self.memory.read(0xFFFD) << 8)
        self.sp = 0xFD
        self.a = self.x = self.y = 0
        self.status = 0x20

    def fetch_byte(self):
        """Fetch a single byte"""
        value = self.memory.read(self.pc)
        self.pc += 1
        return value

    def fetch_word(self):
        """Fetch two bytes (little-endian)"""
        low = self.fetch_byte()
        high = self.fetch_byte()
        return (high << 8) | low

    def push(self, value):
        """Push a byte onto the stack"""
        self.memory.write(STACK_BASE + self.sp, value)
        self.sp = (self.sp - 1) & 0xFF

    def pop(self):
        """Pop a byte from the stack"""
        self.sp = (self.sp + 1) & 0xFF
        return self.memory.read(STACK_BASE + self.sp)

    def set_zero_negative_flags(self, value):
        """Update Zero and Negative flags"""
        self.status = (self.status & 0b01111101) | (0x80 if value & 0x80 else 0) | (0x02 if value == 0 else 0)

    def execute(self, opcode):
        """Execute instruction and return cycle count"""
        cycles = CYCLE_TABLE.get(opcode, 2)

        if opcode == 0xA9:  # LDA Immediate
            self.a = self.fetch_byte()
            self.set_zero_negative_flags(self.a)

        elif opcode == 0xA2:  # LDX Immediate
            self.x = self.fetch_byte()
            self.set_zero_negative_flags(self.x)

        elif opcode == 0xA0:  # LDY Immediate
            self.y = self.fetch_byte()
            self.set_zero_negative_flags(self.y)

        elif opcode == 0x85:  # STA Zero Page
            addr = self.fetch_byte()
            self.memory.write(addr, self.a)

        elif opcode == 0x8D:  # STA Absolute
            addr = self.fetch_word()
            self.memory.write(addr, self.a)

        elif opcode == 0xE8:  # INX
            self.x = (self.x + 1) & 0xFF
            self.set_zero_negative_flags(self.x)

        elif opcode == 0x69:  # ADC Immediate
            value = self.fetch_byte()
            result = self.a + value + (self.status & 0x01)
            self.status = (self.status & 0b11111110) | (1 if result > 255 else 0)
            self.a = result & 0xFF
            self.set_zero_negative_flags(self.a)

        elif opcode == 0xE9:  # SBC Immediate
            value = self.fetch_byte()
            result = self.a - value - (1 - (self.status & 0x01))
            self.a = result & 0xFF
            self.set_zero_negative_flags(self.a)

        elif opcode == 0x48:  # PHA (Push A)
            self.push(self.a)

        elif opcode == 0x68:  # PLA (Pull A)
            self.a = self.pop()
            self.set_zero_negative_flags(self.a)

        elif opcode == 0x20:  # JSR (Jump to Subroutine)
            addr = self.fetch_word()
            return_addr = self.pc - 1
            self.push((return_addr >> 8) & 0xFF)
            self.push(return_addr & 0xFF)
            self.pc = addr

        elif opcode == 0x60:  # RTS (Return from Subroutine)
            return_low = self.pop()
            return_high = self.pop()
            self.pc = (return_high << 8) | return_low + 1

        elif opcode == 0x00:  # BRK (Break)
            return False

        else:
            print(f"Unknown opcode: {hex(opcode)}")

        return cycles

    def run(self, debug=False):
        """Fetch-Decode-Execute loop with cycle timing"""
        running = True
        while running:
            if debug:
                self.print_state()
            
            opcode = self.fetch_byte()
            cycles = self.execute(opcode)

            time.sleep(cycles / CPU_CLOCK_HZ)

    def print_state(self):
        """Print CPU state for debugging"""
        print(f"PC: {hex(self.pc)} | A: {hex(self.a)} | X: {hex(self.x)} | Y: {hex(self.y)} | SP: {hex(self.sp)}")
