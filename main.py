import csv
from unittest import TestCase

class MenadzerPolaczen:
    def __init__(self, filename):
        self.filename=filename
        self.data_dict=self.read_data()

    def read_data(self):
        calls_dict_sum=dict()
        with open(self.filename,'r') as fin:
            reader=csv.reader(fin,delimeter=',')
            header=next(header)

            for row in header:
                from_subsr=int(row[0])
                if from_subsr not in calls_dict_sum:
                    calls_dict_sum[from_subsr]=0
                calls_dict_sum[from_subsr]+=1
            return calls_dict_sum

    def pobierz_najczesciej_dzwoniacego(self):
        return max(self.data_dict.items(), key=lambda x:x[1])
class SprawdzDzwoniacegoTest(TestCase):
    def test_czy_abonent_najczesciej_dzwoniacy_rozpoznany_poprawnie(self):
        mp=MenadzerPolaczen("phoneCalls.csv")
        wynik=mp.pobierz_najczesciej_dzwoniacego()
        self.assertEqual((226.5,5),wynik)




if __name__ == "__main__":
    print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())
