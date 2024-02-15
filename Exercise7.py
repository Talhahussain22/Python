import os
def rename(typ):
        files=os.listdir("Exercise7")
        i=0
        for file in files:
            if file.endswith(typ):
                os.rename(f"Exercise7\{file}",f"Exercise7\photo{i}{typ}")
            i+=1


rename(".png")
