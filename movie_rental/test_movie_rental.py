from movie_rental import Customer
import pytest

params = [
    (
        ({
  "name": "martin",
  "rentals": [
    {"movieID": "F001", "days": 3},
    {"movieID": "F002", "days": 1},
  ]
},
            """Rental Record for martin
  Ran 3.5
  Trois Couleurs: Bleu 2
Amount owed is 5.5
You earned 2 frequent renter points""",
            """<h1>Rental Record for <em>martin</em></h1>
<table>
    <tr><td>Ran</td><td>3.5</td></tr>
    <tr><td>Trois Couleurs: Bleu</td><td>2</td></tr>
</table>
<p>Amount owed is <em>5.5</em></p>
<p>You earned <em>2</em> frequent renter points</p>""",
        )
    )
]


class TestRental:
    @pytest.mark.parametrize("data, statement, htmlstatement", params)
    def test_html_statement(self, data, statement, htmlstatement):
        rental = Customer(**data)
        assert rental.statement() == statement
        result = rental.statement_html()
        assert result == htmlstatement
