def test_page_content():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Hola Mundo" in content, "El contenido de la página no incluye 'Hola Mundo'"