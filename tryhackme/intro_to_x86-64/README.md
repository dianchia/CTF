# INTRO TO x86-64

## R2 CHEAT SHEET

`r2 -d elf` to open binary in debugging mode\
`aa` to analyse all\
`e asm.syntax=att` to set the desassembly syntax to AT&T\
`?` for more specific information. Such as `a?` for info about analysis\
`afl` to print list of function\
`pdf @main` Print disassembly function at main\
Intel has 16 registers:\

64bit | 32bit
------|------
%rax|%eax
%rbx|%ebx
%rcx|%ecx
%rdx|%edx
%rsi|%esi
%rdi|%edi
%rsp|%esp
%rbp|%ebp
%r8|%r8d
%r9|%r9d
%r10|%r10d
%r11|%r11d
%r12|%r12d
%r13|%r13d
%r14|%r14d
%r15|%r15d

First six registers are known as general purpose registers.\
%rsp is stack pointer.

When dealing with memory manipulation using registers, there are cases to be considered:
- (Rb, Ri) = MemoryLocation[Rb + Ri]
- D(Rb, Ri) = MemoryLocation[Rb + Ri + D]
- (Rb, Ri, S) = MemoryLocation[Rb + S * Ri]
- D(Rb, Ri, S) = MemoryLocation[Rb + S * Ri + D]

Some other important instruction are:
- `leaq source, destination`: this instruction sets destination to the address denoted by the expression in source
- `addq source, destination`: destination = destination + source
- `subq source, destination`: destination = destination - source
- `imulq source, destination`: destination = destination * source
- `salq source, destination`: destination = destination << source where << is the left bit shifting operator
- ` sarq source, destination`: destination = destination >> source where >> is the right bit shifting operator
- `xorq source, destination`: destination = destination XOR source
- `andq source, destination`: destination = destination & source
- `orq source, destination`: destination = destination | source

`db 0x562c296bc618` to set breakpoint at 0x562c296bc618\
`dc` to start execution of the program\
`dr` to view value of registers\
`px @rbp-0x4` to print value of the specific var. *Note that because we are checking the exact address, we only need to check to 0 offset. The value stored in memory is stored as hex*\
`ds` to seeks/moves onto the next instruction


## CRACKME 1
> - **What is the password?**
>> 127.0.0.1

Scp the file, and using ghidra to analyse.

## CRACKME 2
> - **What is the password?**
>> dwperuc3sv

Using ghidra we know that the password is checked reversed.