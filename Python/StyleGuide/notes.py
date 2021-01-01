отступы нужно сохранять чтобы при переходах сразу оказываться где нужно
# это объсняет требование двух переносов после классов & fx
    
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


КОД В КОММЕНТАРИЯХ В ''
    # 'related_name' allows access to article comments ('post.comments.all()')
    # , in addition to accessing the article from a comment ('comment.post').


ПОСЛЕ DOCSTRINGS КЛАССОВ ВСЕГДА ПЕРЕНОС

точки в конце комментов позволяют убедиться что мысль дописана

однострочные комменты до кода, так код уже, и легко модифицировать


MRO
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):