import csv
import random
import shutil
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtCore import QSettings, QUrl, QTimer
from UIs.mainmenu_ui import Ui_mainWindow
from UIs.battle_ui import Ui_Form as Ui_battle
from UIs.escmenu_ui import Ui_Form as Ui_escmenu
from UIs.gameplay_v2_ui import Ui_Form as Ui_gameplay
from UIs.inventory_ui import Ui_Form as Ui_inventory
from UIs.settings_ui import Ui_Form as Ui_settings
from UIs.spellbook_ui import Ui_Form as Ui_spellbook
from UIs.trade_ui import Ui_Form as Ui_trade
from global_setup import app


class Data:
    """
    Работа с настройками и данными игры.
    """
    def __init__(self):
        self.difficulty_dict = {1: 'Easy', 2: 'Normal', 3: 'Hard'}
        self.settings = QSettings('Eluzium prod.', 'NELSON ENGINE')
        self.game_data = QSettings('Eluzium prod.', 'NELSON GAME')
        if not self.settings.value('difficulty'):
            self.settings_setup()

    def settings_setup(self):
        self.settings.setValue('difficulty', 2)
        self.settings.setValue('audio/music_volume', 100)
        self.settings.setValue('audio/sounds_volume', 100)

    def game_data_setup(self):
        self.game_data.setValue('dialogue_id', '0000')
        self.game_data.setValue('main_ch_name', 'None')
        self.game_data.setValue('main_ch_money', 0)
        self.game_data.setValue('main_ch_maxhp', 100)
        self.game_data.setValue('quests/tavern', False)


class Debug:
    def playing_bg_music(self, file, mode):
        print('Now playing: {}. Mode: {}'.format(file, mode))

    def playing_sound(self, file):
        print('Play sound: {}'.format(file))

    def data_change(self, argument, change):
        print('Data: {} changed to {}'.format(argument, change))

    def quit_from(self, place, couse):
        print('Game quit from {}. Couse: {}.'.format(place, couse))

    def trade_act(self, trader, item, inv1, inv2):
        print('Trade with {}. Item: {}. From {} to {}.'. format(trader.name, item, inv1, inv2))

    def split_up(self):
        print('-----')


data = Data()
debug = Debug()


