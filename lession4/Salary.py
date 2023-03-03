from mrjob.job import MRJob
import itertools
cols = 'Name,SubName,JobTitle,AgencyId,Agency,HireDate,AnnualSalary,GrossPay'.split(',');

class SalaryMax(MRJob):
    def mapper(self, key, value):
        row = dict(itertools.zip_longest(cols, [a.replace('\"',"").strip() for a in value.split(",")], fillvalue = 0 ));
        
        try:
            yield('salary', (float(row['AnnualSalary'][1:])))
        except ValueError:
            self.increment_counter('warn','missing Annual Salary', 1)

        try:
            if(row['GrossPay']):
                yield('gross', (float(row['GrossPay'][1:])))
        except ValueError:
            self.increment_counter('warn','missing Gross Salary', 1) 

    def reducer(self, key, values):
        topten = []
        for p in values:
            topten.append(p)
            topten.sort()
            topten = topten[-10:]
        for p in topten:
            yield key, p
            
    combiner = reducer

if __name__ == '__main__':
    SalaryMax.run()
