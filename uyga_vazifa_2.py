def funk(arg):
    nmr=str(arg)

    if nmr==nmr[::-1]:
        return True
    else:
        return False
    
print(funk(1232))