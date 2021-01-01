import re

def em_map(m):
    return f"<em>{m.group(0)}</em>"

class Rental:
    def __init__(self, statement):
        self._statement = statement

    def statement(self):
        return self._statement

    def statement_html(self):
        return_list = []
        tab_detected = False
        for i, line in enumerate(self._statement.split("\n")):
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


                
            
            