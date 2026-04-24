import re

def test_sql_checks():
    with open('Profiles.sql', 'r') as f:
        content = f.read().upper()

    # Test 1: Verificar que la tabla se llame 'PROFILES'
    assert "CREATE TABLE PROFILES" in content, "Test 1 Falló: La tabla debe llamarse Profiles"

    # Test 2: Verificar que exista el campo 'BIRTH_DATE' para la edad (Requisito HU)
    assert "BIRTH_DATE DATE" in content, "Test 2 Falló: Falta el campo birth_date de tipo DATE"

    # Test 3: Verificar que el campo 'BIO' o descripción general exista
    assert "BIO TEXT" in content, "Test 3 Falló: Falta el campo bio para la presentación"

    # Test 4: Verificar que el radio de búsqueda sea numérico (INTEGER)
    assert "SEARCH_RADIUS INTEGER" in content, "Test 4 Falló: El radio de búsqueda debe ser INTEGER"

    # Test 5: Verificar que exista la Clave Primaria (PK)
    assert "PRIMARY KEY" in content, "Test 5 Falló: La tabla debe tener una PRIMARY KEY definida"

if __name__ == "__main__":
    try:
        test_sql_checks()
        print("✅ Todos los tests pasaron exitosamente (5/5)")
    except AssertionError as e:
        print(f"❌ Error en el test: {e}")
        exit(1)
        