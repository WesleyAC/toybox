#!/usr/bin/env python3
import sys

from interpreter import BrainfuckProgram

class BrainfuckDebugger(object):
    """A brainfuck debugger"""
    def __init__(self, prog):
        self.prog = BrainfuckProgram(prog)
        self.singlestepping = True
        self.breakpoints = set([])
        self.last_command=""

    def step(self):
        if self.singlestepping:
            print(chr(27) + "[2J") # Clear ANSI terminal

            print("Data:")
            print(self.prog.data)
            print("    " * self.prog.dptr + "^^^")

            print("Program:")
            print(''.join(self.prog.prog))
            print(' ' * self.prog.pptr + "^")
            bpsum = 0
            for bp in sorted(self.breakpoints):
                bpspaces = bp - bpsum
                bpsum += bpspaces + 1
                print(" " * (bpspaces) + "@", end="")
            print("")

            print("Output:")
            print(''.join([chr(c) for c in self.prog.output]))

            command = input("bfdbg> ")
            self._handle_input(command)
        else:
            if self.prog.pptr in self.breakpoints:
                self.singlestepping = True
            else:
                if not self.prog.done:
                    self.prog.step()
                else:
                    self.singlestepping = True

    def _step(self, args):
        self.prog.step()

    def _run(self, args):
        self.singlestepping = False
        self.prog.step()

    def _last(self, args):
        self._handle_input(self.last_command)

    def _addbp(self, args):
        for arg in args:
            try:
                if arg != ".":
                    self.breakpoints.add(int(arg))
                else:
                    self.breakpoints.add(self.prog.pptr)
            except ValueError:
                print("Invalid value for breakpoint!\n"
                      "Breakpoint must be an integer.\n")
                input()

    def _rmbp(self, args):
        for arg in args:
            try:
                if arg != ".":
                    self.breakpoints.discard(int(arg))
                else:
                    self.breakpoints.discard(self.prog.pptr)
            except ValueError:
                print("Invalid value for breakpoint!\n"
                      "Breakpoint must be an integer.\n")
                input()

    def _over(self, args):
        pass

    def _help(self, args):
        if len(args) == 0:
            print(
            "bfdbg - a brainfuck interpreter and debugger\n"
            "Type \"help <command name>\" to see help for a specific command.\n"
            "Commands:\n")
            for cmd in self._commands:
                if cmd != "":
                    print(" * {}".format(cmd))
            print("Pressing enter will single-step (same as typing \"step\")")
        elif len(args) == 1:
            try:
                print(self._commands[args[0]][1])
            except KeyError:
                print("No such command \"{}\"!\n"
                      "Try \"help\" for a list of commands".format(args[0]))
        else:
            print("Too many arguments to \"help\"! Type \"help <command name>/\" or \"help\" to learn\n"
                  "more.")
        input("")

    def _exit(self, args):
        sys.exit(0)

    _commands = {
        "":      [_step],
        ".":     [_last,  "Runs the last command."],
        "step":  [_step,  "Steps through the program. Pressing enter (a blank line) is an alias for this."],
        "run":   [_run,   "Runs the program from here (stopping only where there is a breakpoint)."],
        "addbp": [_addbp, "Adds breakpoint(s). Usage: \"addbp <breakpoint 1> [breakpoint 2] [...]\". Breakpoints can either be an integer, or a \".\" for the current location."],
        "rmbp":  [_rmbp,  "Removes breakpoint(s). Usage: \"addbp <breakpoint 1> [breakpoint 2] [...]\". Breakpoints can either be an integer, or a \".\" for the current location."],
        "over":  [_over,  "TODO"],
        "help":  [_help,  "This command! \"help\" for general help, or \"help <command>\". But it looks like you have that one figured out!"],
        "exit":  [_exit,  "Exit bfdbg"],
    }

    def _handle_input(self, inpt):
        inpt_array = inpt.split()
        if len(inpt_array) != 0:
            cmd = inpt_array[0]
        else:
            cmd = ""
        if len(inpt_array) >= 2:
            args = inpt_array[1:]
        else:
            args = []

        if cmd != ".":
            self.last_command = inpt

        if cmd in self._commands:
            self._commands[cmd][0](self, args)
        else:
            print("Command not found!\n"
                  "Try 'help' for a list of commands")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Wrong number of parameters!\n"
              "Usage: {} filename.bf".format(sys.argv[0]))
        sys.exit(1)
    prog = open(sys.argv[1]).read()
    bfdbg = BrainfuckDebugger(prog)
    while 1:
        bfdbg.step()
