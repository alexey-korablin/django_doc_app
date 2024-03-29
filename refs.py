def reference():
    """
    ПРОВЕРКА ВЕРСИИ django
    $ python -m django --version

    СОЗДАНИЕ ПРОЕКТА
    $ django-admin startproject <project_name>

    СТРУКТУРА
    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py
    Каталог верхнего уровня - mysite - просто каталог, имя которого может быть изменено
    Файл manage.py - утилита командной строки для взаимодействия с django
    Внутренний каталог mysite/ - python-пакет для проекта. Это имя используется для импорта чего-либо из него.
        Например: mysite.urls
    mysite/__init__.py - пустой файл, говорящий python, что данный каталог является пакетом
    mysite/settings.py - файл для различных настроек проекта
    mysite/urls.py - содержит все пути используемые в проекте
    mysite/wsgi.py - точка входа для WSGI-совместимых вэб-серверов для обслуживания проекта

    ЗАПУСК СЕРВЕРА
    $ python manage.py runserver    --> команда запускает dev-сервер.
    Для смены порта выполняется команда     --> $ python manage.py runserver 8080
    Если же требуется сменить IP адрес сервера, нужно выполнить команду вот так:
        $ python manage.py runserver 0.0.0.0:8080
    Сервер перезапускает страницу автоматически почти во всех случаях изменения файлов, но при добавлении или удалении
        файлов перезапуск надо осуществлять вручную

    СОЗДАНИЕ ПРИЛОЖЕНИЯ
    Отличия приложения от проекта: приложение выполняет какое-то действие, например, предоставляет сервис. В то время
        как проект является набором различных настроек и приложений. В то же время приложение может быть частью
        нескольких проектов
    При создании приложения нужно находиться в одной директории с файлом manage.py
    Создание приложения выполняется командой: $ python manage.py startapp polls # polls - имя приложения
        Далее будет создана директория polls со следующими файлами и папками:
        polls/
            migrations/
                __init__.py
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py

    СОЗДАНИЕ VIEW
    Все представления создаются в файле views.py
    Для отображения какого-либо представления оно должно быть сопоставлено с каким-либо URL адресом. Делается это с
        помощью URLconf
    Чтобы создать URLconf в папке с приложением нужно создать файл urls.py
    Для того чтобы указать корень URLconf в файле urls.py (находится в корне проекта) нужно импортировать include и path
        из django.urls и добавить include() в список urlpatterns (см. файлы docsApp/urls.py и docsApp/polls/urls.py
        текущего проекта)
    Функция include() ищет сопоставления адресов, если находит, то отсекает сопоставленное и передает в URLconf
        оставшуюся строку для дальнейшей обработки. Смысл include() в легком подключении адресов
    Так как приложения имеют свои собственные настройки URL, в частности URLconf (polls/urls.py), они могут помещены за
        “/polls/”, или за “/fun_polls/”, или за “/content/polls/” и приложение все равно будет работать
    Функцию include() следует использовать при каждом добавлении адресов, исключение только admin.site.urls
    Функция path() принимает 4 аргумента: 2 обязательных и 2 опциональных. Обязательные: маршрут и представление.
        Опциональные: ключевые слова и имя.
    Аргумент path() route - является строкой, содержащей шаблон адреса. При запросе django обращается к массиву
        urlpatterns и сравнивает запрошенный адрес с шаблонами пока не найдет подходящий. Пример:
            имеется шаблон myapp/
            при запросах к адресам https://www.example.com/myapp/ и https://www.example.com/myapp/?page=3 результат
            будет одинаковым - myapp/
    Аргумент path() view - когда шаблон сопоставляется удачно, происходит вызов определенного представления с объектом
        HttpRequest в качестве первого аргумента и с прочими "захваченными" значениями в качестве второго аргумента
    Аргумент path() kwargs - ключевые слова могут быть переданы в качестве словаря к требуемому представлению
    Аргумент path() name - позволяет передать имя в качестве псевдонима для адреса. После чего к данному адресу можно
        будет не двусмысленно обратиться из любого места приложения.

    НАСТРОЙКА БАЗЫ ДАННЫХ
    Все настройки хранятся в файле settings.py
    Информация об используемой БД и пути к ее файлу находятся в константе DATABASES
    По умолчанию используется БД SQLite (не требует имени пользователя, пароля и хоста)
    Константа INSTALLED_APPS содержит все установленные приложения, которые должны быть доступны в django. По умолчанию
        установлены следующие приложения:
        * django.contrib.admin - управление сайтом
        * django.contrib.auth - система аутентификации
        * django.contrib.contenttypes - фреймворк для типов содержимого
        * django.contrib.sessions - фреймворк для работы с сессиями
        * django.contrib.messages - фреймворк для работы с сообщениями
        * django.contrib.staticfiles - фреймворк для работы со статическими файлами
    Чтобы приложение могло работать с базой данных нужно создать соответствующие записи. Делается это следующей
        командой: $ python manage.py migrate
        Команда migrate смотрит список INSTALLED_APPS и создает любые необходимые таблицы в БД в соответствии с
        настройками в файле mysite/settings.py

    СОЗДАНИЕ МОДЕЛИ
    Для создания таблицы в БД нужно создать модель. Модель создается в файле models.py, который находится в приложении.
        Модель представляет из себя python класс
    Каждая модель представляет из себя подкласс от django.db.models.Model
    Каждая модель содержит переменные, каждая из которых представляет запись из табицы БД в модели
    Каждое поле представлено экземпляром класса Field, например CharField (для текстового поля) или DateTimeField (для
        даты и времени). Благодаря этому django будет хранить типы данных для каждого поля
    Имя каждого экземпляра класса Fields является именем поля в БД
    Некоторые экземпляры класса Field  имеют обязательные аргументы, например CharField требует аргумент max_length. Это
        используется не только в схеме БД, но и при валидации
    Также могут быть определены и взаимоотношения, например через models.ForeignKey
    django поддерживает взаимоотношения: многие-к-одному, многие-ко-многим и один-к-одному

    АКТИВАЦИЯ МОДЕЛИ
    Для активации модели нужно сообщить проекту об установленном приложении.
    Для того чтобы включить приложение в проект нужно в INSTALLED_APPS указать на класс конфигурации этого приложения.
        Данный класс хранится в файле apps.py приложения. Так для приложения polls и его класса настроек PollsConfig
        путь будет выглядеть как polls.apps.PollsConfig. Подобную строку нужно добавить в файл settings.py проекта (в
        массив INSTALLED_APPS)
    Для выполнения миграции конкретного приложения (polls) в базу нужно сделать следующее:
        $ py manage.py makemigrations polls
    Команда makemigrations говорит о том, что были сделаны изменения в модели и их нужно сохранить как миграцию
    Миграции хранятся в папке migrations приложения. Данные миграции являются записями в БД и могут быть изменены
        вручную
    Схемой БД можно управлять и в автоматическом режиме, для этого существует команда migrate
    Посмотреть миграцию можно так: $ py manage.py sqlmigrate polls 0001
    Проверка приложения на наличие проблем: $ py manage.py check
    Добавление изменений в моделях: $ py manage.py migrate
    Flow:
        * сделать изменения в модели models.py
        * создать миграции для этих изменений $ py manage.py makemigrations
        * применить изменения в БД $ py manage.py migrate

    ВЗАИМОДЕЙСТВИЕ С API
    Чтобы запустить командную оболочку для взаимодействия с Django, нужно выполнить команду:
        $ python manage.py shell
    Для взаимодействия с объектами модели их нужно импортировать из polls/models.py:
        from polls.models import Question, Choice
    Для просмотра содержимого модели Question: Question.objects.all()   # --> <QuerySet []>
    Для создания нового запроса: q = Question(question_text="What's new?", pub_date=timezone.now()) # прежде
        импортировать timezone: from django.utils import timezone
    Сохранить запрос в БД: q.save() # после этого можно посмотреть доступные свойства объекта. Для объекта Question это
        id, question_text и pub_date
    Сохраненные значения могут быть изменены: q.question_text="what's up?"  # после снова необходимо выполнить q.save()
    Можно фильтровать записи, например по id: Question.objects.filter(id=2); или по текстовым вхождениям:
        Question.objects.filter(question_text__startswith="What") # --> <QuerySet [<Question: What's up?>]>
    Если предполагается получить только одну запись, то можно использовать метод get, если же записей больше, то нужно
        использовать метод filter
    Записи можно получить по id или по primary key (pk), например: Question.objects.get(pk=1)
    Просмотр записей из смежного (related) объекта: q.choice_set.all() # --> <QuerySet []>
    Создание записей в смежном объекте: q.choice_set.create(choice_text='Not much', votes=0) # --> <Choice: Not much>
    Смежные объекты имеют доступ друг к другу. Если q = Question.objects.get(pk=1), то получить все записи смежного
        объекта Choice можно так: q.choice_set.all(), а количество записей так: q.choice_set.count()
    Чтобы получить доступ к свойствам смежного объекта нужно использовать "__":
        Choice.objects.filter(question__pub_date__year=current_year)    # получит все записи объекта Question c датой
        побликации, соответствующей current_year (current_year = timezone.now().year  == 2019)
    Чтобы удалить запись (можно и через смежный объект) нужно ее сначала получить:
        c = q.choice_set.filter(choice_text__startswith='Just') , а затем удалить: c.delete()   # -->
        (2, {'polls.Choice': 2}) - было удалено две записи

    АДМИНКА DJANGO
    Создание пользователя администратора $ python manage.py createsuperuser После ввода имени пользователя, пароля и
        подтверждения данных пользователь будет создан.
    Запуск development сервера: python manage.py runserver
    Для перехода в админку нужно перейти по адресу: http://127.0.0.1:8000/admin/
    В админке в разделе авторизации и аутентификации будут находиться 2 группы: Группы и Пользователи - эти группы
        предоставляются фреймворком django.contrib.auth
    Чтобы добавить приложение в админ. панель нужно зарегистрировать необходимые объекты в интерфейсе администратора.
        Для этого в файле admin.py каталога приложения нужно выполнить импорт модуля admin из django.contrib. Затем все
        необходимые объекты из модуля models приложения. После чего зарегистрировать эти объекты:
        from django.contrib import admin
        from .models import Question
        admin.site.register(Question)

    ОБЗОР VIEW
    View является типом веб-страницы, управляется сервером, имеет свою логику и шаблон представления. Например:
        страница индекса вопросов - может отображать несколько последних вопросов
        страница с деталями вопроса - может отображать текст вопроса, без ответа, но с формой для вопроса
    Веб-страницыи прочий контент приходит из view. Каждое представление предоставляется простой функцией или методом
        (если view базируется на классе)
    Для получения нужного представления по url используется URLconfs, он сопоставляет шаблоны адресов и представления
    !? Чтобы получить больше информации см. URL dispatcher --

    СОЗДАНИЕ VIEW
    Новые view следует добавлять в polls/views.py
    После создания view, его нужно связать с url в polls.urls путем добавления вызовов path. Это может выглядеть так:
        urlpatterns = [
            ...
            path('<int:question_id>/', views.detail, name='detail'),
            path('<int:question_id>/results/', views.results, name='results'),
            path('<int:question_id>/vote/>', views.vote, name='vote')
        ]
        Теперь при переходе по адресу /polls/34/ будет вызвана функция detail, то же произойдет и при переходе на адреса
        /polls/34/results/ и /polls/34/vote/ т.е. будут вызваны методы results и vote соответственно.
    Разрешение адресов в представления происходит так:
        на сервер приходит запрос на получение страницы - /polls/34/ --> загружается модуль mysite.urls (в данном
        случае это docsApp.urls) потому что на него указывает ROOT_URLCONF (в settings.py) --> urls.py (проекта) обходит
         и сопоставляет все доступные ему шаблоны адресов --> находит 'polls/', обрезает его, получает 'polls/' и
         отправляет оставшийся текст - '34/' в polls.urls --> текст '34/' сопоставляется с шаблоном '<int:question_id>/'
         --> вызывается метод detail() -->  question_id=34 приходит от <int:question_id>; тут угловые скобки захватывают
         часть url и отправляют ее как ключевой аргумент в функцию. Тут часть :question_id> определяет имя котрое
         будет использовано для идентификации подходящего шаблона, а <int: - это конвертер, который определяет, какие
         шаблоны должны соответствовать этой части URL

    НАПИСАНИЕ ПОЛЕЗНОГО VIEW
    Каждое view делает ОДНУ из ДВУХ (обязательных) вещей: возвращает объект HttpResponse, содержащий запрошенную
        страницу или возбуждает исключение Http404
    View может:
        * читать записи из БД
        * использовать систему шаблонов django или сторонние Python системы шаблонов
        * генерировать PDF файлы
        * выводить XML
        * создавать ZIP-файлы
        * делать все что позволяет Python и его экосистема
    View может просто отдать данные (возможное содержимое метода index):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]   # получает 5 объектов question из БД,
        # сортирует их по дате публикации
        output = '\n'.join([q.question_text for q in latest_question_list]) # генерирует список строк 'question_text'
            # из полученных ранее объектов question и объединяет их в строку.
        return HttpResponse(output) # возвращает полученную строку
    Для создания разметки нужно создать папку polls/templates - тут django ищет шаблоны. Настройка TEMPLATES (файл
        settings.py) описывает то, как Django загрузит и отрисует шаблоны. По умолчанию настройки  DjangoTemplates
        таковы, что свойство APP_DIRS - True - это значит что шаблоны будут искаться в папке templates каждого из
        установленных приложений. Если файл с шаблоном расположен по адресу polls/templates/polls/index.html, то
        обратиться к нему можно через polls/index.html
    Файлы с шаблонами лучше никогда не класть непосредственно в папку templates во избежание коллизий имен.
    При использовании html-шаблона необходимо создать сам шаблон (polls/templates/polls/index.html), в файле
        polls/views.py импортировать loader из django.template . Далее код метода index может быть таким:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]   # описывалось ранее
        template = loader.get_template('polls/index.html')  #
        context = {'latest_question_list': latest_question_list}
        return HttpResponse(template.render(context, request))
        Код выше загружает шаблон и  передает контекст (словарь) в метод render объекта template

    СОКРАЩЕНИЯ
    Также возможно использовать сокращение для ответа с отрисованной страницей. Для этого нужно импортировать метод
        render из django.shortcuts: from django.shortcuts import render. Функция render первым аргументом принимает
        объект запроса, вторым аргументом - имя шаблона и третьим, опциональным параметром словарь который является
        контекстом для шаблона. Далее, отрисованная страница попадает в объект HttpResponse
    Если искомая страница не найдена, то нужно возбудить исключение 404. Делается это с помощью метода Http404. Пример
        кода:
        from django.http import Http404 # импорт модуля Http404
        ...
        def detail(request, question_id):   #
            try:
                question = Question.objects.get(pk=question_id) # попытка получить объект из БД по основному ключу
            except Question.DoesNotExist:   # в случае неудачи и ошибки DoesNotExist
                raise Http404('Question does not exist')    # возбуждаем исключение, которое вернет ошибку http 404
            return render(request, 'polls/detail.html', {'question': question}) # в случае успеха отправляем
            # отрисованную страницу
    Сокращенный вариант попытки получения страницы или возбуждения исключения осуществляется через метод
        get_object_or_404. Эта функция принимает django модель в качестве первого аргумента, далее идет произвольное
        число параметров (те же самые, которые могут быть переданы методу модели get):
        from django.shortcuts import get_object_or_404, render
        ...
        question = get_object_or_404(Question, pk=question_id)
        ...
    В случае необходимости получения списка объектов вместо одного объекта можно использовать метод get_list_or_404()
        внутри он использует ни get(), а filter()

    КАК НЕ ИСПОЛЬЗОВАТЬ ХАРДКОД В URL-АДРЕСАХ
    Чтобы убрать хардкод из путей url'ов в шаблонах нужно воспользоваться тегом url. Благодаря этому тегу django
        посмотрит в polls.urls и найдет там путь с соответствующим именем:
        <a href="{% url 'detail' question.id %}">...</a>
        Теперь для изменения путей нужно лишь внести изменения в первый аргумент метода path:
        path('specifics/<int:question_id>/', views.detail, name='detail')   # Тут "specifics" - пример измененного пути.
        # That's it :)

    ПРОСТРАНСТВО ИМЕН URL
    Чтобы django мог понять какой адрес нужно использовать при одинаковых менах в путях нужно добавить пространство имен
        в URLconf в polls/urls.py так: app_name = 'polls', а в шаблоне, внутри атрибута href сделать такие изменения:
        {% url 'polls:detail' question.id %}

    НАПИСАНИЕ ПРОСТОЙ ФОРМЫ
    Пример кода:
        <form action="{% url 'polls:vote' question.id %}" method="post">
            {% csrf_token %}
            {% for choice in question.choice_set.all%}
            <input type="radio" name="choice" id="choice{{forloop.counter}}" value="{{choice.id}}">
            <label for="choice{{forloop.counter}}">{{choice.choice_text}}</label><br>
            {% endfor %}
            <input type="submit" value="Vote">
        </form>
        Так как форма содержит в себе инпуты с типом radio, то на сервер будет отправлен выбранный choice id.
        action содержит сгенерированный адрес, состоящий из пути с именем vote, ищется в пространстве адресов polls (
        polls/urls.py  urlpatterns = [... path('<int:question_id>/vote/', views.vote, name='vote')])
        method - post. Данный метод следует выбирать всегда в случае изменения  данных на сервере.
        forloop.counter - содержит счетчик цикла for
        csrf_token - данный токен тегирует каждый шаблон который отправляет запросы зменяющие данные на сервере. Данный
        токен является встроенной защитой от межсайтового скриптинга (CSRF).
    Пример кода функции vote:
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice."
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
        request.POST - объект подобный словарю, позволяющий получить доступ к отправленным данным (содержимое запроса)
        по ключу (в данном случае 'choice'). request.POST['choice'] возвращает id выбранного choice как строку (всегда
        как строку). Подобным образом данные могут быть извлечены и из GET запроса.
        В отличии от HttpResponse, HttpResponseRedirect принимает только один аргумент - адрес, куда пользователь будет
        перенаправлен. HttpResponseRedirect должен быть использован после каждого успешного POST-запроса.
        Функция reverse помогает избежать хардкода в функции во view. В функцию передается имя view, которому нужно
        передать управление и часть шаблона адреса, указывающего на эту view (docsApp/urls.py --> urlpatterns = [
        ..., path('polls/', include('polls.urls'))]). Шаблон адреса в результате будет выглядеть так:
        '/polls/3/results/' , где 3 - это question_id. Далее будет вызвана view results и показан финальный результат.
    !При одновременно голосовании вычисления количество голосов и запись их в БД будут не верны. Проблема в Race
    Condition. Она может быть решена с помощью функции F()

    ИСПРАВЛЕНИЕ URLconf И VIEWS
    В файле polls/urls.py сделать изменения:
        urlpatterns = [
            path('', views.IndexView.as_view(), name='index'),
            path('<int:pk>/', views.DetailView.as_view(), name='detail'),
            path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
            ...
        ]
    В файле polls/views.py сделать изменения:
        ...
        from django.views import generic
        ...
        class IndexView(generic.ListView):
            template_name = 'polls/index.html'
            def get_queryset(self):
                return Question.objects.order_by('-pub_date')[:5]
        class DetailView(generic.DetailView):
            model = Question
            template_name = 'polls/detail.html'
        class ResultsView(generic.DetailView):
            model = Question
            template_name = 'polls/result.html'
        Выше использовано 2 джинерик вью(ДВ): ListView и DetailView. Они представляют собой концепцию отображения списка
        объектов и отображение деталей определенного типа объекта. Каждый ДВ должен знать с какой моделью ему
        взаимодействовать, за это отвечает атрибут model: model = Question. DetailView ожидает получить primary key
        (pk), которое он получает из url
        По умолчанию DetailView использует шаблон <app name>/<model name>_detail.html в данном случае -
        polls/question_detail.html . Атрибут template_name позволяет указать нужный шаблон.
        Подобным образом работает и ListView. Адрес шаблона по умолчанию: <app name>/<model name>_list.html, атрибут
        template_name используется для тех же целей.

    """

    pass
