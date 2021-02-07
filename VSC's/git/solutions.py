Сменить автора коммитов
    git filter-branch -f --env-filter "GIT_AUTHOR_NAME='Maxim Kalita'; GIT_AUTHOR_EMAIL='kalitamaxwork@gmail.com'; GIT_COMMITTER_NAME='Maxim Kalita'; GIT_COMMITTER_EMAIL='kalitamaxwork@gmail.com';" HEAD
    git push -f origin HEAD


поиск в истории коммитов
    git grep "<regexp>" $(git rev-list --all)


глобально --no-ff(по идее работает и для pycharm)
    git config --global --add merge.ff false