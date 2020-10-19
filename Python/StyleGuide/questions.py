return reverse('blog:post_detail', args=[self.publish.year,
                                         self.publish.month,
                                         self.publish.day, self.slug])
or

return reverse('blog:post_detail',
               args=[self.publish.year, self.publish.month,
                     self.publish.day, self.slug])

#склоняюсь ко второму варианту тк он вроде позволяет проще добавлять новые args


TODO(<author>): Заглавная?