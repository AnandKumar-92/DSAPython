import functools


def welcome(func):
    # @functools.wraps(func)
    def welcome_data(*args,**kwargs):

        print(f"Get data of Square root")
        if 1 == 1:
            return func(*args)

    return welcome_data


@welcome
def Adddata(data):
    return f"{data*data}"


print(Adddata(10))
