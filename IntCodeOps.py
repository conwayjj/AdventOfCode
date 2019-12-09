def _getParam(proc, offset, mode):
    param = None
    _valMem(proc, proc.PC+offset)

    # Position Mode
    if mode == '0':
        _valMem(proc, proc.source[proc.PC+offset])
        param = proc.source[proc.source[proc.PC+offset]]

    # Immediate Mode
    elif mode == '1':
        param = proc.source[proc.PC+offset]

    # Relative Base Mode
    elif mode == '2':
        _valMem(proc, proc.source[proc.PC+offset] + proc.RB)
        param = proc.source[proc.source[proc.PC+offset] + proc.RB]

    return param

def _getTarget(proc, target, mode):
    out = None
    _valMem(proc, proc.PC + target)
    
    if mode == '0':
        _valMem(proc, proc.source[proc.PC + target])
        out = proc.source[proc.PC + target]

    elif mode == '1':
        print ("INVALID Mode 1 for Target")

    elif mode == '2':
        _valMem(proc, proc.source[proc.PC + target] + proc.RB)
        out = proc.source[proc.PC + target] + proc.RB

    return out

def _getParams(proc, mode, numParams, target = None):
    params = []

    for i in range(numParams):
        params.append(_getParam(proc, i+1, mode[i]))

    if target != None:
        target = _getTarget(proc, target, mode[target-1])

    return params, target

def _valMem(proc, addr):
    if addr not in proc.source:
        if addr >= 0:
            proc.source[addr] = 0
        else:
            print("INVALID ADDRESS", addr)
        
#99 HALT
def halt(proc, mode):
    return -1

#01 ADD
def add(proc, mode):
    params, target = _getParams(proc, mode, 2, target = 3)
    proc.source[target] = params[0] + params[1]
    return proc.PC + 4

#02 MUL
def mul(proc, mode):
    params, target = _getParams(proc, mode, 2, target = 3)
    proc.source[target] = params[0] * params[1]
    return proc.PC + 4

#03 INP
def inp(proc, mode):
    params, target = _getParams(proc, mode, 0, target = 1)
    proc.source[target] = proc.getInput()
    return proc.PC + 2

#04 OUT
def out(proc, mode):
    params, target  = _getParams(proc, mode, 1)
    proc.sendOutput(params[0])
    return proc.PC+ 2

#05 JNZ
def jnz(proc, mode):
    params, target  = _getParams(proc, mode, 2)
    return proc.PC + 3 if params[0] == 0 else params[1]

#06 JEZ
def jez(proc, mode):
    params, target  = _getParams(proc, mode, 2)
    return proc.PC + 3 if params[0] != 0 else params[1]

#07 LT
def lt(proc, mode):
    params, target = _getParams(proc, mode, 2, target = 3)
    proc.source[target] = 1 if params[0] < params[1] else 0
    return proc.PC + 4

#08 EQ
def eq(proc, mode):
    params, target  = _getParams(proc, mode, 2, target = 3)
    proc.source[target] = 1 if params[0] == params[1] else 0
    return proc.PC + 4

#09 SRB
def srb(proc, mode):
    params, target  = _getParams(proc, mode, 1)
    proc.RB = proc.RB + params[0]
    return proc.PC + 2



OpCodes =   {99: halt,
             1: add,
             2: mul,
             3: inp,
             4: out,
             5: jnz,
             6: jez,
             7: lt,
             8: eq,
             9: srb}
