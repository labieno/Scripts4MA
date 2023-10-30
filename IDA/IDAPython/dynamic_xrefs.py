# This scripts identifies dynamic calls and create cross references to enrich the references function graph

# It must be executed while debugging after rebuild the IAT with renimp.idc

# If errors are met when step over the calls, the debugger must be manually carried through the instruction (putting BPs)

import idc
import idautils
import idaapi

print("+++++++++++++++++++++++++++++++++++++++++")
print("Identifying dynamic calls:")

JMPS = [idaapi.NN_jmp, idaapi.NN_jmpfi, idaapi.NN_jmpni]
CALLS = [idaapi.NN_call, idaapi.NN_callfi, idaapi.NN_callni]

def condicion(line):        
        addr = next_head(here())
        #addr = here()
        #print(hex(addr))
        
        func = idaapi.get_func(addr) # funcion origen del xref
        #print(func) 
        #print(idc.get_func_name(addr))

        #print(idc.print_operand(addr, 0)) #Print the register that it's called, e.g. "eax"
        reg = idc.print_operand(addr, 0)
        dir_fun = idc.get_reg_value(reg) # funcion destino
        #print(hex(dir_fun), reg)
        for xref in idautils.XrefsTo(dir_fun, 1):
                # To gather info
                #print (xref.type, idautils.XrefTypeName(xref.type), hex(xref.frm), hex(xref.to), xref.iscode)
                ida_xref.add_cref(addr, xref.frm, fl_CN)
                print("xref created")

        del_bpt(line)

# Definimos breakpoint condicional:

def bp(address, cond):
        add_bpt(line)
        bpt = idaapi.bpt_t()
        idaapi.get_bpt(line, bpt)
        bpt.elang = "Python"
        bpt.condition = cond
        idaapi.update_bpt(bpt)

# Identificamos calls dinamicos y ponemos el BP:

for func in idautils.Functions():
	flags = idc.get_func_attr(func, FUNCATTR_FLAGS)
	if flags & FUNC_LIB or flags & FUNC_THUNK:
		continue
	dism_addr = list(idautils.FuncItems(func))
	for line in dism_addr:
                ins = ida_ua.insn_t()
                idaapi.decode_insn(ins, line)
                if ins.itype in CALLS or ins.itype in JMPS:
                        if ins.Op1.type == o_reg:
                                print (hex(line), idc.generate_disasm_line(line, 0), idc.get_func_name(line))
                                bp(line, 'condicion(' + str(line) + ')')
                                print("bp set")