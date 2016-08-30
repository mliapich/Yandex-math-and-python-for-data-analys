import re
import numpy as np
import scipy.spatial.distance as dist


def index(words):
    w = set()
    result = {}
    for word in words:
        if word in w:
            continue
        else:
            w.add(word)
            result[word] = len(result)
    return result


def get_matrix(sentences, index):
    matrix = []
    for sentence in sentences:
        row = [0 for _ in range(len(index))]
        words = re.split('[^a-z]', sentence)
        words = filter(lambda x: x != '', words)
        for word in words:
            ind = index[word]
            row[ind] += 1
        matrix.append(row)
    return np.array(matrix)


def cos_dist(matrix):
    sentece1 = matrix[0]
    res = []
    for i in range(1, len(matrix)):
        res.append(dist.cosine(sentece1, matrix[i]))
    return(res)


def main():
    with open('cats.txt') as file:
        text = file.read().lower()
        words = re.split('[^a-z]', text)
        words = filter(lambda x: x != '', words)
        sentences = text.split('\n')
        mat = get_matrix(sentences, index(words))
        distances = cos_dist(mat)
        minimal_distances = sorted(distances)[:2]
        nums_of_sentences = [distances.index(d) for d in minimal_distances]
        print (nums_of_sentences)

if __name__ == '__main__':
    main()
