import pandas as pd
import user_input as ui
import models as md



def main_menu():
    set = ui.main_menu()
    if set == '1':
        frst_tm,frst_res,scnd_tm,scnd_res = md.add_game()
        md.tourn_tb_change(frst_tm,frst_res,scnd_tm,scnd_res)
        main_menu()
    if set == '2':
        df_table = pd.read_csv('tornt_tb.csv', sep=';', index_col='Team_name', encoding='cp1251')
        print(df_table)
        main_menu()
    if set == '3':      
        df_game = pd.read_csv('game.csv', sep=';', index_col='Date', encoding='cp1251')
        print(df_game)
        main_menu()



