<str>
    .join()
    # exe за линейное время независимо от реализации Python
    
dict:https://www.youtube.com/watch?v=37S53yFg9wc&index=7&t=0s&list=PLmcXv3fDgVcjpZ6QnpXrSNTj7-RxtdFhA
# locals() больше не dict?
2.7 перемешивает val в dict, но всегда одинаково
3.5 randomized -> 3.6 ordered
хеши помещаются в таблицу чтобы их не вычислять повторно
def fast_match(key, target):
    if key is target: return True
    if key.hash != target_key.hash:return False
    return key == target

питон втыкает в таблицу по val хеша, втыкаем B но если там уже есть запись A - ищет пустую подходящую, но если запись A будет удалена, B будет искаться в на месте А -> решение, при удалении оставлять запись dummy являющуюся указателем что нужно проверить другие места
словари имеют номер версии, для исбегания повторных поисков методов