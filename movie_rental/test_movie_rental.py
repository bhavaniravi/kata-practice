from movie_rental import Rental
import pytest

params = [
    (
        (
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
    def test_statement(self):
        rental = Rental(statement="hello")
        assert rental.statement() == "hello"
        assert rental._statement == "hello"

    @pytest.mark.parametrize("input, expected", params)
    def test_html_statement(self, input, expected):
        rental = Rental(statement=input)
        assert rental.statement() == input
        result = rental.statement_html()
        print (result, "\n\n", expected)
        assert result == expected
