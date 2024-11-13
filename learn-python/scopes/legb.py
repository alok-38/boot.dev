# LEGB Rule in Action
# Lexical, Enclosed, Global and Built-in scopes in action

# Global scope
x = 100

def outer():
    # Enclosing scope
    x = 200

    def inner():
        # Local scope
        print("Local x inside inner:", x)

    inner()

    def modify_enclosing():
        nonlocal x
        x = 400

    modify_enclosing()
    print("Enclosing x after modify_enclosing:", x)

outer()
print("Global x after outer execution:", x)

