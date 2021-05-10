.generics
#дженерик?
    GenericAPIView
    #расширяет возможности APIView, добавляя часто используемые методы list и detail
    #обеспечивает базовую fx
    
    ListCreateAPIView
    #List + Create(post & get)
    
    RetrieveAPIView
    #
    
    get_object_or_404
    #
    
    RetrieveUpdateDestroyAPIView
    # наследует
        RetrieveModelMixin
        UpdateModelMixin
        DestroyModelMixin
        GenericAPIView


.serializers
# <serializer>(..., many=True) - позволяет сериализовывать querysets
    
    HyperlinkedModelSerializer
    # hyperlinking is good RESTful design
    
    ModelSerializer
    #shortcut для создания Serializer на основе модели
        автоматом определяет набор полей
        включает простую реализацию create() & update()

.viewsets
    ModelViewSet
    #предоставляет набор стандартных rw операций
    
.decorators
    action(methods=('GET',), url_path=)
    #создает кастомное действие с именем декорируемой fx(url = имени fx)
        #можно его изменить с помощью url_path kwarg
    #используется для создания конечных точек(url?) !~ crud
    #by def отвечает только на GET

.permissions
    .IsAuthenticatedOrReadOnly
    #позволяет убедиться что auth requests получат rw доступ, а unauthenicated requests ro
.urlpatterns
    .format_suffix_patterns
    #добавляет urls для более удобного указания формата данных запроса
ListModelMixin
#реализует action .list()


Mixin
#реализует action используемый для обеспечения базового поведения представления

ViewSets
#продвинутый класс, позволяет удостовериться что URL-соглашения консистенты во всем api
#минимизирует V кода, позволяя сконцентрироваться на представлении API а URLS
#менее явно

serializers
#позволяют преобрарзовать сложные данные(напр. querysets, models) в типы данных python, которые затем можно преобразовать в json, xml, etc content types
#чертовски похожи на forms
    .HyperlinkedModelSerializer
    #используется вместо ModelSerializer для создания гиперссылок между сущностями
        не имеет поля `id` by def
        включает `url = HyperlinkedIndentityField`
        отношения используют `HyperlinkedRelatedField` вместо `PrimaryKeyRelatedField`

можно создавать несколько классов на разные методы и добавлять их urls


создадим api для
        чтения
        редактирования
        удаления
    статей в блоге
проект имитирующий блог с серверным api


api view
#простой класс

Request
# расширяет HttpRequest, предоставляет более гибкий парсинг
    .data
    #похож на .POST, но полезнее для Web APIs
    #в отличие от .POST хранит произвольные данные, работает с POST, PUT, PATCH
    

Response
#позволяет не париться что отдавать
#производный SimpleTemplateResponse производный от HttpResponse, хранит unrendered контент и определяет корректный тип для >> клиенту
    return Response(data)  # Renders to content type as requested by the client
#тк api отдает контент в формате основываясь на запросе - при запросе из браузера >> html
.status
    .HTTP_400_BAD_REQUEST
    #явнее

ОБЕРТКИ
#проверяют
    #что request во view получен
    # и добавляет контекст к Response с указанием типа содержимого
    # предоставляет 405 Method Not Allowed responses при необходимости
    # отлавливает ЛЮБЫЕ ParseError expect при доступе к request.data в случае неверного ввода
        @api_view
        #декоратор fx для оборачивания views
        
        
        APIView
        #декоратор классов-views


указание format во views позволяет использовать urls вида example.com/item.json

рендеринг в html
    на основе пререндереного html
    
    на основе шаблонов

.renderers
    StaticHTMLRenderer
    #

Hyperlinking API
#работа с отношениями сущностей - сложнейший аспект дизайна API
#способы представления:
    используя pk
    hyperlinking между сущностями
    используя уникальный слаг для связанной сущности
    используя default string representation связанной сущности
    включение связанной сущности в представление родителя
    другие кастомные способы представления
    #drf поддерживает все варианты, может применять их к прямым или обратным отношениям, или применять их посредством пользовательских менеджеров - общих внешних ключей


ПАГИНАЦИЯ
#имеет мно-во стилей


drf ВКЛЮЧ абстракцию для работы с ViewSets, позволяющую создавать ulrs на основе общих соглашений
ViewSet ~ View, но предоставляют retrieve() & update() вместо get(), put().
привязывается к обработчикам методов при создании наборов представления(обычно с помощью Router)

Router
#обрабатывает сложности определения urls за разраба
#при использовании ViewSets позволяет регистрировать их как маршруты

методы обработчика привязываются к actions oi определен URLConf