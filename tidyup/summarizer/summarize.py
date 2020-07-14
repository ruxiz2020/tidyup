from summarizer import Summarizer

def summarize(body):

    model = Summarizer()
    result = model(body, min_length=20)
    full = ''.join(result)

    return full


if __name__ == '__main__':

    with open('../read_it/test.txt', 'r') as file:
        data = file.read().replace('\n', ' ')

    print(summarize(data))
