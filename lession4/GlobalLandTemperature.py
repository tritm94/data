from mrjob.job import MRJob
from mrjob.step import MRStep

class GlobalTemperaTureCount(MRJob):
    
    def mapper(self, key, value):
        dt, AverageTemperature, AverageTemperatureUncertainty, State, Country = value.split(",")
        year = int(dt[:4])
        if (year >= 1900):
            key = State + 'co nhiet do' + AverageTemperature + 'thuoc quoc gia' + Country
            yield(key, 1)

    def combiner(self, key, values):
        yield(key, sum(values))


    def reducer(self, key, values):
        yield (key, sum(values))


    def steps(self):
        return [
            MRStep(
                mapper= self.mapper,
                combiner= self.combiner,
                reducer=self.reducer
            )
        ]

if __name__ == '__main__':
    GlobalTemperaTureCount.run()
