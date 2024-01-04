import hidden_4
if __name__ == "__main__":
    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(module_names):
        print(name)




#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
