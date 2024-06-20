from cmd import Cmd

class MathOps(Cmd):
    def do_add(self, args):
        '''add two numbers'''
        num = args.split()
        print('addition:', int(num[0]) + int(num[1]))

    def do_sub(self, args):
        '''subtract two numbers'''
        num = args.split()
        print('subtraction:', int(num[0]) - int(num[1]))

    def do_mul(self, args):
        '''multiply two numbers'''
        num = args.split()
        print('multiplication:', int(num[0]) * int(num[1]))

    def do_div(self, args):
        '''perform division'''
        num = args.split()
        print('division:', int(num[0]) / int(num[1]))

    def do_EOF(self, args):
        
        return True

op = MathOps()
op.prompt = "->"
op.cmdloop("loop starts. Press ^D to exit")
