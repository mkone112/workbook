# указать пользователя
~/.gitconfig
    [user]
        email = kalitamaxwork@gmail.com
        name = Maxim Kalita


# алиас для вывода графа лога
    [alias]
    lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
    lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
    lg = !"git lg1"


# вывод простого графа лога
    git log --all --decorate --oneline --graph


# влить все за один коммит
    #переключиться на целевую ветку и:
    git merge --no-ff <branch_for_merge>

# откат
    # стирает данные(нужно ввести ревизию последнего(?) коммита)
    git reset --hard HEAD~1

    # у меня что-то не сработало
    git reset --hard HEAD^



refactor(audio-controls) use common library for all controls


# crlf

    git config --global core.autocrlf false
    git config --global core.eol lf


# создать новую пустую ветку
$ git checkout --orphan <branc_name>


    feature — используется при добавлении новой функциональности уровня приложения
    fix — если исправили какую-то серьезную багу
    docs — всё, что касается документации
    style — исправляем опечатки, исправляем форматирование
    refactor — рефакторинг кода приложения
    test — всё, что связано с тестированием
    chore — обычное обслуживание кода


