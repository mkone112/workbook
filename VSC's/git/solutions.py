Сменить автора коммитов
    git filter-branch -f --env-filter "GIT_AUTHOR_NAME='Maxim Kalita'; GIT_AUTHOR_EMAIL='kalitamaxwork@gmail.com'; GIT_COMMITTER_NAME='Maxim Kalita'; GIT_COMMITTER_EMAIL='kalitamaxwork@gmail.com';" HEAD
    git push -f origin HEAD


поиск в истории коммитов
    git grep "<regexp>" $(git rev-list --all)


глобально --no-ff(по идее работает и для pycharm)
    git config --global --add merge.ff false

git stash push -a -u -m <msg>

.bashrc
# добавить в конец файла
    # stop git merge from opening text editor
    export GIT_MERGE_AUTOEDIT=no