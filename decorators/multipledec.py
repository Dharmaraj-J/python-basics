def split(ref):
    def process1():
        data = ref()
        return data.split()

    return process1


def concatinate(ref):
    def process2():
        word = ref()
        return word + ['how','are','you']
    return process2


@concatinate
@split
def fun():
    return "hi friends"

print(fun())


