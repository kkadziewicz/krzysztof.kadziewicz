import snakemd
from secrets import token_urlsafe # https://docs.python.org/3/library/secrets.html

plik = f"pliki/{token_urlsafe(8)}"
nowy_dokument = snakemd.new_doc(plik)

tekst = """
Litwo, ojczyzno moja,
tu jestes jak zdrowie,...
itd...
"""

nowy_dokument.add_header("Hej - nowy dokument")
nowy_dokument.add_horizontal_rule()
nowy_dokument.add_paragraph(tekst)
nowy_dokument.add_code("from snakemd import *", lang="python")
nowy_dokument.output_page()
