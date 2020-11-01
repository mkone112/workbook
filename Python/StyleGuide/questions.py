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