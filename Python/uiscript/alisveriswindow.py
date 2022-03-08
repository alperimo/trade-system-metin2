import uiScriptLocale
import localeInfo

ROOT_PATH = "d:/ymir work/ui/game/guild/"
KUCUK = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
ORTA = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
BUYUK = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
SLOT = "d:/ymir work/ui/public/Slot_Base.sub"

window = {
	"name" : "AlisverisWindow",
	"style" : ("movable", "float",),

	"x" : 90,
	"y" : 100,

	"width" : 807+16,
	"height" : 471,

	"children" :
	(

		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 807+16,
			"height" : 471,

			"title" : "Riot2 - Alisveris",

			"children" :
			(
				#{ "name":"ayarlar", "type":"horizontalbar", "x":9, "y":64, "width":140+3, },
				{
					"name" : "AramaicinSlotbar",
					"type" : "slotbar",
					"x" : 28-10,
					"y" : 62-3,
					"width" : 94+30+20,
					"height" : 18,
					"children" :
					(
						{
							"name" : "itemara",
							"type" : "editline",
							
							"width" : 92,
							"height" : 48,
							
							"text"	: "item ara..",
							
							"input_limit" : 24,
							
							"x" : 2,
							"y" : 2,
						
						},
					),
				},
				{ "name":"arabutton", "type":"button", "x":172, "y":59, "text" : "Ara", "default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub", "over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub", "down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub", },
				{
					"name" : "ItemlerThin",
					"type" : "thinboard",
					
					"x" : 11,
					"y" : 111,
					
					"width" : 763+15+8+3+2,
					"height" : 351,
					
					"children" :
					(
						{
							"name" : "ItemList",
							#"type" : "listbox_scrollt",
							"type" : "listbox_scrollitem",
							
							"x" : 3,
							"y" : 3,
							
							#"width" : 760+15+5+8+25-6-10,
							"width" : 760+15+5+8+25-6-10+5 + 16,
							"height" : 348,
							
						},
					),
				},
				{
					"name" : "itemadilevelsahibivsvsresim",
					"type" : "titlebaralisveris",
					
					"x": 10,
					"y": 85,
					
					"width": 763+15+8+3+2,
					
					"children" :
					(
						{
							"name" : "resim",
							"type" : "text",
							
							"x" : 5+20+15,
							"y" : 3,
							
							"text" : "Resim",
							
						},
						{
							"name" : "adi",
							"type" : "text",
							
							"x" : 5+80+30+80+30,
							"y" : 3,
							
							"text" : localeInfo.ITEMADI,
							
						},
						{
							"name" : "fiyat",
							"type" : "text",
							
							"x" : 5+80+80+80+80+30+80+30-6,
							"y" : 3,
							
							"text" : "Fiyat",
							
						},
						{
							"name" : "satan",
							"type" : "text",
							
							"x" : 5+80+80+80+80+80+30+80+30+30+7+15,
							"y" : 3,
							
							"text" : localeInfo.SATICI,
							
						},
					),	
				},
				{
					"name":"Money_Slot",
					"type":"button",

					"x":28-10+2+3+1+10,
 
                    "y":34,
					

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "left",
							"text_horizontal_align" : "left",

							"text" : "100.000.000",
						},
					),
				},
				{ "name":"anasayfabutton", "type":"button", "x":630, "y":35+7, "text":"Ana Sayfa", "default_image" : "d:/ymir work/ui/public/middle_button_01.sub", "over_image" : "d:/ymir work/ui/public/middle_button_02.sub", "down_image" : "d:/ymir work/ui/public/middle_button_03.sub", },
				{ "name":"itemlerimbutton", "type":"button", "x":701, "y":35+7, "text":localeInfo.ITEMLERIM, "default_image" : "d:/ymir work/ui/public/middle_button_01.sub", "over_image" : "d:/ymir work/ui/public/middle_button_02.sub", "down_image" : "d:/ymir work/ui/public/middle_button_03.sub", },
			),
		},
	),
}
