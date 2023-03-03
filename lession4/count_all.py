from mrjob.job import MRJob
class MRWorldCount(MRJob):
    def mapper(self, key, value):
        for word in value.split():
            yield "chars", len(value)
            yield "lines", 1
            yield "words", len(value.split(" "))
            # yield(word, 1)
    def reducer(self, key, values):
        yield(key, sum(values))
    
if __name__ == '__main__':
    MRWorldCount.run();