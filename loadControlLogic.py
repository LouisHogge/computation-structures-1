print("Simple Python to create control logic ROM file")

f = open("control_logic", 'w')

f.write("v2.0 raw\n") # file version Logisim needs to read

f.write("24*0 ") # ???
f.write("1a0 ") # LD
f.write("10c ") # ST
f.write("0 ")
f.write("82 ") # JMP
f.write("0 ")
f.write("80 ") # BEQ
f.write("80\n") # BNE

f.write("0 ")
f.write("1d0 ") # ADD
f.write("2d0 ") # SUB
f.write("3d0 ") # MUL
f.write("4d0 ") # DIV
f.write("ad0 ") # CMPEQ
f.write("8d0 ") # CMPLT
f.write("9d0\n") # CMPLE

f.write("0 ")
f.write("5d0 ") # AND
f.write("6d0 ") # OR
f.write("7d0 ") # XOR
f.write("0 ")
f.write("bd0 ") # SHL
f.write("cd0 ") # SHR
f.write("dd0\n") # SRA

f.write("0 ")
f.write("190 ") # ADDC
f.write("290 ") # SUBC
f.write("390 ") # MULC
f.write("490 ") # DIVC
f.write("a90 ") # CMPEQC
f.write("890 ") # CMPLTC
f.write("980\n") # CMPLEC

f.write("0 ")
f.write("590 ") # ANDC
f.write("690 ") # ORC
f.write("790 ") # XORC
f.write("0 ")
f.write("b90 ") # SHLC
f.write("c90 ") # SHRC
f.write("d90") # SRAC

f.close()

print("\nScript went well")