class Character:
    def __init__(self, name, maxhp=100, money=100, state=None):
        self.name = name
        self.state = state
        self.maxhp = maxhp
        self.realtime_hp = maxhp
        self.money = money
        self.weapon_name = None
        self.damage = None
        self.armor_name = None
        self.protection = None
        self.set_selected_item('weapon', 'data/csv/main_hero/selected/weapon.csv')
        self.set_selected_item('armor', 'data/csv/main_hero/selected/armor.csv')

    def set_selected_item(self, type, file):
        """
        Функция загружает данные о надетых на персонажа предметах
        """
        with open(file, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            next(reader)
            item_info = reader.__next__()[0:2]
            if type == 'weapon':
                self.weapon_name = item_info[0]
                self.damage = item_info[1]
            elif type == 'armor':
                self.armor_name = item_info[0]
                self.protection = item_info[1]

    def set_armor(self, armor_name, protection):
        self.armor_name = armor_name
        self.protection = protection

    def trade_with(self):
        self.trade_with_ch = Trade(self, 'armor')
        self.trade_with_ch.show()

    def attack_damage(self):
        """
        Функция возвращает случайное число урона от заданного урона оружя
        прим: 18-25 -> 20
        """
        damage_interval = self.damage.split('-')
        if len(damage_interval) > 1:
            return random.randint(int(damage_interval[0]), int(damage_interval[1]))
        else:
            return int(damage_interval[0])

    def random_attack(self):
        """
        Функция возвращает случайное действие-аттаку персонажа из файла
        """
        with open('data/csv/characters/{}/attacks.txt'.format(self.name), mode='rt', encoding='utf-8') as attacks_io:
            attacks_step1 = attacks_io.read().split('\ufeff')
            attacks_step2 = attacks_step1[-1]
            attacks_list = attacks_step2.split('\n')
            choice = random.randint(0, len(attacks_list) - 1)
            return attacks_list[choice].split(':')


main_ch = Character('None')
morgan = Character('Морган', 0, 0, state='Врач')
jordan = Character('Джордан', 9999, 9999, state='Торговец оружием')
moira = Character('Мойра Браун', 9999, 9999, state='Торговец бронёй')
tavern = Character('Хозяин таверны', 999, 999, state='Трактирщик')
david = Character('Дэвид', maxhp=250, state='Алхимик-чародей')
kartush = Character('Картуш', maxhp=650, state='Разбойник')
mr_hankey = Character('Mr. Hankey', 99, 150, state='Trader')  # debug-персонаж. Не используется.


class MainMenu(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.continue_gameplay)
        self.newgame_btn.clicked.connect(self.restart_gameplay)
        self.settings_btn.clicked.connect(self.open_settings)
        self.quit_btn.clicked.connect(self.quit)
        if not data.game_data.value('main_ch_name'):
            self.continue_btn.setDisabled(True)
        play_background_music('menu_theme')

    def open_settings(self):
        play_sound('menu')
        self.settings = Settings()
        self.settings.show()

    def continue_gameplay(self):
        gameplay.dialog_mechanics(data.game_data.value('dialogue_id'))
        play_sound('menu')
        gameplay.show()
        self.close()

    def restart_gameplay(self):
        shutil.rmtree('data/csv')
        shutil.copytree('data/primary_csv', 'data/csv')
        data.game_data_setup()
        self.continue_gameplay()

    def quit(self):
        play_sound('menu')
        debug.quit_from(self, 'Quit button clicked')
        app.exit()


class Settings(QWidget, Ui_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.difficulty_spb.setValue(data.settings.value('difficulty'))
        self.difficulty_spb.valueChanged.connect(self.set_difficulty)
        self.difficulty_show_lb.setText(data.difficulty_dict[self.difficulty_spb.value()])
        self.music_slider.setValue(data.settings.value('audio/music_volume'))
        self.sounds_slider.setValue(data.settings.value('audio/sounds_volume'))
        self.music_per_lb.setText('Music: {}%'.format(data.settings.value('audio/music_volume')))
        self.sounds_per_lb.setText('Sounds: {}%'.format(data.settings.value('audio/sounds_volume')))
        self.music_slider.valueChanged.connect(self.set_music_volume_percent)
        self.sounds_slider.valueChanged.connect(self.set_sounds_volume_percent)
        self.ok_btn.clicked.connect(self.save_settings_then_close)
        self.apply_btn.clicked.connect(self.save_settings)
        self.cancel_btn.clicked.connect(self.unsave_settings)

    def set_difficulty(self):
        self.difficulty_show_lb.setText(data.difficulty_dict[self.difficulty_spb.value()])
        play_sound('point')

    def set_music_volume_percent(self):
        if self.music_slider.value() > 0:
            self.music_per_lb.setText('Music: {}%'.format(self.music_slider.value()))
        else:
            self.music_per_lb.setText('Music: OFF')

    def set_sounds_volume_percent(self):
        if self.sounds_slider.value() > 0:
            self.sounds_per_lb.setText('Sounds: {}%'.format(self.sounds_slider.value()))
        else:
            self.sounds_per_lb.setText('Sounds: OFF')

    def save_settings_then_close(self):
        self.save_settings()
        self.close()

    def save_settings(self):
        data.settings.setValue('audio/music_volume', self.music_slider.value())
        data.settings.setValue('audio/sounds_volume', self.sounds_slider.value())
        data.settings.setValue('difficulty', self.difficulty_spb.value())
        background_music.setVolume(data.settings.value('audio/music_volume'))
        data.settings.sync()
        if self.sender().text() == 'Apply':
            play_sound('point')
        else:
            play_sound('menu')

        # debug massage
        debug.split_up()
        debug.data_change('music volume', data.settings.value('audio/music_volume'))
        debug.data_change('sounds volume', data.settings.value('audio/sounds_volume'))
        debug.data_change('difficulty', data.settings.value('difficulty'))
        debug.split_up()

    def unsave_settings(self):
        play_sound('menu')
        self.close()


class Battle(QWidget, Ui_battle):
    def __init__(self, opponent, run_chance=50):
        super().__init__()
        self.setupUi(self)
        self.opponent = opponent
        self.opponent.realtime_hp = self.opponent.maxhp
        main_ch.realtime_hp = main_ch.maxhp
        self.iswin = False
        self.spell_used = False
        self.result = ''
        self.selected_spell_name = None
        self.selected_spell_damage = None
        self.run_chance = run_chance
        self.setWindowTitle('Battle')
        self.setup_opponent_info()
        self.setup_hero_info()
        self.setup_hp_info()
        self.set_hero_weapon()
        self.spellbook = Spellbook(self)
        self.weapon_attack_btn.clicked.connect(self.hero_attack)
        self.use_spell_btn.clicked.connect(self.hero_spell_attack)
        self.spell_book_btn.clicked.connect(self.open_spellbook)
        self.try_to_run_btn.clicked.connect(self.try_to_run)

    def setup_opponent_info(self):
        self.opponent_name_lb.setText('<html><body><p align="center"><span style=" font-size:12pt; '
                                      'font-weight:600;">{}</span></p></body></html>'.format(self.opponent.name))
        if self.opponent.state:
            self.opponent_state_lb.setText('<html><body><p align="center"><span style=" font-weight:600;">'
                                           '{}</span></p></body></html>'.format(self.opponent.state))
        else:
            self.opponent_state_lb.setText('')

    def setup_hero_info(self):
        self.hero_name_lb.setText('<html><body><p align="center"><span style=" font-size:12pt; font-weight:600;">'
                                  '{}</span></p></body></html>'.format(data.game_data.value('main_ch_name')))

    def setup_hp_info(self):
        self.hero_hp_lb.setText('<html><body><p align="center"><span style=" font-size:9pt;">HP: {}/{}'
                                '</span></p></body></html>'.format(main_ch.realtime_hp, main_ch.maxhp))
        self.opponent_hp_lb.setText('<html><body><p align="center"><span style=" font-size:9pt;">HP: {}/{}'
                                    '</span></p></body></html>'.format(self.opponent.realtime_hp, self.opponent.maxhp))

    def set_hero_weapon(self):
        self.weapon_attack_btn.setText("Ударить с {}  |  Damage: {}".format(main_ch.weapon_name, main_ch.damage))

    def set_attack_info(self, text, damage, damage_to):
        self.action_lb.setText('<html><body><p align="center"><span style=" font-size:14pt;">'
                               '{}</span></p></body></html>'.format(text))
        self.action_profit_lb.setText('<html><body><p align="center"><span style=" font-size:9pt;">'
                                      '{}: -{} HP</span></p></body></html>'.format(damage_to, damage))

    def opponent_attack(self):
        text, damage = self.opponent.random_attack()
        self.opponent.damage = damage
        damage = int(self.opponent.attack_damage() - int(main_ch.protection))
        if damage < 0:
            damage = 0
        self.set_attack_info('{} {}'.format(self.opponent.name, text), damage, data.game_data.value('main_ch_name'))
        self.attack_action(main_ch, damage)
        if self.iswin:
            self.opponent_win()
        self.setup_hp_info()
        self.enable_buttons()

    def hero_attack(self):
        sounds = ['sword01', 'sword02', 'sword03', 'punch']
        play_sound(random.choice(sounds))
        self.disable_buttons()
        damage = main_ch.attack_damage()
        self.set_attack_info('Вы ударили {} с {}'.format(self.opponent.name, main_ch.weapon_name),
                             damage, self.opponent.name)
        self.spell_used = False
        self.attack_action(self.opponent, damage)
        if self.iswin:
            self.hero_win()
        self.setup_hp_info()
        self.hero_attack_delay()

    def hero_spell_attack(self):
        if self.selected_spell_name:
            if self.selected_spell_name == 'FusRoDa':
                play_sound('fus-ro-dah')
            elif self.selected_spell_name == 'Fireball':
                play_sound('fireball')
            self.spell_used = True
            self.disable_buttons()
            self.set_attack_info('Вы использовали {} на {}'.format(self.selected_spell_name, self.opponent.name),
                                 self.selected_spell_damage, self.opponent.name)
            self.attack_action(self.opponent, self.selected_spell_damage)
            if self.iswin:
                self.hero_win()
            self.setup_hp_info()
            self.hero_attack_delay()
        else:
            self.battle_info("No spell selected!                    ", "Open spellbook and choose.")

    def attack_action(self, victim, damage):
        if victim.realtime_hp - int(damage) > 0:
            victim.realtime_hp -= int(damage)
        else:
            victim.realtime_hp = 0
            self.setup_hp_info()
            self.iswin = True

    def disable_buttons(self):
        self.weapon_attack_btn.setDisabled(True)
        self.use_spell_btn.setDisabled(True)
        self.spell_book_btn.setDisabled(True)
        self.try_to_run_btn.setDisabled(True)

    def enable_buttons(self):
        self.weapon_attack_btn.setDisabled(False)
        self.spell_book_btn.setDisabled(False)
        self.try_to_run_btn.setDisabled(False)
        if not self.spell_used:
            self.use_spell_btn.setDisabled(False)

    def hero_attack_delay(self):
        if not self.iswin:
            self.current_timer = QTimer()
            self.current_timer.timeout.connect(self.opponent_attack)
            self.current_timer.setSingleShot(True)
            self.current_timer.start(1700)

    def open_spellbook(self):
        self.spellbook.show()

    def battle_info(self, maintext, information=None):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Battle info")
        msg.setInformativeText(information)
        msg.setText(maintext)
        msg.show()

    def hero_win(self):
        background_music.stop()
        play_sound('win')
        self.result = 'win'
        self.action_lb.setText('<html><body><p align="center"><span style=" font-size:14pt;">'
                               'Вы выиграли!</span></p></body></html>')
        self.action_profit_lb.setText('')
        self.current_timer = QTimer()
        self.current_timer.timeout.connect(self.stop)
        self.current_timer.setSingleShot(True)
        self.current_timer.start(1500)

    def opponent_win(self):
        background_music.stop()
        play_sound('dead')
        self.result = 'lose'
        self.action_lb.setText('<html><body><p align="center"><span style=" font-size:14pt;">'
                               'Вы проиграли.</span></p></body></html>')
        self.action_profit_lb.setText('')
        self.current_timer = QTimer()
        self.current_timer.timeout.connect(self.stop)
        self.current_timer.setSingleShot(True)
        self.current_timer.start(1500)

    def try_to_run(self):
        self.disable_buttons()
        luck = random.randint(1, 100)
        if luck <= self.run_chance:
            self.result = 'run'
            self.action_lb.setText('<html><body><p align="center"><span style=" font-size:14pt;">'
                                   'Вам удалось сбежать!</span></p></body></html>')
            self.action_profit_lb.setText('')
            self.current_timer = QTimer()
            self.current_timer.timeout.connect(self.stop)
            self.current_timer.setSingleShot(True)
            self.current_timer.start(1500)
        else:
            self.action_lb.setText('<html><body><p align="center"><span style=" font-size:14pt;">'
                                   'Сбежать не удалось</span></p></body></html>')
            self.action_profit_lb.setText('')
            self.current_timer = QTimer()
            self.current_timer.timeout.connect(self.opponent_attack)
            self.current_timer.setSingleShot(True)
            self.current_timer.start(1500)
        print(luck)

    def stop(self):
        self.spellbook.close()
        gameplay.dialog_mechanics(None)
        self.close()


class EscMenu(QWidget, Ui_escmenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.continue_gameplay)
        self.settings_btn.clicked.connect(self.open_settings)
        self.mainmenu_btn.clicked.connect(self.tomainmenu)
        self.quit_btn.clicked.connect(self.quit)

    def open_settings(self):
        play_sound('menu')
        self.settings = Settings()
        self.settings.show()

    def continue_gameplay(self):
        play_sound('menu')
        self.close()

    def tomainmenu(self):
        gameplay.close()
        self.mainmenu = MainMenu()
        self.mainmenu.show()
        self.close()

    def quit(self):
        play_sound('menu')
        debug.quit_from(self, 'Quit button clicked')
        app.exit()


class Gameplay(QWidget, Ui_gameplay):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_money()
        self.set_enable_all()
        self.opponent = mr_hankey
        self.sendertext = ''
        self.through_counter = 0
        self.inventory_btn.clicked.connect(self.open_inv)
        self.menu_btn.clicked.connect(self.open_esc_menu)
        self.next_btn.clicked.connect(self.dialog_mechanics)
        self.answ_one_btn.clicked.connect(self.dialog_mechanics)
        self.answ_two_btn.clicked.connect(self.dialog_mechanics)
        self.answ_three_btn.clicked.connect(self.dialog_mechanics)
        self.answ_four_btn.clicked.connect(self.dialog_mechanics)
        self.set_variants()

    def dialog_mechanics(self, nowid):
        """
        основная функция взаимодействия с игроком.
        ячейка dialogue_id представляет реплику и варианты взаимодействия.
        см. dialogue_id == 'Pattern'
        """
        dialogue_id = data.game_data.value('dialogue_id')
        if nowid:
            dialogue_id = nowid

        if dialogue_id == '0000':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_phrase('Вот так! Мы очнулись!')
            self.set_variants('Что...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0001')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0001':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_phrase('Так, тихо, тихо. Тебе пришлось два дня пролежать без сознания.')
            self.set_variants('Что произошло?')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0002')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0002':
            self.opponent = morgan
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.set_dialog_name('Старик')
            self.set_phrase('Расслабься, подожди пару секунд. Нужно время, чтобы прийти в себя.')
            self.set_variants('...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0003')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0003':
            self.opponent = morgan
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.set_phrase('Посмотрим, что у тебя с головой. Как тебя зовут? Можешь сказать?')
            self.set_variants('Меня зовут...', 'Не твоего ума дело.', 'Я, кажется, не помню...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_main_ch_name('0004')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0005')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_dialogue_id('0006')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0004':
            self.opponent = morgan
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.set_dialog_name('Старик')
            self.set_phrase('{}, значит... Да уж. Я бы тебя так не назвал, конечно. Но какое имя дали, такое дали, '
                            'ничего не поделаешь.'.format(data.game_data.value('main_ch_name')))
            self.set_variants('Ну спасибо...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0010')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0005':
            self.opponent = morgan
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.set_phrase('Значит тебя зовут "Не твоего ума дело"?')
            self.set_dialog_name('Старик')
            self.set_variants('Ну, видимо так.', 'Эй!', 'Вообще-то я...')
            if self.sender():
                if self.sender().text() == '1' or self.sender().text() == '2':
                    self.noe()
                    data.game_data.setValue('main_ch_name', 'Не твоего ума дело')
                    self.set_dialogue_id('0004')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_main_ch_name('0004')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0006':
            play_background_music('sanctus_saint', mode='saveloop')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_location('Большая хижина')
            self.set_phrase('Не помнишь? Значит будем придумывать! Как тебе имя... хм... Роман?')
            self.set_variants('Вроде звучит...', 'Может что-то другое?', 'Давай лучше я...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    data.game_data.setValue('main_ch_name', 'Роман')
                    self.set_dialogue_id('0009')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0007')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_main_ch_name('0004')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0007':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_phrase('Ну нет так нет. А как насчет... Митч Коннер?')
            self.set_variants('Идеально!', 'Может что-то другое?', 'Давай лучше я...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    data.game_data.setValue('main_ch_name', 'Митч Коннер')
                    self.set_dialogue_id('0009')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0008')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_main_ch_name('0004')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0008':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_phrase('А ты видимо не торопишься, в отличие от меня... Отныне ты... Ренди!')
            self.set_variants('Пусть будет так.', 'Я вспомнил... Надеюсь.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    data.game_data.setValue('main_ch_name', 'Ренди')
                    self.set_dialogue_id('0009')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_main_ch_name('0004')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0009':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Большая хижина')
            self.opponent = morgan
            self.set_dialog_name('Старик')
            self.set_phrase('Ну вот и славно! Одного из моих детей тоже зовут {}. '
                            'Ты и представить не можешь как я её люблю...'.format(data.game_data.value('main_ch_name')))
            self.set_variants('Да, славно.', 'Угу. Стоп... её?')
            if self.sender():
                if self.sender().text() == '1' or self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0010')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0010':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Кажется, ты начал очухиваться, значит не забудешь мое имя как в прошлый раз. '
                            'Я Морган. Добро пожаловать в деревушку Гудспрингс.')
            self.set_variants('Гудспрингс?', 'В прошлый раз?', 'Как я здесь оказался?', '...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0011')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0012')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_dialogue_id('0013')
                elif self.sender().text() == '4':
                    self.noe()
                    self.set_dialogue_id('0015')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0011':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Да, Гудспрингс! Маленькая, но важная для любого путешественника деревушка в нашем '
                            'королевстве, ибо здесь можно пополнить запасы и найти работенку.')
            self.set_variants('Хм...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0014')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0012':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Ты уже просыпался несколько раз до этого, а в прошлый мы даже смогли дойти до моего имени,'
                            ' но ты его благополучно забыл. Как и всё остальное...')
            self.set_variants('...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0014')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0013':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Тебя нашли в паре шагов к северу от этих мест и принесли ко мне. Вот уже два дня лежишь.')
            self.set_variants('Вон оно как...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0014')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0014':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Хочешь еще чего узнать или мы можем продолжить?')
            self.set_variants('Гудспрингс?', 'В прошлый раз?', 'Как я здесь оказался?', 'Давай продолжим.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0011')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0012')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_dialogue_id('0013')
                elif self.sender().text() == '4':
                    self.noe()
                    self.set_dialogue_id('0015')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0015':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('На этот раз ты вроде как очухался полностью. И славно!')
            self.set_variants('Не то слово.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0016')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0016':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('А то! Ну что ж, можно и прощаться. На последок могу лишь дать тебе несколько шекелей, '
                            'чтобы ты тут с голоду не умер. Береги себя!')
            self.set_variants('Спасибо, Морган!')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    play_sound('receipt')
                    now_main_ch_money = data.game_data.value('main_ch_money') + 50
                    data.game_data.setValue('main_ch_money', now_main_ch_money)
                    self.set_dialogue_id('0017')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0017':
            play_background_music('sanctus_saint', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('+50₪', font_size=16)
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    play_sound('door')
                    self.set_dialogue_id('0018')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0018':
            play_background_music('hero_is_born', mode='saveloop')
            self.set_location('Гудспрингс', 'Улица')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('И так... Что дальше?')
            self.set_variants('Пойти на рынок', 'Пойти в таверну', 'Путь из Гудспрингс')
            if data.game_data.value('quests/tavern') == 'true':
                self.answ_two_btn.setDisabled(True)
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == '2':
                    self.noe()
                    play_sound('door')
                    self.set_dialogue_id('0024')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_dialogue_id('0038')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0019':
            play_background_music('farm_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Рынок')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Рынок. Что бы посмотреть...')
            self.set_variants('Броня', 'Оружие', 'Уйти с рынка')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0020')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0022')
                elif self.sender().text() == '3':
                    self.noe()
                    self.set_dialogue_id('0018')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0020':
            play_background_music('farm_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Рынок')
            self.opponent = moira
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Приветствую тебя, путник! Я - Мойра Браун, а это мой магазин. Хочешь приодеться?')
            self.set_variants('Покажи что у тебя есть.', 'Пожалуй, нет.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.trade = Trade(self.opponent, 'armor')
                    self.trade.show()
                    self.set_disable_all()
                    self.answ_one_btn.setDisabled(False)
                    self.sender().setText(self.sendertext)
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == 'Done':
                    self.set_enable_all()
                    self.set_dialogue_id('0021')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0021':
            play_background_music('farm_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Рынок')
            self.opponent = moira
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Приходите ещё, добрый путник!')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0022':
            play_background_music('farm_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Рынок')
            self.opponent = jordan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Privet, drug! Smotri glaza vibirai klinok!')
            self.set_variants('...', 'Я пойду...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.trade = Trade(self.opponent, 'weapon')
                    self.trade.show()
                    self.set_disable_all()
                    self.answ_one_btn.setDisabled(False)
                    self.sender().setText(self.sendertext)
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == 'Done':
                    self.set_enable_all()
                    self.set_dialogue_id('0023')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0023':
            play_background_music('farm_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Рынок')
            self.opponent = jordan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Poka, drug!')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0024':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Хм. День, а в харчевне столько людей. Тоже мне, работяги...')
            self.set_variants('Подойти к прилавку.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0025')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0025':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = tavern
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Новые лица... Чего изволите?')
            self.set_variants('В таврне имеется выпивка?', 'Я ищу работу.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0026')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0028')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0026':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = tavern
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Конечно. Эль за 5 шекелей, водка за 10 и вино за 15.')
            self.set_variants('Я возьму эль.', 'Я возьму водку.', 'Я возьму вино.', 'Пожалуй, воздержусь.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    if data.game_data.value('main_ch_money') >= 5:
                        play_sound('money_spend')
                        now_main_ch_money = data.game_data.value('main_ch_money') - 5
                        data.game_data.setValue('main_ch_money', now_main_ch_money)
                        self.set_dialogue_id('0027')
                    else:
                        self.no_money_error()
                        self.sender().setText(self.sendertext)
                elif self.sender().text() == '2':
                    self.noe()
                    if data.game_data.value('main_ch_money') >= 10:
                        play_sound('money_spend')
                        now_main_ch_money = data.game_data.value('main_ch_money') - 10
                        data.game_data.setValue('main_ch_money', now_main_ch_money)
                        self.set_dialogue_id('0027')
                    else:
                        self.no_money_error()
                        self.sender().setText(self.sendertext)
                elif self.sender().text() == '3':
                    self.noe()
                    if data.game_data.value('main_ch_money') >= 15:
                        play_sound('money_spend')
                        now_main_ch_money = data.game_data.value('main_ch_money') - 15
                        data.game_data.setValue('main_ch_money', now_main_ch_money)
                        self.set_dialogue_id('0027')
                    else:
                        self.no_money_error()
                        self.sender().setText(self.sendertext)
                elif self.sender().text() == '4':
                    self.noe()
                    self.set_dialogue_id('0027')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0027':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = tavern
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Что-нибудь ещё?')
            self.set_variants('Я ищу работу.')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0028')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0028':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = tavern
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Та-ак, работа. Да, есть одно дельце...')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0029')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0029':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = david
            self.set_dialog_name('Старик в мантии')
            self.set_phrase('{}! Тебя не должно здесь быть!'.format(data.game_data.value('main_ch_name')))
            self.set_variants('Что за...')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0030')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0030':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = david
            self.set_dialog_name('Старик в мантии')
            self.set_phrase('Я видел! Из-за тебя умрут они... Все!')
            self.set_variants('Кто ты?', 'Это становится все более странным...')
            if self.sender():
                if self.sender().text() == '1' or self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0031')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0031':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.hp_lb.setText('<html><body><p align="center">HP: 100/100</p></body></html>')
            self.opponent = david
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Мое имя - Дэвид! Я алхимик и чародей... Я чародей-алхимик! '
                            'Я здесь чтобы убить тебя и спасти их... Их всех!')
            self.set_variants('Вон оно как...', 'Придется помахать кулауами.')
            if self.sender():
                if type(self.sender()) == QTimer:
                    if self.battle.result == 'win':
                        self.set_enable_all()
                        self.set_dialogue_id('0032')
                    elif self.battle.result == 'lose':
                        self.dialog_mechanics('9999')
                    elif self.battle.result == 'run':
                        play_sound('door')
                        self.set_dialogue_id('0035')
                elif self.sender().text() == '1' or self.sender().text() == '2':
                    play_background_music('ready_for_battle_02', 'battle01', mode='intro')
                    play_sound('menu')
                    self.set_disable_all()
                    self.battle = Battle(self.opponent, run_chance=6)
                    self.battle.show()
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0032':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = david
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Н-нет... Они все умрут, слышишь, умрут...')
            self.set_variants()
            if self.sender():
                if type(self.sender()) == QTimer:
                    pass
                elif self.sender().text() == 'Next':
                    self.noe()
                    play_sound('receipt')
                    now_main_ch_money = data.game_data.value('main_ch_money') + 50
                    data.game_data.setValue('main_ch_money', now_main_ch_money)
                    self.set_dialogue_id('0033')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0033':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = david
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Победа над Дэвидом<br>+50₪', font_size=13)
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0034')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0034':
            play_background_music('tavern_theme', mode='saveloop')
            self.set_location('Гудспрингс', 'Таверна')
            self.opponent = tavern
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Эй! Дебошир! А ну вон из таверны, смри что устроили!')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    play_sound('door')
                    self.set_dialogue_id('0036')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0035':
            play_background_music('hero_is_born', mode='saveloop')
            self.set_location('Гудспрингс', 'Улица')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Мне удалось выбраться из таверны во время этой заварушки. Пока туда ни ногой')
            self.set_variants()
            if self.sender():
                if type(self.sender()) == QTimer:
                    pass
                elif self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0037')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0036':
            play_background_music('hero_is_born', mode='saveloop')
            self.set_location('Гудспрингс', 'Улица')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Тоже мне, я им чудаков сокращаю, а они...')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0037')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0037':
            data.game_data.setValue('quests/tavern', True)
            play_background_music('hero_is_born', mode='saveloop')
            self.set_location('Гудспрингс', 'Улица')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Ну-с. Куда дальше?')
            self.set_variants('Пойти на рынок', 'Путь из Гудспрингс')
            if self.sender():
                if self.sender().text() == '1':
                    self.noe()
                    self.set_dialogue_id('0019')
                elif self.sender().text() == '2':
                    self.noe()
                    self.set_dialogue_id('0038')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0038':
            play_background_music('elven_kingdom', mode='saveloop')
            self.set_location('Нильфгаард', 'Лесная дорога')
            self.opponent = main_ch
            self.set_dialog_name(data.game_data.value('main_ch_name'))
            self.set_phrase('Вот уже 2 часа иду и ничего не происходит. Удивительно...')
            self.set_variants()
            if self.sender():
                if self.sender().text() == 'Next':
                    self.noe()
                    self.set_dialogue_id('0039')
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0039':
            play_background_music('elven_kingdom', mode='saveloop')
            self.set_location('Нильфгаард', 'Лесная дорога')
            self.opponent = kartush
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Хе-ей. А кто тут у нас? А не хочет ли нашь маленткий друг немного '
                            'поделиться с дядей разбойником своими вещами?')
            self.set_variants('На 3 час пути все встало на свои места...')
            if self.sender():
                if type(self.sender()) == QTimer:
                    if self.battle.result == 'win':
                        self.set_enable_all()
                        self.set_dialogue_id('0040')
                    elif self.battle.result == 'lose':
                        self.dialog_mechanics('0041')
                    elif self.battle.result == 'run':
                        self.dialog_mechanics('9999')
                elif self.sender().text() == '1':
                    play_background_music('ready_for_battle_02', 'battle01', mode='intro')
                    play_sound('menu')
                    self.set_disable_all()
                    self.battle = Battle(self.opponent, run_chance=0)
                    self.battle.show()
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == '0040':
            play_background_music('elven_kingdom', mode='saveloop')
            self.set_location('Нильфгаард', 'Лесная дорога')
            self.opponent = kartush
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Победа победа вместо обеда!<br>ПРОДОЛЖЕНИЕ СЛЕДУЕТ<br>(Возможно)')
            self.set_variants()
            self.set_disable_all()

        elif dialogue_id == '0041':
            play_background_music('elven_kingdom', mode='saveloop')
            self.set_location('Нильфгаард', 'Лесная дорога')
            self.opponent = kartush
            self.set_dialog_name(self.opponent.name)
            self.set_phrase('Стыдно должно быть не тому кто проиграл, а тому кто не попытался выиграть.'
                            '<br>ПРОДОЛЖЕНИЕ СЛЕДУЕТ<br>(Возможно)')
            self.set_variants()
            self.set_disable_all()

        elif dialogue_id == '9999':
            # ячейка смерти
            # отсылаем игрока сюда при поражении
            # next_btn возвращает игрока на ячейку с боем
            play_background_music('church_theme', mode='saveloop')
            self.set_location('-')
            self.hp_lb.setText('<html><body><p align="center">HP: 0/100</p></body></html>')
            self.set_dialog_name('Смерть')
            self.set_phrase('{} сумел победить вас.<br>Чтобы продолжить, нажмите на кнопку Next'
                            .format(self.opponent.name))
            self.set_variants()
            if self.sender():
                if type(self.sender()) == QTimer:
                    pass
                elif self.sender().text() == 'Next':
                    self.noe()
                    pass
                elif self.sender().text() == 'Noe':
                    self.sender().setText(self.sendertext)

        elif dialogue_id == 'Pattern':
            play_background_music('hero_is_born', mode='saveloop')
            self.set_location('Гудспрингс', 'Хижина Моргана')
            self.opponent = morgan
            self.set_dialog_name(self.opponent.name)
            self.set_phrase(' ')
            self.set_variants()
            if self.sender():
                if self.sender().text() == '1':  # вариант ответа 1
                    self.noe()  # см. def noe()
                    pass
                elif self.sender().text() == '2':  # вариант ответа 2
                    self.noe()
                    pass
                elif self.sender().text() == '3':  # вариант ответа 3
                    self.noe()
                    pass
                elif self.sender().text() == '4':  # вариант ответа 4
                    self.noe()
                    pass
                elif self.sender().text() == 'Noe':  # возвращает текст кнопки в начальное состояние
                    self.sender().setText(self.sendertext)

    def set_dialogue_id(self, newid):
        self.set_money()
        data.game_data.setValue('dialogue_id', newid)
        self.dialog_mechanics(newid)

    def set_phrase(self, text, font_size=12):
        self.replica_show.setText("""<html><body><p align="center" style=" margin-top:0px; margin-bottom:0px; margin
        -left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'-apple-system'; 
        font-size:{}pt; color:#000000; background-color:#ffffff;">{}</span></p></body></html>""".format(font_size, text))

    def set_dialog_name(self, name):
        self.dialog_name_lb.setText('<html><body><p align="center"><span style=" font-size:14pt; font-weight:600;">'
                                    '{}</span></p></body></html>'.format(name))

    def set_variants(self, var1='-', var2='-', var3='-', var4='-', next_on=False):
        self.var1, self.var2, self.var3, self.var4 = var1, var2, var3, var4
        self.set_disable(next_on)
        self.answers_show.setText("""<html><head/><body><span style=" font-size:10pt;"><p>1. {}</p>
                                <p>2. {}</p>
                                <p>3. {}</p>
                                <p>4. {}</p></span></body></html>""".format(self.var1, self.var2, self.var3, self.var4))

    def set_disable(self, next_on):
        """
        выключает кнопки при отсутствии соответствующего варианта ответа
        если есть хоть один вариант ответа, next_btn отключается
        next_on = True принудительно включает next_btn при наличии вариантов ответа
        """
        self.answ_one_btn.setDisabled(True) if self.var1 == '-' else self.answ_one_btn.setDisabled(False)
        self.answ_two_btn.setDisabled(True) if self.var2 == '-' else self.answ_two_btn.setDisabled(False)
        self.answ_three_btn.setDisabled(True) if self.var3 == '-' else self.answ_three_btn.setDisabled(False)
        self.answ_four_btn.setDisabled(True) if self.var4 == '-' else self.answ_four_btn.setDisabled(False)
        if self.var1 == '-' and self.var2 == '-' and self.var3 == '-' and self.var4 == '-' or next_on:
            self.next_btn.setDisabled(False)
        else:
            self.next_btn.setDisabled(True)

    def set_disable_all(self):
        self.answ_one_btn.setDisabled(True)
        self.answ_two_btn.setDisabled(True)
        self.answ_three_btn.setDisabled(True)
        self.answ_four_btn.setDisabled(True)
        self.next_btn.setDisabled(True)
        self.inventory_btn.setDisabled(True)

    def set_enable_all(self):
        self.answ_one_btn.setDisabled(False)
        self.answ_two_btn.setDisabled(False)
        self.answ_three_btn.setDisabled(False)
        self.answ_four_btn.setDisabled(False)
        self.next_btn.setDisabled(False)
        self.inventory_btn.setDisabled(False)

    def set_location(self, fullsize_milieu, local_milieu=''):
        self.location_lb.setText('<html><body><p align="center">Location<br/>{}<br/>{}</p></body></html>'
                                 .format(fullsize_milieu, local_milieu))

    def set_money(self):
        self.money_lb.setText('<html><p align="center">₪: {}</p></body></html>'
                              .format(data.game_data.value('main_ch_money')))

    def no_money_error(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Trade fail")
        msg.setInformativeText("No money no honey ¯\_(ツ)_/¯")
        msg.setText("You need more shekels to buy it.")
        msg.show()

    def noe(self):
        """
        функция меняет текст на кнопке вариантов ответа
        без этого при нажатии кнопки будут вызываться соответствующие ответы во всей последовательности ячеек
        """
        self.sendertext = self.sender().text()
        self.sender().setText('Noe')

    def set_main_ch_name(self, next_dialogue_id):
        new_main_ch_name, okBtnPressed = QInputDialog.getText(self, "Введите имя",
                                                              "Как тебя зовут?")
        if okBtnPressed:
            if new_main_ch_name == '':
                data.game_data.setValue('main_ch_name', 'Noname')
            else:
                data.game_data.setValue('main_ch_name', new_main_ch_name)
            self.set_dialogue_id(next_dialogue_id)

    def open_trade(self):
        self.opponent.trade_with()
        play_sound('menu')

    def open_inv(self):
        self.inv = Inventory()
        self.inv.show()
        play_sound('menu')

    def open_esc_menu(self):
        self.esc = EscMenu()
        self.esc.show()
        play_sound('menu')


gameplay = Gameplay()


class Inventory(QWidget, Ui_inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.item_to_select = None
        self.set_selected_info()
        self.money_lb.setText('<html><body><p align="right"><span style=" font-size:9pt;">₪: {}'
                              '</span></p></body></html>'.format(data.game_data.value('main_ch_money')))
        loadInventory('data/csv/main_hero/main.csv', self.main_table)
        loadInventory('data/csv/main_hero/weapon.csv', self.weapon_table)
        loadInventory('data/csv/main_hero/armor.csv', self.armor_table)
        loadInventory('data/csv/main_hero/spells.csv', self.spellbook_table)
        loadInventory('data/csv/main_hero/selected/weapon.csv', self.weapon_selected_table)
        loadInventory('data/csv/main_hero/selected/armor.csv', self.armor_selected_table)
        loadInventory('data/csv/other/deleted_weapon.csv', self.weapon_deleted_table)
        loadInventory('data/csv/other/deleted_armor.csv', self.armor_deleted_table)
        self.delete_btn.clicked.connect(self.delete_item)
        self.done_btn.clicked.connect(self.inventory_close)
        self.select_btn.clicked.connect(self.prepare_to_select_item)
        self.inventory_tabs.currentChanged.connect(self.set_choose_mode)
        self.armor_table.itemDoubleClicked.connect(self.choose_item)
        self.weapon_table.itemDoubleClicked.connect(self.choose_item)

    def set_choose_mode(self):
        """
        активирует и деактивирует возможность выбора предмета в инвентаре
        зависит от выбранной таблицы
        """
        if self.inventory_tabs.currentIndex() in (0, 3):
            self.select_btn.setDisabled(True)
            self.delete_btn.setDisabled(True)
            self.setup_no_action_mode()
        elif self.inventory_tabs.currentIndex() in (1, 2):
            self.select_btn.setDisabled(False)
            self.delete_btn.setDisabled(False)
            self.setup_item_info()

    def setup_item_info(self):
        self.item_lb.setText('<html><body><p align="center"><span style=" font-size:12pt; font-weight:600;">'
                             'Choose item</span></p></body></html>')
        self.item_stat_lb.setText('<html><head/><body><p align="center"><span style=" font-size:9pt;">'
                                  '-</span></p></body></html>')
        self.item_to_select = None

    def setup_no_action_mode(self):
        self.item_lb.setText('<html><body><p align="center"><span style=" font-size:12pt; font-weight:600;">'
                             'No actions</span></p></body></html>')
        self.item_stat_lb.setText('<html><head/><body><p align="center"><span style=" font-size:9pt;">'
                                  '-</span></p></body></html>')

    def edit_item_info(self):
        self.item_lb.setText('<html><body><p align="center"><span style=" font-size:12pt; font-weight:600;">'
                             '{}</span></p></body></html>'.format(self.item_to_select[0].text()))
        self.item_stat_lb.setText('<html><head/><body><p align="center"><span style=" font-size:9pt;">{} {}</span></p>'
                                  '</body></html>'.format(self.item_to_select[1].text(),
                                                          self.sender().horizontalHeaderItem(1).text()))

    def choose_item(self):
        play_sound('point')
        self.item_to_select = self.sender().selectedItems()
        self.edit_item_info()

    def prepare_to_select_item(self):
        if self.item_to_select:
            if self.inventory_tabs.currentIndex() == 1:
                self.select_item(self.weapon_table, self.weapon_selected_table, 'weapon')
                self.set_selected_weapon()
            elif self.inventory_tabs.currentIndex() == 2:
                self.select_item(self.armor_table, self.armor_selected_table, 'armor')
                self.set_selected_armor()
            self.setup_item_info()
            self.set_selected_info()

    def select_item(self, inventory_table, select_table, type):
        play_sound('receipt')
        item_to_unselect = list()
        [item_to_unselect.append(select_table.item(0, i)) for i in range(3)]
        replace_item(select_table, inventory_table, item_to_unselect)
        replace_item(inventory_table, select_table, self.item_to_select)
        saveToCsv('data/csv/main_hero/{}.csv'.format(type), inventory_table)
        saveToCsv('data/csv/main_hero/selected/{}.csv'.format(type), select_table)

    def set_selected_weapon(self):
        main_ch.weapon_name = self.weapon_selected_table.item(0, 0).text()
        main_ch.damage = self.weapon_selected_table.item(0, 1).text()

    def set_selected_armor(self):
        main_ch.armor_name = self.armor_selected_table.item(0, 0).text()
        main_ch.protection = self.armor_selected_table.item(0, 1).text()

    def set_selected_info(self):
        self.selected_weapon_lb.setText('<html><body><p align="center">| Weapon |<br/><b>{}<br/>{}'
                                        ' damage</b></p></body></html>'.format(main_ch.weapon_name, main_ch.damage))
        self.selected_armor_lb.setText('<html><body><p align="center">| Armor |<br/><b>{}<br/>{} protection'
                                       '</b></p></body></html>'.format(main_ch.armor_name, main_ch.protection))

    def delete_item(self):
        if self.item_to_select:
            if self.inventory_tabs.currentIndex() == 1:
                replace_item(self.weapon_table, self.weapon_deleted_table, self.item_to_select)
                saveToCsv('data/csv/main_hero/weapon.csv', self.weapon_table)
                saveToCsv('data/csv/other/deleted_weapon.csv', self.weapon_deleted_table)
            elif self.inventory_tabs.currentIndex() == 2:
                replace_item(self.armor_table, self.armor_deleted_table, self.item_to_select)
                saveToCsv('data/csv/main_hero/armor.csv', self.armor_table)
                saveToCsv('data/csv/other/deleted_armor.csv', self.armor_deleted_table)
            self.setup_item_info()

    def inventory_close(self):
        play_sound('menu')
        self.close()


class Trade(QWidget, Ui_trade):
    def __init__(self, trader, type):
        super().__init__()
        self.setupUi(self)
        self.trader = trader
        self.isEnded = False
        self.main_inv = 'data/csv/main_hero/{}.csv'.format(type)
        self.trader_inv = 'data/csv/characters/{}/{}.csv'.format(self.trader.name, type)
        self.hero_name_lb.setText('<html><body><p><span style=" font-size:11pt; font-weight:600;">'
                                  '{}</span></p></body></html>'.format(data.game_data.value('main_ch_name')))
        self.trader_name_lb.setText('<html><body><p align="right"><span style=" font-size:11pt; font-weight:600;">'
                                    '{}</span></p></body></html>'.format(self.trader.name))
        self.setWindowTitle('Trade with {}'.format(self.trader.name))
        self.set_money_label()
        self.trade_action = None
        self.trade_item = None
        self.profit = ''
        self.price = 0
        self.ok_trade_btn.clicked.connect(self.do_trade)
        self.done_btn.clicked.connect(self.trade_close)
        self.cancel_trade_btn.clicked.connect(self.setup_trade_info)
        self.hero_table.itemDoubleClicked.connect(self.choose_to_sell)
        self.trader_table.itemDoubleClicked.connect(self.choose_to_buy)
        loadInventory(self.trader_inv, self.trader_table)
        loadInventory(self.main_inv, self.hero_table)

    def choose_to_sell(self):
        self.trade_action = 'Sell'
        self.trade_item = self.hero_table.selectedItems()
        self.edit_trade_info()

    def choose_to_buy(self):
        self.trade_action = 'Buy'
        self.trade_item = self.trader_table.selectedItems()
        self.edit_trade_info()

    def setup_trade_info(self):
        self.trade_action = None
        self.trade_item = None
        self.profit = ''
        self.trade_action_lb.setText('<html><body><p align="center"><span style=" '
                                     'font-size:10pt;">-</span></p></body></html>')
        self.item_lb.setText('<html><head/><body><p align="center"><span style=" '
                             'font-size:12pt; font-weight:600;">Choose item</span></p></body></html>')
        self.profit_lb.setText('<html><head/><body><p align="center"><span style=" '
                               'font-size:9pt;">0 ₪</span></p></body></html>')

    def edit_trade_info(self):
        play_sound('point')
        if self.trade_action == 'Sell':
            self.profit = '+' + self.trade_item[-1].text()
        elif self.trade_action == 'Buy':
            self.profit = '-' + self.trade_item[-1].text()
        else:
            self.profit = self.trade_item[-1].text()

        self.trade_action_lb.setText('<html><body><p align="center"><span style="font-size:10pt;">{} item #{}</span>'
                                     '</p></body></html>'.format(self.trade_action, self.trade_item[0].row() + 1))
        self.item_lb.setText('<html><body><p align="center"><span style="font-size:12pt; font-weight:600;">{}'
                             '</span></p></body></html>'.format(self.trade_item[0].text()))
        self.profit_lb.setText('<html><body><p align="center"><span style=" '
                               'font-size:9pt;">{} ₪</span></p></body></html>'.format(self.profit))

    def do_trade(self):
        if self.is_enough_money():
            self.price = int(self.trade_item[-1].text())
            if self.trade_action == 'Sell':
                play_sound('money_income')
                debug.trade_act(self.trader, self.trade_item[0].text(), self.main_inv, self.trader_inv)
                replace_item(self.hero_table, self.trader_table, self.trade_item)
            elif self.trade_action == 'Buy':
                play_sound('money_spend')
                debug.trade_act(self.trader, self.trade_item[0].text(), self.trader_inv, self.main_inv)
                replace_item(self.trader_table, self.hero_table, self.trade_item)
            self.do_payment()

            saveToCsv(self.trader_inv, self.trader_table)
            saveToCsv(self.main_inv, self.hero_table)

            self.setup_trade_info()

        elif not self.is_enough_money():
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Trade fail")
            msg.setInformativeText("No money no honey ¯\_(ツ)_/¯")
            if self.trade_action == 'Buy':
                msg.setText("You need more shekels to buy {}.".format(self.trade_item[0].text()))
            elif self.trade_action == 'Sell':
                msg.setText("{} doesn't have enough shekels to buy {}."
                                       .format(self.trader.name, self.trade_item[0].text()))
            elif not self.trade_action:
                msg.setText("You should choose an item for buy or sale.")
                msg.setInformativeText('Try double-click on any item.')
            else:
                msg.setText("Something went wrong.\n(And I don’t know why)")
                msg.setInformativeText('¯\_(ツ)_/¯')
            msg.show()

    def is_enough_money(self):
        if self.trade_action == 'Sell' and self.trader.money >= int(self.trade_item[-1].text()):
            return True
        elif self.trade_action == 'Buy' and data.game_data.value('main_ch_money') >= int(self.trade_item[-1].text()):
            return True
        return False

    def do_payment(self):
        if self.trade_action == 'Sell':
            now_main_ch_money = data.game_data.value('main_ch_money') + self.price
            data.game_data.setValue('main_ch_money', now_main_ch_money)
            self.trader.money -= self.price
        elif self.trade_action == 'Buy':
            now_main_ch_money = data.game_data.value('main_ch_money') - self.price
            data.game_data.setValue('main_ch_money', now_main_ch_money)
            self.trader.money += self.price
        self.set_money_label()

    def set_money_label(self):
        self.hero_money_lb.setText("""<html><body><p align="right"><span style=" font-family:'sans-serif'; 
        font-size:10pt; font-weight:600;">₪: {}</span></p></body></html>""".format(data.game_data.value('main_ch_money')))
        self.trader_money_lb.setText("""<html><body><p><span style=" font-family:'sans-serif'; font-size:10pt; 
        font-weight:600;">₪: {}</span></p></body></html>""".format(self.trader.money))

    def trade_close(self):
        play_sound('menu')
        self.isEnded = True
        gameplay.dialog_mechanics(data.game_data.value('dialogue_id'))
        self.close()


class Spellbook(QWidget, Ui_spellbook):
    def __init__(self, battle):
        super().__init__()
        self.setupUi(self)
        self.battle = battle
        self.set_selected_spell()
        self.spells_table.itemDoubleClicked.connect(self.select_spell)
        loadInventory('data/csv/main_hero/spells.csv', self.spells_table)

    def set_selected_spell(self):
        self.selected_lb.setText('<html><body><p align="center"><span style=" font-size:10pt; font-weight:600;">'
                                 'Selected: {}</span></p></body></html>'.format(self.battle.selected_spell_name))

    def select_spell(self):
        self.battle.selected_spell_name = self.spells_table.selectedItems()[0].text()
        self.battle.selected_spell_damage = self.spells_table.selectedItems()[1].text()
        self.set_selected_spell()


def replace_item(output_table, input_table, item):
        input_table.insertRow(input_table.rowCount())
        column_to_place = 0
        for item in item:
            input_table.setItem(input_table.rowCount() - 1, column_to_place, QTableWidgetItem(item.text()))
            column_to_place += 1
        output_table.removeRow(item.row())


def loadInventory(inventory_file, table):
    with open(inventory_file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        title = next(reader)
        table.setColumnCount(len(title))
        table.setHorizontalHeaderLabels(title)
        table.setRowCount(0)
        for i, row in enumerate(reader):
            table.setRowCount(table.rowCount() + 1)
            for j, elem in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(elem))
    table.resizeColumnsToContents()


def saveToCsv(filename, table):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([table.horizontalHeaderItem(i).text()
                            for i in range(table.columnCount())])
        for i in range(table.rowCount()):
            row = []
            for j in range(table.columnCount()):
                item = table.item(i, j)
                if item is not None:
                    row.append(item.text())
            writer.writerow(row)


def play_sound(filename):
    global sound
    media = QUrl.fromLocalFile('data/audio/sounds/{}.mp3'.format(filename))
    sound = QtMultimedia.QMediaPlayer()
    sound.setMedia(QtMultimedia.QMediaContent(media))
    if data.settings.value('audio/sounds_volume'):
        sound.setVolume(data.settings.value('audio/sounds_volume'))
        sound.play()
        debug.playing_sound(sound.media().canonicalUrl().path())


def play_background_music(*filenames, mode='loop'):
    """
    проигрвает музыку в разных режимах:
    loop: проигрывание списка по кругу.
    saveloop: проигрывание песни по кругу. Если вызванная песня уже играет, то проигрывание не будет прервано.
    intro: первая песня из списка играет один раз. Все следующие по кругу.
    """
    global background_music, playlist, bg_mode, bg_filenames, playing_filename
    if mode != 'saveloop' or filenames[0] != playing_filename:
        bg_mode = mode
        bg_filenames = filenames
        playing_filename = filenames[0]
        playlist = QtMultimedia.QMediaPlaylist()
        for filename in filenames:
            media = QUrl.fromLocalFile('data/audio/music/{}.mp3'.format(filename))
            playlist.addMedia(QtMultimedia.QMediaContent(media))
        playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        background_music = QtMultimedia.QMediaPlayer()
        background_music.setVolume(data.settings.value('audio/music_volume'))
        background_music.setPlaylist(playlist)
        background_music.play()
        background_music_debug()
        playlist.currentMediaChanged.connect(background_music_debug)
        playlist.currentIndexChanged.connect(background_intro_delete)


def background_music_debug():
    if not playlist.isEmpty():
            debug.playing_bg_music(playlist.currentMedia().canonicalUrl().path(), bg_mode)


def background_intro_delete():
    if bg_mode == 'intro':
        playlist.clear()
        play_background_music(*bg_filenames[1:])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
    sys.excepthook = except_hook
    main_window = MainMenu()
    main_window.show()
    sys.exit(app.exec_())