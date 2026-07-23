is_logged_in = True


def login_required(func):

    def wrapper(*args, **kwargs):

        if is_logged_in:
            func(*args, **kwargs)
        else:
            print("Access Denied! Please log in first.")

    return wrapper


@login_required
def dashboard():
    print("Welcome to your Dashboard")


dashboard()