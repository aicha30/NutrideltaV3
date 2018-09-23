 from model import CsvModel

 class MyCSvModel(CsvModel):
    aliment_name = CharField()
    retinol = DecimalField()

    class Meta:
        delimiter = ";"
        dbModel = aliment