# bfdbg
#### A debugger and interpreter for [brainfuck](http://esolangs.org/wiki/brainfuck)

This directory contains both a brainfuck interpreter and debugger. They are very hacky and incomplete (The `,` command is not implemented).

## Interpreter:

```
interpreter.py program.bf
```

This will run the program, printing output as it goes. The `,` command is not implemented, so it isn't very useful.

## Debugger:

```
debugger.py program.bf
```

`help` will display all commands.
You can press enter or type `step` to step through to program.

It supports breakpoints, single-stepping, and running.

Like the interpreter, it does not support the `,` command.
