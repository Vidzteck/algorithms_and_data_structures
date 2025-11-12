def greedy_vertex_cover(edges):
    """
    Жадный 2-аппроксимационный алгоритм для задачи о вершинном покрытии
    Args:
        edges: список кортежей (u, v) представляющих ребра графа
    Returns:
        множество вершин, образующих покрытие
    """
    cover = set()
    remaining_edges = set(edges) # Создаем копию множества ребер

    while remaining_edges: # Пока есть непокрытые ребра
        # Выбрать произвольное ребро
        u, v = remaining_edges.pop()

        # Добавить обе вершины в покрытие
        cover.add(u)
        cover.add(v)

        # Удалить все ребра, инцидентные u или v
        # Создаем новое множество, исключая инцидентные ребра
        remaining_edges = {(a, b) for a, b in remaining_edges if a != u and a != v and b != u and b != v}

    return cover

def analyze_vertex_cover(edges):
    """
    Анализ качества аппроксимации и проверка корректности решения.
    """
    cover = greedy_vertex_cover(edges)
    print(f"Размер покрытия: {len(cover)}")
    print(f"Покрытие: {sorted(list(cover))}")

    # Проверка корректности: каждое ребро должно быть покрыто
    all_covered = True
    for u, v in edges:
        if u not in cover and v not in cover:
            print(f"Ошибка: Ребро ({u}, {v}) не покрыто!")
            all_covered = False
    if all_covered:
        print("Все ребра покрыты ✓")

    # Вывод коэффициента аппроксимации
    # Для этого цикла из 10 вершин оптимальное покрытие = 5 вершин (например, {0, 2, 4, 6, 8})
    optimal_size = 5 # Известно для этого конкретного графа (цикла C_10)
    approx_ratio = len(cover) / optimal_size
    print(f"Размер оптимального покрытия (известный): {optimal_size}")
    print(f"Коэффициент аппроксимации (A(I) / OPT(I)): {approx_ratio:.2f}")
    print(f"Коэффициент гарантированной 2-аппроксимации: <= 2")
    if approx_ratio <= 2:
        print("Коэффициент аппроксимации соответствует гарантии (≤ 2). ✓")
    else:
        print("Коэффициент аппроксимации ПРЕВЫШАЕТ гарантию (2)!")


edges = []
for i in range(10):
    a, b = map(int, input().split())
    edges.append((a,b))
analyze_vertex_cover(edges)
