АБСТРАКТНАЯ ФАБРИКА
#порождающий паттерн
#позволяет создавать семейства связанных obj, не привязываясь к конкретным классам создаваемых obj
] мы пишем симулятор мебельного магазина, код ⊃
	семейство зависимы продуктов
		кресло + диван + столик
	несколько вариация этого семейства
	#напр представленные в стилях
		Ар-деко
		Викторианский
		Модерн
требуется создавать obj продуктов : они сочетались(?) с другими продуктами семейства
#при этом требуется НЕ вносить изменения в ∃ код при добавлении новых продуктов|семейств в программу
АФ выделяет общие интерфейсы для отдельных продуктов составляющих семейства
#∀ кресла ⊃ интерфейс "Кресло", ∀ диваны ⊃ интерфейс "Диван" ...