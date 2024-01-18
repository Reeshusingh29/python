# Custom exception raise karein
def raise_custom_error():
    raise Exception("This is a custom error.")

# Try block mein function call karein aur exception handle karein
try:
    raise_custom_error()
except Exception as e:
    print(f"Caught a custom exception: {e}")
finally:
    print("Finally block always executes.")
