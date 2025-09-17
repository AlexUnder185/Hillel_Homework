import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видаляємо теги
    cleaned = re.sub(r'<[^>]*>', '', html)

    # Прибираємо порожні рядки
    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]

    final_text = '\n'.join(lines)

    # Записуємо результат
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)


# Виклик функції
delete_html_tags("draft.html")
