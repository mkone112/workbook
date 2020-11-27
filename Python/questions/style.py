not a in b ?| a not in b

return reverse('blog:post_detail', args=[self.publish.year,
                                         self.publish.month,
                                         self.publish.day, self.slug])
or

return reverse('blog:post_detail',
               args=[self.publish.year, self.publish.month,
                     self.publish.day, self.slug])

#склоняюсь ко второму варианту тк он вроде позволяет проще добавлять новые args



TODO(<author>): Заглавная?
-> Да



существуют ли какие либо ограничения на сортировку fx и классов в коде Python/django?
#скажем по алфавиту



где использовать висящую запятую?
    return render(request, 'blog/post/share.html',
                      {'post': post, 'form': form, 'sent': sent,
                       'sent_failed': sent_failed,(?)})



Использовать ли переносы строк в коллекциях?
    return render(request, 'blog/post/share.html',
                      {'post': post, 'form': form, 'sent': sent,
                       'sent_failed': sent_failed,(?)})
    ->
    return render(request, 'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent,
                   'sent_failed': sent_failed,
                   })
    ПЕРЕНОСТИТЬ ЛИ СКОБКИ?
        return render(request, 'blog/post/share.html',
                      {'post': post,
                       'form': form,
                       'sent': sent,
                       'sent_failed': sent_failed,
                       })
        return render(request, 'blog/post/share.html',
                      {'post': post, 'form': form, 'sent': sent,
                       'sent_failed': sent_failed})
        ->
                return render(
                            request, 'blog/post/share.html',
                            {'post': post,
                             'form': form,
                             'sent': sent,
                             'sent_failed': sent_failed,
                            }
                             )
                return render(
                            request, 'blog/post/share.html',
                            {'post': post, 'form': form, 'sent': sent,
                            'sent_failed': sent_failed}
                             )
                return render(
                           request,
                           'account/register_done.html',
                           {'new_user': new_user}
                       )


так-ли хороша вясящая запятая?
# вроде запрещены в литералах
# Это делает различия в контроле версий чище и изменение кода может быть менее хлопотным.

Нужны ли f' у не форматных строк?
            print(
                "PASSWORD:\n"
                 "\tuser_form.cleaned_data['password']="
                f"{user_form.cleaned_data['password']}\n"
                f"\tnew_user.password={new_user.password}"
            )                   


ГДЕ ОПРЕДЕЛЯТЬ КАСТОМНЫЕ МЕТОДЫ МОДЕЛЕЙ?
# кастомные методы вроде clean_ должны быть вроде после Meta, но где?
    db fields
    custom managers
    Meta
    <?тут>
    __str__
    <?тут>
    save()
    <?тут>
    get_absolute_url
    <?тут>
            