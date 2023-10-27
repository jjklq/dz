def is_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_type = kwargs.get('user_type')
            if user_type == required_role:
                return func(*args, **kwargs)
            else:
                raise ValueError("Permission denied")

        return wrapper

    return decorator

# Usage
@is_role('admin')
def show_customer_receipt(**kwargs):
    # Some operation
    print("Showing customer receipt")

# Test with different user roles
try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)

show_customer_receipt(user_type='admin')



def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {e}")

    return wrapper

# Usage
@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})
