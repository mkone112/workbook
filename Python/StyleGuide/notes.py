отступы нужно сохранять чтобы при переходах сразу оказываться где нужно
# это объсняет требование двух переносов после классов & fx
#конфликтует с dj    

    def f():
    ∙∙∙∙#code
    ∙∙∙∙
    
    def g():
    ∙∙∙∙pass
    ∙∙∙∙

МНОГОСТРОЧНЫЕ ЛИТЕРАЛЫ СТАРАТЬСЯ БИТЬ ПО \n


СТАРАТЬСЯ НЕ СОВМЕЩАТЬ ' И " В ОДНОЙ СТРОКЕ ЧТОБЫ НЕ ИСПОЛЬЗОВАТЬ """/'''
    message = (f'''Read "{post.title}" at {post_url}\n\n{cd['name']}'s '''
               f'''comments:{cd['comments']}''')
    message = (f'Read "{post.title}" at {post_url}\n\n'
               f"{cd['name']}'s comments:{cd['comments']}")


ПРОБЕЛЫ В ВЕРХНЕЙ СТРОКЕ
    subject = (f"{cd['name']} ({cd['email']}) recommends you reading "
               f"{post.title}")
    
    вместо
    
    subject = (f"{cd['name']} ({cd['email']}) recommends you reading"
               f" {post.title}")


КОД В КОММЕНТАРИЯХ В `
#хорошо выглядит и стиль принят в django by def
    # `related_name` allows access to article comments (`post.comments.all()`)
    # , in addition to accessing the article from a comment (`comment.post`).



ПОСЛЕ DOCSTRINGS КЛАССОВ ВСЕГДА ПЕРЕНОС

точки в конце комментов позволяют убедиться что мысль дописана

однострочные комменты до кода, так код уже, и легко модифицировать


MRO
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
СОРТИРУЙ FX/МЕТОДЫ/КЛАССЫ/INLINE IMPORTS ПО ИСПОЛЬЗОВАНИЮ -> ПО ГРУППАМ -> АЛФАВИТУ И регистроЗАВИСИМО


ПАРАМЕТРЫ В ЗАГОЛОВКАХ МЕТОДОВ СОРТИРУЮТСЯ ПО СМЫСЛУ -> АЛФАВИТУ И регистроЗАВИСИМО


MULTILINE TODOES
    # TODO(mk-dv): Check what happens if, for example, the 'request' is sent using 
    #               the POST method.
    #              Other task.


используй стиль typing в docstring
    attr(list[str]): ...


ВЫДЕЛЯТЬ КОРТЕЖИ СКОБКАМИ
#несмотря на необязательность, явно дают понять что это один кортеж, а не несколько элтов