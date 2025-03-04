# 📜 6502 Emulator

A **Python-based emulator** for the **MOS 6502 CPU**, capable of executing instructions with **cycle-accurate timing**, stack operations, and various **addressing modes**. This project can also **load ROMs** and run real 6502 programs.

---

## 📌 Features

✅ **Instruction Set**: Supports key instructions like **LDA, STA, ADC, SBC, PHA, PLA, JSR, RTS, INX**  
✅ **Memory Management**: Full 64KB memory space with ROM loading  
✅ **Stack Handling**: Proper push (`PHA`), pull (`PLA`), and subroutine calls (`JSR`, `RTS`)  
✅ **Addressing Modes**: Implements **Immediate, Absolute, Zero Page, Indexed**  
✅ **Cycle-Accurate Execution**: Each opcode executes with correct **timing delays**  
✅ **Debugging Support**: **Step-by-step execution** with detailed logging  
✅ **ROM Loading**: Load and execute **real 6502 programs**  

---

## 📂 Project Structure

```
6502_emulator/
│── emulator.py         # Core CPU emulation
│── memory.py           # Memory management
│── main.py             # Entry point to run the emulator
│── roms/
│   └── test.bin        # 6502 program (ROM)
│── README.md           # Project documentation
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/sukanyaghosh74/6502-emulator.git
cd 6502-emulator
```

### 2️⃣ Install Python (if not installed)

Ensure you have **Python 3.8+** installed. You can check with:

```sh
python --version
```

---

## 🚀 Running the Emulator

### Load a ROM (Recommended)

1. Place your **6502 binary ROM** in the `roms/` folder (e.g., `roms/test.bin`).
2. Run the emulator:

   ```sh
   python main.py
   ```

3. The program will execute, and you will see debug output of the CPU state.

### Run Without a ROM

If no ROM is found, the emulator runs a small **test program** (LDA, INX, BRK).

---

## 💻 Supported Instructions

| Opcode | Mnemonic   | Description                     |
|--------|-----------|---------------------------------|
| `0xA9` | **LDA #imm**  | Load A with immediate value |
| `0xA2` | **LDX #imm**  | Load X with immediate value |
| `0xA0` | **LDY #imm**  | Load Y with immediate value |
| `0x85` | **STA zp**    | Store A into Zero Page      |
| `0x8D` | **STA abs**   | Store A into Absolute Address |
| `0xE8` | **INX**       | Increment X                 |
| `0x69` | **ADC #imm**  | Add with Carry (Immediate)  |
| `0xE9` | **SBC #imm**  | Subtract with Carry (Immediate) |
| `0x48` | **PHA**       | Push A to stack             |
| `0x68` | **PLA**       | Pull A from stack           |
| `0x20` | **JSR abs**   | Jump to Subroutine          |
| `0x60` | **RTS**       | Return from Subroutine      |
| `0x00` | **BRK**       | Break (halt execution)      |

---

## 🔍 Debugging Mode

Enable **step-by-step execution** by running:

```sh
python main.py --debug
```

This will print each instruction as it executes.

**Example Output:**

```
PC: 0x8000 | A: 0x10 | X: 0x00 | Y: 0x00 | SP: 0xFD
Executing: LDA #$10
PC: 0x8002 | A: 0x10 | X: 0x00 | Y: 0x00 | SP: 0xFD
Executing: INX
PC: 0x8003 | A: 0x10 | X: 0x01 | Y: 0x00 | SP: 0xFD
```

---

## 📄 Future Improvements

🚀 **Support for More Instructions** (AND, ORA, CMP, CPX, CPY, etc.)  
🔄 **Save/Load Emulator State**  
🎮 **6502-based Game ROM Support**  
⏳ **More Cycle Accuracy Improvements**  

---

## 📜 License

This project is **MIT Licensed**. Feel free to use, modify, and share it!

