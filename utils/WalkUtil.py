import os


def walk(
    dir,
    name = lambda fn: True,
    path = lambda rt: False):

    modules = []

    for root, dirs, files in os.walk(dir, topdown=False):
        for f in files:
            if path(root):
                continue
                
            if name(f) and not (form:=os.path.join(root, f).split(".")[0].replace("/", ".")) in modules:
                modules.append(form)
    
    return modules
