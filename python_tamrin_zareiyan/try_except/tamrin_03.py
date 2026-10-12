def safe_int(value):
    try:
        number = int(value)
        return number
    except ValueError:
        return None
    except TypeError:
        return None


zarf = safe_int('ghvhg')
print(zarf)