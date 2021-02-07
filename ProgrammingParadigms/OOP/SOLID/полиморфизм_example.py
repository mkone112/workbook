"""
В наследство от тяжкого советского прошлого мы получили класс двойного назначения Radar, которым можно и еду разогреть, и врага найти. А вместо панели управления используется будильник, потому что план перевыполнен, а их надо куда-то девать. Но, к счастью, безымянный МНС из НИИ Химии, Удобрений и Ядов, на которого это спихнули, реализовал интерфейсы FoodWarmer для радара и FoodWarmerControlPanel для будильника.

Спустя поколение кому-то пришло в голову, что еду лучше греть микроволновкой, а управлять микроволновкой лучше кнопочками. И вот созданные классы Microwave и ButtonsPanel. И они реализуют те же интерфейсы. FoodWarmer и FoodWarmerControl. Что нам это даёт?

Если мы везде в своём коде использовали для разогрева еды переменную типа FoodWarmer, то мы можем просто заменить реализацию на более современную, и никто ничего не заметит. То есть, коду, использующему интерфейс нет никакого дела до деталей реализации. Или до того факта, что она поменялась целиком и полностью. Мы можем даже сделать класс FoodWarmerFactory, который выдаёт разные реализации FoodWarmer в зависимости от конфигурации вашего приложения.

"""
class InterfaceFoodWarmer:

    def get_access_to_control_panel(self) -> InterfaceFoodWarmerControlPanel:
        ...
        
    def open_door(self) -> None:
        ...
        
    def put(self, Food) -> None:
        ...
        
    def close_door(self) -> None:
        ...
    
        

class InterfaceFoodWarmerControlPanel:

    def press_on(self) -> None:
        ...
        
    def press_off(self) -> None:
        ...
        
    def press_increase_time(self) -> None:
        ...
        
    def press_decrease_time(self) -> None:
        ...
        
    def press_start(self) -> None:
        ...
        
    def press_stop(self) -> None:
        ...


class InterfaceEnemyFinder:
    def find_enemies(self) -> [*enemies]:
        ...


class ImplementationRadar(InterfaceFoodWarmer, InterfaceEnemyFinder):
    """Реализация интерфейса обязана реализовывать все его методы."""
    _secret_military_chips = [*chips]
    _giant_microwaves_generator = FoodWarmerController
    _strange_control_panel = ImplementationAlarmClock
    
    def get_access_to_control_panel(self) -> InterfaceFoodWarmerControlPanel:
        ...
    
    def open_door(self):
        ...
        
    def put(self, Food):
        ...
        
    def close_door(self):
        ...
        
    def find_enemies(self) -> [*enemies]:
        ...
        

class ImplementationAlarmClock(InterfaceFoodWarmerControlPanel):
    _mechanics = [*mechanic_parts]
    
    def press_on(self) -> None:
        ...
         
    def press_off(self)-> None:
        ...
         
    def press_increase_time(self)-> None:
        ...
         
    def press_decrease_time(self)-> None:
        ...
         
    def press_start(self)-> None:
        ...
         
    def public press_stop(self)-> None:
        ...
         

class ImplementationMicrowave(InterfaceFoodWarmer):
    _fancy_inner_chips = [*chips]
    _food_warming_thing = FoodWarmerController
    _buttons_panel = ImplementationButtonsPanel
    
    def get_access_to_control_panel(self) -> IntefaceFoodWarmerControlPanel:
        ...
        
    def open_door(self) -> None:
        ...
        
    def put(self, Food) -> None:
        ...
        
    def close_door(self) -> None:
        ...
        

class ImplementationButtonsPanel(InterfaceFoodWarmerControlPanel):
    _buttons = [*button_states]
    
    def press_on(self) -> None:
        ...
        
    def press_off(self) -> None:
        ...
        
    def press_increase_time(self) -> None:
        ...
        
    def press_decrease_time(self) -> None:
        ...
        
    def press_start(self) -> None:
        ...
        
    def press_stop(self) -> None:
        ...
        