# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:52:05 2017

@author: cLennon
"""
#The first problem set involves building a debugger

import sys




stepping = False #indicates whether we are stepping line by line through the program or
                # running the program
watchpoints = {'c': True}
breakpoint={21:True} #points at which to stop to examine variable values (dict line $ to values)

# Our buggy program
def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out


# main program that runs the buggy program
def main():
    print(remove_html_markup('xyz'))
    print(remove_html_markup('"<b>foo</b>"'))
    print(remove_html_markup("'<b>foo</b>'"))



#tracit is called on every line, stepping by line or stopping at breakpoints
#printing our events and diagnostic information.  Then receive commands and resume action
#


def traceit(frame,event,arg):
    global stepping
    global breakpoints
    
    if event=='Line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print(event, frame.f_lineno,frame.f_code.co_name, frame.f_locals)
                command = input_command()
                resume = debug(command, arg, frame.f_locals)
    return traceit

def debug(command, my_locals):
    global stepping
    global breakpoints
    
    if command.find(' ') > 0:
        arg = command.split(' ')[1] #for 2 word commands takes second word as arg
    else:
        arg = None

    if command.startswith('s'):     # step
        stepping = True
        return True
    elif command.startswith('c'):   # continue
        stepping = False
        return True
    elif command.startswith('p'):    # print 
        if not arg:
            print(my_locals)
        else:
            if my_locals.has_key(arg):
                print( arg + " = " + repr(my_locals.get(arg)))         
            else:
                print( "No such variable:  "+arg)
    elif command.startswith('w'):    # watch variable
        if arg:
            if my_locals.has_key(arg):
                watchpoints[arg]=True
            else:
                print("No such variable "+arg)
        else:
            print( 'You must supply a variable name')
            
    elif command.startswith('b'):
        if arg:
            breakpoints[int(arg)]=True
        else:
            print('You must supply a line number')
    elif command.startswith('q'):   # quit
        sys.exit(0)
    else:
        print("No such command", repr(command))
        
    return False
        
commands = ["p", "s", "p tag", "p foo", "q"]

def input_command():
   # command = input("(my-spyder) ")
    global commands
    command = commands.pop(0)
    return command        
sys.settrace(traceit)
main()
sys.settrace(None)


#below is a test program 