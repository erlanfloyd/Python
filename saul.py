def decorator(func_to_decorate):
    def wrapper():
        print("Saul")
        func_to_decorate()
        print("Alvarez")
    return wrapper


@decorator
def mexico():
    print("Canelo")
mexico()
