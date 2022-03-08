quest alisveris begin
	state start begin
		-- [Ýtemi alisverise koyma]
		when 20092.take begin
			local id = item.get_id()
			local vnum = item.get_vnum()
			local item_isim = item.get_name()
			local isim = pc.get_name()
			local bul = mysql_query('SELECT * FROM player.item WHERE id = \\"'..id..'\\"')
			say_title("Merhaba "..isim)
			say_item_vnum(vnum)
			wait()
			say("Ýtemi alisveris'e koymak istediðine emin misin?")
			local karar = select(locale.yes, locale.no)
			if karar == 2 then
				say("Açýk arttýrma sayesinde gayet iyi[ENTER]para kazanabilirdin.")
				say("Ama yine de sen bilirsin.")
			elseif karar == 1 then
				say_title("Açýk Arttýrma:")
				say("Ýtem için kaç para istiyorsun?")
				local para = tonumber(input())
				if para == "0" or para == 0 or para == nil then
					say("Boþ býrakamazsýnýz.")
				elseif para > 2000000000 then
					say("Maksimum 2T koyabilirsin.")
				else
					notice(item_isim.." açýk arttýrmaya "..para.." yang karþýlýðý konuldu.")
					--pc.remove_item(vnum)
					chat(id)
					syschat(bul.socket0[1])
					chat(bul.socket0[1])
					local ac = io.open('/usr/game/share/locale/turkey/quest/alisveris/itemler.txt', "a+")
					--ac:write(bul.socket4[1])
					ac:close()
					--ac:write(bul.socket0[1]..'#'..bul.socket1[1]..'#'..bul.socket2[1]..'#'..bul.socket3[1]..'#'..bul.socket4[4]..'#'..bul.socket5[1]..'#'..bul.attrtype0[1]..'#'..bul.attrvalue0[1]..'#'..bul.attrtype1[1]..'#'..bul.attrvalue1[1]..'#'..bul.attrtype2[1]..'#'..bul.attrvalue2[1]..'#'..bul.attrtype3[1]..'#'..bul.attrvalue3[1]..'#'..bul.attrtype4[1]..'#'..bul.attrvalue4[1]..'#'..bul.attrtype5[1]..'#'..bul.attrvalue5[1]..'#'..bul.attrtype6[1]..'#'..bul.attrvalue6[1])
					--ac:write('#'..pc.get_name()..'#'..vnum..'#'..para..'#'..bul.socket0[1]..'#'..bul.socket1[1]..'#'..bul.socket2[1]..'#'..bul.socket3[1]..'#'..bul.socket4[4]..'#'..bul.socket5[1]..'#'..bul.attrtype0[1]..'#'..bul.attrvalue0[1]..'#'..bul.attrtype1[1]..'#'..bul.attrvalue1[1]..'#'..bul.attrtype2[1]..'#'..bul.attrvalue2[1]..'#'..bul.attrtype3[1]..'#'..bul.attrvalue3[1]..'#'..bul.attrtype4[1]..'#'..bul.attrvalue4[1]..'#'..bul.attrtype5[1]..'#'..bul.attrvalue5[1]..'#'..bul.attrtype6[1]..'#'..bul.attrvalue6[1])
					--ac:close()
					local ac2 = io.open('/usr/game/share/locale/turkey/quest/alisveris/'..pc.get_name(), "r")
					if ac2 == nil then
						os.execute("mkdir ".."/usr/game/share/locale/turkey/quest/alisveris/"..pc.get_name())
						local ac3 = io.open('/usr/game/share/locale/turkey/quest/alisveris/'..pc.get_name()..'/para.txt', "w")
						ac3:write("0")
						ac3:close()
					end
					--ac:write('#'..pc.get_name()..'#'..vnum..'#'..para..'#'..bul.socket0[1]..'#'..bul.socket1[1]..'#'..bul.socket2[1]..'#'..bul.socket3[1]..'#'..bul.socket4[4]..'#'..bul.socket5[1]..'#'..bul.attrtype0[1]..'#'..bul.attrvalue0[1]..'#'..bul.attrtype1[1]..'#'..bul.attrvalue1[1]..'#'..bul.attrtype2[1]..'#'..bul.attrvalue2[1]..'#'..bul.attrtype3[1]..'#'..bul.attrvalue3[1]..'#'..bul.attrtype4[1]..'#'..bul.attrvalue4[1]..'#'..bul.attrtype5[1]..'#'..bul.attrvalue5[1]..'#'..bul.attrtype6[1]..'#'..bul.attrvalue6[1]..'#\\n')
						--ac:write('deneme : '..bul.attrtype0[1]..'#'..bul.attrvalue0[1]..'#'..bul.attrtype1[1]..'#'..bul.attrvalue1[1]..'#'..bul.attrtype2[1]..'#'..bul.attrvalue2[1]..'#'..bul.attrtype3[1]..'#'..bul.attrvalue3[1]..'#'..bul.attrtype4[1]..'#'..bul.attrvalue4[1]..'#'..bul.attrtype5[1]..'#'..bul.attrvalue5[1]..'#'..bul.attrtype6[1]..'#'..bul.attrvalue6[1])
				end
			end
		end
		
		-- [Alisveris penceresini açma]
		
		when 20092.chat."Alisveris" begin
			say("Alisveris sistemini açmak istiyormusun?")
			local ac = select("Evet", "Hayir")
			if ac == 2 then
				return
			elseif ac == 1 then
				syschat('Alisveris sistemi açildi.')
				cmdchat("LuaToPython alisverisopen")
				local ac = io.open('/usr/game/share/locale/turkey/quest/alisveris/itemler.txt', "r")
				for i in ac:lines() do
					if string.find(i, pc.get_name()) != -1 then
						cmdchat("LuaToPython "..'myitems'..i)
					else
						cmdchat("LuaToPython "..'itemler'..i)
					end
				end
			end
		end
		
		-- [Python to Lua iþlemleri]
		
		when login begin
			cmdchat("PythonToLua"..q.getcurrentquestindex())
		end
		when button begin
			local islem = getinput("PythonIslem")
			if islem == "MoneyAyarlari" then
				local aco = io.open('/usr/game/share/locale/turkey/quest/alisveris/'..pc.get_name()..'.txt', "r")
				local ac3 = aco:read()
				say_title("Alisveris parasý(AP) Ayarlarý:")
				if aco == nil then	
					say("Toplam AP : 0")
				else
					say("Toplam AP : "..tonumber(ac3))
				end
				say("Ne yapmak istiyorsun?")
				local s = select("Para yatýr", "Para çek")
				if s == 1 then
					say("Kaç para yatýrmak istiyorsun?")
					local yatir = input()
					if yatir == "" or yatir == 0 or yatir == nil then
						say("Bir miktar girin...")
					else
						if yatir > pc.get_money() then 
							syschat('Bu kadar paran yok..') 
							return
						else
							local eski = tonumber(ac3)
							local yeni = eski + yatir
							local acw = io.open('/usr/game/share/locale/turkey/quest/alisveris/'..pc.get_name()..'.txt', "w")
							acw:write(yeni)
							notice('Para baþarýyla Alisveris parasýna yatýrýldý.')
						end
					end
				elseif s == 2 then
					say("Toplam paran : "..ac3)
					local n = input()
					if n == "0" or n == 0 or n == nil then
						say("Boþ býrakamassýn")
					else
						if n > tonumber(ac3) then
							syschat('Alisveris paranda o kadar para yok..')
						else
							local old = tonumber(ac3)
							local new = old - n
							pc.change_money(n)
							syschat(n..' yang alisveris parandan çekildi.')
						end
					end
				end
			end
		end
	end
end