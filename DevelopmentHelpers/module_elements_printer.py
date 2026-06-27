
# Import to study elements inside a module.

def print_module_elements(module_variable):
    print(f"============ [{module_variable.__name__}] ==============")
    for attrib in module_variable.__dir__():
        if attrib[:2] != "__":
            print(f"--> {attrib}")
    print(f"============ [{module_variable.__name__}] ==============")