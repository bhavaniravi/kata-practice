import re

movies = {
  "F001": {"title": "Ran",                     "code": "regular"},
  "F002": {"title": "Trois Couleurs: Bleu",     "code": "regular"},
}

def em_map(m):
    return f"<em>{m.group(0)}</em>"




class Customer:
    def __init__(self, name, rentals):
        self.name = name
        self.rentals = rentals

    def calculate_price(self, movie_type, days):
        if movie_type == "regular":
            amount = 2
            if days > 2: 
                amount += (days - 2) * 1.5
            return amount
        if movie_type == "new":
            return r.days * 3
        if movie_type == "childrens":
            amount = 1.5
            if days > 3:
                amount += (days - 3) * 1.5
            return amount

    def statement(self):
        statement = f"Rental Record for {self.name}\n"
        total_price = 0
        freq_points = 0
        for rental in self.rentals:
            freq_points += 1
            movie = movies[rental['movieID']]
            if movie['code'] == "new" and rental['days'] > 2:
                freq_points += 1
            price = self.calculate_price(movie['code'], rental['days'])
            statement += f"  {movie['title']} {price}\n"
            total_price += price

        statement += f'Amount owed is {total_price}\nYou earned {freq_points} frequent renter points'


        return statement

    def statement_html(self):
        return_list = []
        tab_detected = False
        for i, line in enumerate(self.statement().split("\n")):
            em_mapped = re.sub(r"(\d+(?:\.\d+)?)", em_map, line)
            if i == 0:
                em_mapped = re.sub(r"(\w+)$", em_map, em_mapped) 
                return_list.append(f"<h1>{em_mapped}</h1>")
            elif line.startswith(('\t', '  ', '    ')):
                if not tab_detected:
                    tab_detected = True
                    return_list.append("<table>")
                data = line.rsplit(" ", 1)
                data = f"<td>{data[0].strip()}</td><td>{data[1]}</td>"
                return_list.append(f"    <tr>{data}</tr>")
            elif tab_detected:
                return_list.append("</table>")
                tab_detected = False
                return_list.append(f"<p>{em_mapped}</p>")
            else:
                return_list.append(f"<p>{em_mapped}</p>")
        return "\n".join(return_list).strip()


                
            
            