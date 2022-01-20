import gc

print("Is GC Enabled ? : ",gc.isenabled( )  )
gc.disable()
print("Is GC Enabled ? : ",gc.isenabled() )
gc.enable()
print("Is GC Enabled ? :",gc.isenabled())
